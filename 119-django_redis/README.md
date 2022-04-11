# django redis

    pipenv install django-redis

## 访问缓存

    python manage.py shell

    >>> from django.core.cache import cache
    >>> cache.set('my_key', 'hello, world!', 30)
    >>> cache.get('my_key')
    'hello, world!'
    >>> cache.get('my_key', 'has expired')
