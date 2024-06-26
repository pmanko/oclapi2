MAPPING_TYPE = 'Mapping'
SAME_AS = 'SAME-AS'

MAPPING_WAS_RETIRED = 'Mapping was retired'
MAPPING_WAS_UNRETIRED = 'Mapping was un-retired'
MAPPING_IS_ALREADY_RETIRED = 'Mapping is already retired'
MAPPING_IS_ALREADY_NOT_RETIRED = 'Mapping is already not retired'
PERSIST_CLONE_ERROR = 'An error occurred while saving new concept version.'
PARENT_VERSION_NOT_LATEST_CANNOT_UPDATE_MAPPING = 'Parent version is not the latest. Cannot update mapping.'
PERSIST_CLONE_SPECIFY_USER_ERROR = "Must specify which user is attempting to create a new mapping version."
OPENMRS_SINGLE_MAPPING_BETWEEN_TWO_CONCEPTS = 'There can be only one mapping between two concepts'
OPENMRS_INVALID_MAPTYPE = 'Invalid mapping type'
OPENMRS_EXTERNAL_ID_LENGTH = 36
OPENMRS_MAPPING_EXTERNAL_ID_ERROR = f'Mapping External ID cannot be more than {OPENMRS_EXTERNAL_ID_LENGTH} characters.'
MUST_SPECIFY_FROM_CONCEPT = "Must specify a 'from_concept'."
MUST_SPECIFY_TO_CONCEPT_OR_TO_SOURCE = "Must specify either 'to_concept_url' or 'to_source_url' & 'to_concept_code'."
TO_SOURCE_UNIQUE_ATTRIBUTES_ERROR_MESSAGE = "Parent, map_type, from_concept, to_source, to_concept_code must be unique."
ALREADY_EXISTS = "Mapping ID must be unique within a source."
