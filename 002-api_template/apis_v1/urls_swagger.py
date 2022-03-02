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
    public=False,
    authentication_classes=(
        SessionAuthentication,
    ),
    permission_classes=(
        IsAuthenticated,
    ),
    patterns=patterns,
)

urlpatterns = [
    # for drf_yasg
    url(r'^apis/v1/_swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='apisv1-json'),
    url(r'^apis/v1/_swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='apisv1-swagger-ui'),
]
