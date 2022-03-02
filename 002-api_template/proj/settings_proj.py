from .settings import INSTALLED_APPS

INSTALLED_APPS = INSTALLED_APPS + [
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',

    'apis_v1.apps.ApisV1Config',
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Token': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}
