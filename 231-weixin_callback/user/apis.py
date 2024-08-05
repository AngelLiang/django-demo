from user.router import router
from utils.response import make_response
from user.services import UserService
from user.schemas import UserLoginIn, UserLoginOut


# @router.post('/login')
# def user_login(request, payload: UserLoginIn):
#     data = UserService().login(payload.openid)
#     return make_response(data=data)
