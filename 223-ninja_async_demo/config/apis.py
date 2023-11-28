import time
import asyncio
from django.contrib.auth import get_user_model

from ninja import NinjaAPI

User = get_user_model()


api = NinjaAPI()


@api.get("/say-after")
def say_after(request, delay: int, word: str):
    time.sleep(delay)
    return {"saying": word}


@api.get("/say-after/async")
async def say_after_async(request, delay: int, word: str):
    await asyncio.sleep(delay)
    return {"saying": word}


@api.get("/get-user-list/async")
async def get_user_list_async(request):
    user_list = []
    async for user in User.objects.all():
        user_list.append(user)
    return {"data": [{"id": user.id, "username": user.username} for user in user_list]}


@api.get("/get-user/async/{id}")
async def get_user_async(request, id):
    user = await User.objects.filter(id=id).afirst()
    return {"data": {"id": user.id, "username": user.username}}
