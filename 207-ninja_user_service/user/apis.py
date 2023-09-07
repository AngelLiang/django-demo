from urllib import response
from ninja import Router
from user.services import UserService
from user.schemas import UserOut

router = Router()

def make_records_response(records, total, code=0, message='success'):
    return {
        'code': code,
        'message':message,
        'data': {
            'records': records,
            'total': total
        }
    }

@router.get('/')
def list_user(request):
    records, total = UserService(request).get_list()
    return make_records_response(records, total)


@router.get('/{userId}', response=UserOut)
def get_user_detail(request, userId: int):
    return UserService(request).get_by_id(userId)
