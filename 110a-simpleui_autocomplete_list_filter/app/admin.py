from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from admin_auto_filters.filters import AutocompleteFilterFactory
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_dispaly = ('title', 'creator', 'is_public')

    list_filter = (
        AutocompleteFilterFactory(_('按创建者过滤'), 'creator', 'admin:auth_user_autocomplete_light', True),
        'is_public',
        'created_at',
    )

admin.site.register(Post, PostAdmin)
