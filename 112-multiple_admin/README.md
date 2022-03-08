# django 使用多个站点

在 URL 上面添加多个 admin 的 URL 即可。

    # urls.py
    from django.urls import path
    from myproject.admin import advanced_site, basic_site

    urlpatterns = [
        path('basic-admin/', basic_site.urls),
        path('advanced-admin/', advanced_site.urls),
    ]

---

ref: https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#multiple-admin-sites-in-the-same-urlconf
