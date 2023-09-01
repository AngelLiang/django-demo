from ninja import Router
# from .models import Event

router = Router()


@router.get('/')
def list_events(request):
    return {"code": 0}


@router.get('/{event_id}')
def event_details(request, event_id: int):
    # event = Event.objects.get(id=event_id)
    return {"code": 0}
