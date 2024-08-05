from typing import Tuple
from user.models import User
from user.models import UserToken
from user import schemas
from utils.strings import generate_random_string


class UserService:

    def add_user(self, openid: str) -> schemas.UserLoginOut:
        user = User.objects.create(
            openid=openid,
        )
        return schemas.UserLoginOut.from_orm(user)

    # def login(self, openid: str) -> schemas.UserLoginOut:
    #     user, _ = User.objects.get_or_create(openid=openid)
    #     token, _ = UserToken.objects.get_or_create(user=user)
    #     return schemas.UserLoginOut(token=token)

    def weixin_qrcode_login(self, openid: str) -> str:
        """微信扫码登录"""
        user, _ = User.objects.get_or_create(openid=openid)
        self.clean_user_all_token(user)
        token = UserToken.objects.create(user=user, key=generate_random_string(64))
        return token.key

    def validate_token(self, key: str) -> UserToken | None:
        return UserToken.objects.filter(key=key).first()

    def clean_user_all_token(self, user):
        UserToken.objects.filter(user=user).delete()
