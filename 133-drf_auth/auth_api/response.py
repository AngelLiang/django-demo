from rest_framework.response import Response


def success_response(request, msg='操作成功', data=None):
    return Response({
        'code': 0,
        'msg': msg,
        'data': data
    })


def failure_response(request, msg='操作失败',  data=None):
    return Response({
        'code': 1,
        'msg': msg,
        'data': data
    })
