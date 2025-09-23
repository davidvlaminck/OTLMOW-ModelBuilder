UPDATE InternalBaseClass
SET class_uri = REPLACE(class_uri, '-test', '')
WHERE class_uri LIKE '%-test%';

UPDATE InternalBaseClass
SET base_uri = REPLACE(base_uri, '-test', '')
WHERE base_uri LIKE '%-test%';

UPDATE OSLOClass
SET uri = REPLACE(uri, '-test', '')
WHERE uri LIKE '%-test%';

UPDATE OSLOAttributen
SET uri = REPLACE(uri, '-test', '')
WHERE uri LIKE '%-test%';

UPDATE OSLOAttributen
SET class_uri = REPLACE(class_uri, '-test', '')
WHERE class_uri LIKE '%-test%';

UPDATE OSLOAttributen
SET "type" = REPLACE("type", '-test', '')
WHERE "type" LIKE '%-test%';

UPDATE OSLODatatypeComplex
SET uri = REPLACE(uri, '-test', '')
WHERE uri LIKE '%-test%';

UPDATE OSLODatatypeComplexAttributen
SET uri = REPLACE(uri, '-test', '')
WHERE uri LIKE '%-test%';

UPDATE OSLODatatypeComplexAttributen
SET "type" = REPLACE("type", '-test', '')
WHERE "type" LIKE '%-test%';

UPDATE OSLODatatypeComplexAttributen
SET class_uri = REPLACE(class_uri, '-test', '')
WHERE class_uri LIKE '%-test%';

UPDATE OSLODatatypePrimitive
SET uri = REPLACE(uri, '-test', '')
WHERE uri LIKE '%-test%';

UPDATE OSLODatatypePrimitiveAttributen
SET uri = REPLACE(uri, '-test', '')
WHERE uri LIKE '%-test%';

UPDATE OSLODatatypePrimitiveAttributen
SET "type" = REPLACE("type", '-test', '')
WHERE "type" LIKE '%-test%';

UPDATE OSLODatatypePrimitiveAttributen
SET class_uri = REPLACE(class_uri, '-test', '')
WHERE class_uri LIKE '%-test%';

UPDATE OSLODatatypeUnion
SET uri = REPLACE(uri, '-test', '')
WHERE uri LIKE '%-test%';

UPDATE OSLODatatypeUnionAttributen
SET uri = REPLACE(uri, '-test', '')
WHERE uri LIKE '%-test%';

UPDATE OSLODatatypeUnionAttributen
SET "type" = REPLACE("type", '-test', '')
WHERE "type" LIKE '%-test%';

UPDATE OSLODatatypeUnionAttributen
SET class_uri = REPLACE(class_uri, '-test', '')
WHERE class_uri LIKE '%-test%';

UPDATE OSLOEnumeration
SET uri = REPLACE(uri, '-test', '')
WHERE uri LIKE '%-test%';

UPDATE OSLOEnumeration
SET codelist = REPLACE(codelist, '-test', '')
WHERE codelist LIKE '%-test%';

UPDATE OSLORelaties
SET uri = REPLACE(uri, '-test', '')
WHERE uri LIKE '%-test%';

UPDATE OSLORelaties
SET bron_uri = REPLACE(bron_uri, '-test', '')
WHERE bron_uri LIKE '%-test%';

UPDATE OSLORelaties
SET doel_uri = REPLACE(doel_uri, '-test', '')
WHERE doel_uri LIKE '%-test%';

UPDATE TypeLinkTabel
SET item_uri = REPLACE(item_uri, '-test', '')
WHERE item_uri LIKE '%-test%';
