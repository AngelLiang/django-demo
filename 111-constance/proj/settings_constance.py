from datetime import date
from .settings import INSTALLED_APPS

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

INSTALLED_APPS = [
    'constance',
    'constance.backends.database',
] + INSTALLED_APPS

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_ADDITIONAL_FIELDS = {
    'yes_no_null_select': ['django.forms.fields.ChoiceField', {
        'widget': 'django.forms.Select',
        'choices': ((None, "-----"), ("yes", "Yes"), ("no", "No"))
    }],
    'image_field': ['django.forms.ImageField', {}]
}

CONSTANCE_CONFIG = {
    'SITE_NAME': ('My Title', 'Website title'),
    'SITE_DESCRIPTION': ('', 'Website description'),
    'THEME': ('light-blue', 'Website theme'),
    'THE_ANSWER': (42, 'Answer to the Ultimate Question of Life, '
                   'The Universe, and Everything'),
    'DATE_ESTABLISHED': (date(2020, 1, 1), "the shop's first opening"),
    'MY_SELECT_KEY': ('yes', 'select yes or no', 'yes_no_null_select'),
    'LOGO_IMAGE': ('default.png', 'Company logo', 'image_field'),
}
