from ninja import NinjaAPI
from ninja import Schema, Field


api = NinjaAPI()

class HelloIn(Schema):
    each_string:str = Field(alias='eachString')

class HelloOut(Schema):
    each_string:str = Field(alias='eachString')

    class Config:
        # 修改响应字段为驼峰需要标记这个
        allow_population_by_field_name = True 

@api.post("/hello", response=HelloOut, by_alias=True)  # 修改响应字段为驼峰需要标记 by_alias 为 True
def hello(request, hello:HelloIn):
    return {
        'each_string': hello.each_string
    }

