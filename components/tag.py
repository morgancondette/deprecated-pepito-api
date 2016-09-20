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
    'description': {
        'type': 'string'
    },
    'featured': {
        'type': 'boolean'
    },
    'visible': {
        'type': 'boolean'
    },
    'parent': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'tag',
            'embeddable': True
        },
    },
    'articles': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'article',
            'embeddable': True
        },
    }
}

tag = {
    'item_title': 'tag',

    # GET requests at '/tag/<slug>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'slug'
    },

    'schema': schema
}