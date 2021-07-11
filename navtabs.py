USER_NAVTABS = [
    {
        "name": "Name Me",
        "url": "/dog/memes/",  # It is recommended to get these URLs through Django Reverse
        # See https://docs.djangoproject.com/en/3.2/ref/urlresolvers/#reverse for more info
        "icon-right-class": "fas fa-filter",
        "icon-left-class": "fas fa-checkmark",
    },
]
ADMIN_NAVTABS = [
    {
        "name": "Name Me",
        "url": "/dog/memes/",
        "icon-right-class": "fas fa-filter",
        "icon-left-tag": "span",
        "icon-left-class": "fas fa-checkmark",
        "icon-left-text": "filter_alt",
    },
]
CUSTOM_NAVTABS = {
    "Group Name": [
        {
            "name": "Name Me",
            "url": "/dog/memes/",
            "icon-right-class": "fas fa-filter",
            "icon-left-class": "fas fa-checkmark",
            "auth-level": 1,
        },
    ],
}
SETTINGS_TABS = [
    ("tab_name", "<URL>"),
    ("tab_name_2", "<URL>"),
]
