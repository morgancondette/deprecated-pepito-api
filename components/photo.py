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
    'visible': {
        'type': 'boolean'
    },
    'exifs': {
        'type': 'dict',
        'schema': {
            'filename': {'type': 'string'},
            'location': {'type': 'string'},
            'width': {'type': 'integer'},
            'height': {'type': 'integer'},
            'iso': {'type': 'integer'},
            'focallength': {'type': 'integer'},
            'speed': {'type': 'string'},
            'aperture': {'type': 'float'},
            'camera': {'type': 'string'},
            'lens': {'type': 'string'},
            'taken': {'type': 'datetime'}
        }
    },
    'collections': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'collection',
            'embeddable': True
        },
    }

}

photo = {
    'item_title': 'photo',

    # GET requests at '/photo/<slug>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'slug'
    },

    'schema': schema
}