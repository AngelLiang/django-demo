from ninja import Router
from .models import News

router = Router()

@router.get('/')
def list_news(request):
    return {'code':0}

@router.get('/{news_id}')
def news_details(request, news_id: int):
    return {'code':0}
