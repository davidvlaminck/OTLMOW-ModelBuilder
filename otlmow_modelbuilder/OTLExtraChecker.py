from pathlib import Path


class OTLExtraChecker:
    @classmethod
    def modify_for_extra_checks(cls, directory: Path) -> None:
        cls.modify_naamfield(directory)

    @classmethod
    def modify_naamfield(cls, directory: Path) -> None:
        naamfield_path = directory / 'Classes/ImplementatieElement/AIMNaamObject.py'
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
"        if StringField.validate(value, attribuut):\n",
"            return re.match('^[a-zA-Z0-9.\\-_]*$', value) is not None\n",
"        else:\n",
"            return False\n", '\n']

        for index, line in enumerate(block):
            lines.insert(class_line_number + index, line)

        with open(naamfield_path, 'w') as f:
            f.writelines(lines)

