from rest_framework.authentication import TokenAuthentication


class AppTokenAuthentication(TokenAuthentication):
    """
        Authorization: AppToken 401f7ac837da42b97f613d789819ff93537bee6a
    """
    # model = AppToken
    keyword = 'AppToken'

    def get_model(self):
        from apptoken.models import AppToken
        return AppToken

    def authenticate_credentials(self, key):
        return super().authenticate_credentials(key)
