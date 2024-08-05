
def make_response(code=200, message='操作成功', data=None):
    return {
        'code': code,
        'message': message,
        'data': data
    }


def make_records_response(records, total, code=200, message='操作成功', current=None, size=None):
    data = {
        'records': records,
        'total': total,
        'current': current,
        'size': size,
    }
    return make_response(code, message, data=data)
