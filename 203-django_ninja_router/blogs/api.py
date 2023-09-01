from ninja import Router
from .models import Event

router = Router()

@router.get('/')
def list_events(request):
    return {'code':0}
    # return [
    #     {"id": e.id, "title": e.title}
    #     for e in Event.objects.all()
    # ]

@router.get('/{event_id}')
def event_details(request, event_id: int):
    return {'code':0}

    # event = Event.objects.get(id=event_id)
    # return {"title": event.title, "details": event.details}
