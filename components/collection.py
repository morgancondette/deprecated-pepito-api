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
            'resource': 'collection',
            'embeddable': True
        },
    },
    'photos': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'photo',
            'embeddable': True
        },
    }
}

collection = {
    'item_title': 'collection',

    # GET requests at '/collection/<slug>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'slug'
    },

    'schema': schema
}