from django.urls import path, include
from .views import profile

urlpatterns = [
    path('profile/', profile),
]
