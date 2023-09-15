from ninja import Router
from user.services import UserService
from user.schemas import UserOut, UserListResponseOut, UserDetailResponseOut, UserUpdateIn
from user.schemas import UserAddIn

router = Router()


def make_response(data=None, code=0, message='success'):
    return {
        'code': code,
        'message':message,
        'data': data
    }

def make_records_response(records, total, code=0, message='success'):
    data={
        'records': records,
        'total': total
    }
    return make_response(data, code, message)


@router.get('/', response=UserListResponseOut, by_alias=True)
def list_user(request):
    records, total = UserService(request).get_list_and_total()
    print(records)
    return make_records_response(records, total)


@router.get('/{userId}', response=UserDetailResponseOut, by_alias=True)
def get_user_detail(request, userId: int):
    data = UserService(request).get_by_id(userId)
    return make_response(data=data)


@router.post('/')
def add_user(request, data: UserAddIn):
    UserService(request).add_user(data)
    return make_response()


@router.put('/{userId}',)
def update_user(request, userId: int, data: UserUpdateIn):
    UserService(request).update_by_id(userId, data)
    return make_response()
