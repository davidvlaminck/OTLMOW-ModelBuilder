from pathlib import Path


class OTLExtraChecker:
    @classmethod
    def modify_for_extra_checks(cls, directory: Path) -> None:
        cls.modify_naamfield(directory)
        cls.modify_naampad_field(directory)

    @classmethod
    def modify_naamfield(cls, directory: Path) -> None:
        naamfield_path = directory / 'Classes/ImplementatieElement/AIMNaamObject.py'
        if not naamfield_path.exists():
            return

        with open(naamfield_path, 'r') as f:
            lines = f.readlines()

        if 'import re' not in lines:
            lines.insert(1, '\n')
            lines.insert(1, 'import re\n')

        namefield_line_number = lines.index("        self._naam = OTLAttribuut(field=StringField,\n")
        lines[namefield_line_number] = "        self._naam = OTLAttribuut(field=NaamField,\n"

        class_line_number = lines.index('class AIMNaamObject(AIMObject):\n') - 2
        block = ['\n', "class NaamField(StringField):\n",
"    def __init__(self, naam: str, label: str, objectUri: str, definition: str, owner):\n",
"        super().__init__(naam, label, objectUri, definition, owner)\n",
"\n",
"    @classmethod\n",
"    def validate(cls, value, attribuut) -> bool:\n",
'        if not StringField.validate(value, attribuut):\n',
'            return False\n',
"        if re.match(r'^[\\w.\\-]*$', value) is None:\n",
'            return False\n',
"        if hasattr(attribuut.owner, 'naampad') and attribuut.owner.naampad is not None:\n",
"            return attribuut.owner.naampad.split('/')[-1] == value\n",
'        return True\n',
 "\n",
"    @classmethod\n",
"    def create_dummy_data(cls) -> str:\n",
"        return 'dummy'", '\n']

        for index, line in enumerate(block):
            lines.insert(class_line_number + index, line)

        with open(naamfield_path, 'w') as f:
            f.writelines(lines)

    @classmethod
    def modify_naampad_field(cls, directory: Path) -> None:
        naampad_path = directory / 'Classes/ImplementatieElement/NaampadObject.py'
        if not naampad_path.exists():
            return

        with open(naampad_path) as f:
            lines = f.readlines()

        if 'import re' not in lines:
            lines.insert(1, '\n')
            lines.insert(1, 'import re\n')

        lines.remove("from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField\n")

        namefield_line_number = lines.index("        self._naampad = OTLAttribuut(field=StringField,\n")
        lines[namefield_line_number] = "        self._naampad = OTLAttribuut(field=NaampadField,\n"

        namefield_line_number = lines.index("from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject\n")
        lines[namefield_line_number] = "from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject, NaamField\n"

        class_line_number = lines.index('class NaampadObject(AIMNaamObject):\n') - 2
        block = ['\n', "class NaampadField(NaamField):\n",
"    def __init__(self, naam: str, label: str, objectUri: str, definition: str, owner):\n",
"        super().__init__(naam, label, objectUri, definition, owner)\n",
"\n",
"    @classmethod\n",
"    def validate(cls, value, attribuut) -> bool:\n",
"        if re.match(r'^[\\w.\\-]+[/[\\w.\\-]+]*$', value) is None:\n",
"            return False\n",
"        if attribuut.owner.naam is not None:\n",
"            return value.split('/')[-1] == attribuut.owner.naam\n",
"        return True\n",
"\n",
"    @classmethod\n",
"    def create_dummy_data(cls) -> str:\n",
"        return 'dummy/dummy'", '\n']

        for index, line in enumerate(block):
            lines.insert(class_line_number + index, line)

        with open(naampad_path, 'w') as f:
            f.writelines(lines)
