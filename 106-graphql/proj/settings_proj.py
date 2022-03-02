from .settings import INSTALLED_APPS

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

INSTALLED_APPS = INSTALLED_APPS + [
    'graphene_django'
]

# GRAPHENE = {
#     'SCHEMA': 'user.graphql.schema' # Where your Graphene schema lives
# }
