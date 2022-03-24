from django.contrib import admin
from django.utils import timezone

from . import models
from .forms import OrderForm


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_no', 'title', 'creator')
    readonly_fields = ('order_no', 'creator')
    fieldsets = (
        (None, {
            'fields': [
                'order_no',
                'order_date',
                'title',
                'content',
                'creator',
            ]}),
    )

    form = OrderForm

    def get_changeform_initial_data(self, request):
        return {
            'order_date': timezone.now().date,
            'title': '请填写标题',
            'content': '请填写内容',
            'creator': request.user,
        }

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(models.Order, OrderAdmin)
