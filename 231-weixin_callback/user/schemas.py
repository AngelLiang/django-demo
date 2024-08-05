from pydantic import BaseModel, Field


class UserLoginIn(BaseModel):
    openid: str


class UserLoginOut(BaseModel):
    token: str
