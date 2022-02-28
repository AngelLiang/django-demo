from .settings import INSTALLED_APPS

INSTALLED_APPS = INSTALLED_APPS + [
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',

    'apptoken.apps.ApptokenConfig',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',  # add this
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',  # add this
        'apptoken.authentication.AppTokenAuthentication',  # add this
    ],
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        # 'Basic': {
        #     'type': 'basic'
        # },
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
}
