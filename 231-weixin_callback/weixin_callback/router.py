from ninja import Router

router = Router(tags=['微信相关'])

from weixin_callback.apis import *  # noqa
