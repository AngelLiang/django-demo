from django.contrib.auth import login, logout, authenticate

from django.http import Http404
from django.contrib.auth import get_user_model
User = get_user_model()


class LoginService:

    def login(self, request, username, password) -> str:
        user:User = User.objects.filter(username=username).first()
        if not user:
            raise Http404()
        if  not user.is_active:
            raise Http404()
        if user.check_password(password):
            # login(request, user)
            return 'token'

    def logout(self, request):
        pass
        # logout(request)
