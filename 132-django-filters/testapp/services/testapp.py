from ..models import Testapp


def testapp_create(*args, **kwargs) -> Testapp:
    obj = Testapp(*args, **kwargs)

    obj.full_clean()
    obj.save()

    return obj
