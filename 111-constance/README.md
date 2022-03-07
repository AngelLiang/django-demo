
## 快速使用 django-constance

    pipenv install django-constance[database]


```
# settings_constance.py
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

INSTALLED_APPS = (
    # other apps
    'constance.backends.database',
)
```

    python manage.py migrate database


https://django-constance.readthedocs.io/en/latest/backends.html#database
