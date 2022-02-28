from django.conf import settings

from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from django.contrib.auth import get_user_model
User = get_user_model()

from ..models.wechataccount import WeChatAccount
from ..models.wechatuserinfo import WeChatUserInfo
from ..core.wechatcrypt import WeChatCrypt
from ..serializers.wechataccount import WeChatAccountSerializer


class WeChatUpdateInfoAPIView(views.APIView):
    """更新用户信息"""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        params = request.data
        encryptedData = params.get('encryptedData', None)
        iv = params.get('iv', None)

        if not encryptedData:
            return Response({"encryptedData": "This field is reuqired"}, status=status.HTTP_400_BAD_REQUEST)

        if not iv:
            return Response({"iv": "This field is reuqired"}, status=status.HTTP_400_BAD_REQUEST)

        wechat_user = WeChatAccount.objects.filter(user=request.user).first()
        pc = WeChatCrypt(settings.WECHAT_MINIPROGRAM_CONFIG['APPID'], wechat_user.session_key)

        user = pc.decrypt(encryptedData, iv)
        if not wechat_user.userinfo:
            wechat_user.userinfo = WeChatUserInfo.objects.create()
            wechat_user.save()
        wechat_user.userinfo.nickName = user['nickName']
        wechat_user.userinfo.gender = user['gender']
        wechat_user.userinfo.language = user['language']
        wechat_user.userinfo.city = user['city']
        wechat_user.userinfo.avatarUrl = user['avatarUrl']
        wechat_user.userinfo.save()

        token = Token.objects.get(user=self.request.user)
        return Response({
            'token': token.key,
            'wechat': WeChatAccountSerializer(wechat_user).data
        }, status=status.HTTP_200_OK)
