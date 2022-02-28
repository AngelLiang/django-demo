from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from apptoken.authentication import AppTokenAuthentication


class AppTokenPingAPIView(APIView):
    authentication_classes = [
        AppTokenAuthentication,
    ]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        return Response({
            'code': 2000,
            'user': str(request.user),
        })
