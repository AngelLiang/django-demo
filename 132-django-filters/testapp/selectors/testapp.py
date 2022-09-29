from typing import Iterable

from ..models import Testapp


def testapp_list(*args, *kwargs) -> Iterable[Testapp]:
    return Testapp.objects.filter(*args, *kwargs)
