from django.urls import path
from django.conf.urls import url
from rest_framework.authentication import SessionAuthentication

# from .permissions import IsSuperuser
from rest_framework.permissions import IsAuthenticated

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .urls import urlpatterns as patterns


schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        # description="Test description",
    ),
    public=True,
    # authentication_classes=(
    #     SessionAuthentication,
    # ),
    # permission_classes=(
    #     IsAuthenticated,
    # ),
    patterns=patterns,
)

urlpatterns = [
    # for drf_yasg
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='swagger-api-json'),
    url(r'^swagger/index.html$', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-api-ui'),
]
