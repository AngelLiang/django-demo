from django.contrib import admin


class AppTokenAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    readonly_fields = ('key', 'user')
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'key',
                'user',
                'memo',
            )
        }),
    )

    # def get_changeform_initial_data(self, request):
    #     return {
    #         'user': request.user,
    #     }

    def save_model(self, request, obj, form, change):
        if not obj.pk and not hasattr(obj, 'user'):
            obj.user = request.user
        return super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.all()
        return qs.filter(user=request.user).all()
