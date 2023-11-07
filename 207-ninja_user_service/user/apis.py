from typing import List
from ninja import Router
from user.services import UserService
from user.schemas import UserOut, UserListResponseOut, UserDetailResponseOut, UserUpdateIn
from user.schemas import UserAddIn, UserBatchAddIn

router = Router()


def make_response(data=None, code=0, message='success'):
    return {
        'code': code,
        'message': message,
        'data': data
    }


def make_records_response(records, total, code=0, message='success'):
    data = {
        'records': records,
        'total': total
    }
    return make_response(data, code, message)


@router.get('/', response=UserListResponseOut, by_alias=True)
def list_user(request):
    records, total = UserService(request).get_list_and_total()
    return make_records_response(records, total)


@router.get('/{userId}', response=UserDetailResponseOut, by_alias=True)
def get_user_detail(request, userId: int):
    data = UserService(request).get_by_id(userId)
    return make_response(data=data)


@router.post('/')
def add_user(request, payload: UserAddIn):
    UserService(request).add_user(payload)
    return make_response()


@router.post('/batch/add')
def batch_add_user(request, payload: List[UserBatchAddIn]):
    UserService(request).batch_add_user(payload)
    return make_response()


@router.put('/{userId}')
def update_user(request, userId: int, payload: UserUpdateIn):
    UserService(request).update_by_id(userId, payload)
    return make_response()
