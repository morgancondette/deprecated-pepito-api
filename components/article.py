schema = {
    'title': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 255
    },
    'slug': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 255,
        'unique': True
    },
    'cover': {
        'type': 'string',
        'minlength': 1
    },
    'featured': {
        'type': 'boolean'
    },
    'visible': {
        'type': 'boolean'
    },
    'content': {
        'type': 'dict',
        'schema': {
            'markdown': {'type': 'string'},
            'html': {'type': 'string'}
        },
    },
    'tags': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'tag',
            'embeddable': True
        },
    }
}

article = {
    'item_title': 'article',

    # GET requests at '/article/<slug>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'slug'
    },

    'schema': schema
}