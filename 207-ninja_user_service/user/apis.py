from ninja import Router
from user.services import UserService
from user.schemas import UserOut

router = Router()


def make_response(data, code=0, message='success'):
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
    return make_response(data,code,message)


@router.get('/')
def list_user(request):
    records, total = UserService(request).get_list()
    return make_records_response(records, total)


@router.get('/{userId}')
def get_user_detail(request, userId: int):
    data = UserService(request).get_by_id(userId)
    return make_response(data=data)
