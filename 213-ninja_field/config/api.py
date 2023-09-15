from ninja import NinjaAPI
from ninja import Schema, Field


api = NinjaAPI()

class HelloIn(Schema):
    each_string:str = Field(alias='eachString')

class HelloOut(Schema):
    eachString:str = Field(alias='each_string')


@api.post("/hello", response=HelloOut)
def hello(request, hello:HelloIn):
    return {
        'each_string': hello.each_string
    }

