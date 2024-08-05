from ninja import NinjaAPI
from ninja import Router

router = Router(tags=['用户认证'])

from user.apis import *  # noqa
