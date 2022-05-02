def get_admin_by_modelclass(model):
    from django.contrib import admin
    return admin.site._registry.get(model)
