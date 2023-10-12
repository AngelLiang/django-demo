
def make_response(code=0, message='操作成功', data=None):
    return {
        'code': code,
        'message': message,
        'data': data
    }


def make_records_response(records, total, code=0, message='操作成功'):
    data = {
        'records': records,
        'total': total
    }
    return make_response(code, message, data=data)
