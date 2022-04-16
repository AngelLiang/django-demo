from django.contrib import admin
from river.models import TransitionApprovalMeta
from river.models import TransitionMeta


class TransitionMetaInline(admin.TabularInline):
    extra = 0
    model = TransitionMeta
    fields = ('__str__', 'source_state', 'destination_state',)
    readonly_fields = ('__str__',)

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj):
        return False


class TransitionApprovalMetaInline(admin.TabularInline):
    extra = 0
    model = TransitionApprovalMeta
    fields = ('__str__', 'permissions', 'parents', 'priority',)
    readonly_fields = ('__str__',)

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj):
        return False
