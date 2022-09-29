from django.urls import path, include
from .apis.testapp import testapp_urls


urlpatterns = [
    path('api/', include(testapp_urls))
    # path('api/v1/testapp/testapp', testapp_list,
    # path('api/v1/testapp/testapp/<int:pk>', testapp_detail,
]
