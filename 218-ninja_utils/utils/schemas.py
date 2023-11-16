from typing import List
from pydantic import create_model
from ninja import Schema


class ResponseOut(Schema):
    code: int
    message: str
    data: dict


def make_response_schema(class_name: str, data_schema):
    response_schema_fields = {
        'code': (int, 0),
        'message': (str, 'success'),
        'data': (data_schema, None)
    }
    response_schema = create_model(
        class_name,
        __config__=None,
        __base__=Schema,
        __module__=Schema.__module__,
        __validators__={},
        **response_schema_fields
    )
    return response_schema


def make_records_response_schema(class_name: str, model_schema):
    """
    创建一个如下的类

    from ninja import Schema

    class UserListOut(Schema):
        class Data(Schema):
            records: List[UserSchema]
            total: int
            current: int
            size: int

        code :int = 0
        message: str = 'success'
        data: Data

    """

    data_schema_fields = {
        'records': (List[model_schema], None),
        'total': (int, None),
        'current': (int, None),
        'size': (int, None),
    }
    data_schema = create_model(
        'Data',
        __config__=None,
        __base__=Schema,
        __module__=Schema.__module__,
        __validators__={},
        **data_schema_fields,
    )  # type: ignore

    # response_schema_fields = {
    #     'code': (int, 0),
    #     'message': (str, 'success'),
    #     'data': (data_schema, None)
    # }
    # response_schema = create_model(
    #     class_name,
    #     __config__=None,
    #     __base__=Schema,
    #     __module__=Schema.__module__,
    #     __validators__={},
    #     **response_schema_fields
    # )
    response_schema = make_response_schema(class_name, data_schema)

    return response_schema
