import json

from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from pydash import get

from core.common.utils import jsonify_safe, flatten_dict, format_url_for_search
from core.sources.models import Source


@registry.register_document
class SourceDocument(Document):
    class Index:
        name = 'sources'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    locale = fields.ListField(fields.KeywordField())
    last_update = fields.DateField(attr='updated_at')
    updated_by = fields.KeywordField(attr='updated_by.username')
    owner = fields.KeywordField(attr='parent_resource', normalizer='lowercase')
    owner_type = fields.KeywordField(attr='parent_resource_type')
    public_can_view = fields.TextField(attr='public_can_view')
    source_type = fields.KeywordField(attr='source_type', normalizer='lowercase')
    version = fields.KeywordField(attr='version')
    name = fields.TextField(attr='name')
    _name = fields.KeywordField(attr='name', normalizer='lowercase')
    canonical_url = fields.TextField(attr='canonical_url')
    _canonical_url = fields.TextField()
    mnemonic = fields.TextField(attr='mnemonic')
    _mnemonic = fields.KeywordField(attr='mnemonic', normalizer='lowercase')
    extras = fields.ObjectField(dynamic=True)
    identifier = fields.ObjectField()
    jurisdiction = fields.ObjectField()
    publisher = fields.KeywordField(attr='publisher', normalizer='lowercase')
    content_type = fields.KeywordField(attr='content_type', normalizer='lowercase')
    custom_validation_schema = fields.KeywordField(attr='custom_validation_schema', normalizer='lowercase')
    hierarchy_meaning = fields.KeywordField()
    created_by = fields.KeywordField()
    property_codes = fields.ListField(fields.KeywordField())
    filter_codes = fields.ListField(fields.KeywordField())

    class Django:
        model = Source
        fields = [
            'full_name',
            'revision_date',
            'retired',
            'experimental',
            'case_sensitive',
            'compositional',
            'version_needed',
            'external_id',
        ]

    @staticmethod
    def get_match_phrase_attrs():
        return ['name', 'external_id', 'canonical_url', 'full_name']

    @staticmethod
    def get_exact_match_attrs():
        return {
            'mnemonic': {
                'boost': 4,
            },
            'name': {
                'boost': 3.5,
            },
            'full_name': {
                'boost': 3.2,
            },
            'canonical_url': {
                'boost': 3,
            },
            'external_id': {
                'boost': 2.5
            }
        }

    @staticmethod
    def get_wildcard_search_attrs():
        return {
            'mnemonic': {
                'boost': 1,
                'lower': True,
                'wildcard': True
            },
            'name': {
                'boost': 0.8,
                'lower': True,
                'wildcard': True
            },
            'full_name': {
                'boost': 0.6,
                'lower': True,
                'wildcard': True
            },
            'canonical_url': {
                'boost': 0.6,
                'lower': True,
                'wildcard': True
            }
        }

    @staticmethod
    def get_fuzzy_search_attrs():
        return {
            'name': {
                'boost': 0.8,
                'lower': True,
                'wildcard': True
            },
            'full_name': {
                'boost': 0.2,
                'lower': True,
                'wildcard': True
            },
        }

    @staticmethod
    def prepare_locale(instance):
        return get(instance.supported_locales, [])

    @staticmethod
    def prepare_property_codes(instance):
        return [prop.get('code') for prop in get(instance.properties, [])]

    @staticmethod
    def prepare_filter_codes(instance):
        return [prop.get('code') for prop in get(instance.filters, [])]

    @staticmethod
    def prepare_extras(instance):
        value = {}

        if instance.extras:
            value = jsonify_safe(instance.extras)
            if isinstance(value, dict):
                value = flatten_dict(value)

        if value:
            value = json.loads(json.dumps(value))
        return value or {}

    @staticmethod
    def prepare_identifier(instance):
        value = {}

        if instance.identifier:
            value = jsonify_safe(instance.identifier)
            if isinstance(value, dict):
                value = flatten_dict(value)
            if isinstance(value, str):
                value = {'value': value}

        return value or {}

    @staticmethod
    def prepare_jurisdiction(instance):
        value = {}
        if instance.jurisdiction:
            value = jsonify_safe(instance.jurisdiction)
            if isinstance(value, dict):
                value = flatten_dict(value)
            if isinstance(value, str):
                value = {'value': value}

        return value or {}

    @staticmethod
    def prepare_created_by(instance):
        return instance.created_by.username

    @staticmethod
    def prepare_hierarchy_meaning(instance):
        hierarchy_meaning = instance.hierarchy_meaning
        if hierarchy_meaning:
            return hierarchy_meaning.lower()
        return 'None'

    @staticmethod
    def prepare__canonical_url(instance):
        return format_url_for_search(instance.canonical_url)
