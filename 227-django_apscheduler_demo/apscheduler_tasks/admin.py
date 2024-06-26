from django.contrib import admin
from django_apscheduler import util
from django.utils.safestring import mark_safe
from django.utils import timezone
from django.conf import settings
import pytz

from django_apscheduler.models import DjangoJob, DjangoJobExecution
from django_apscheduler.admin import DjangoJobAdmin as _DjangoJobAdmin, DjangoJobExecutionAdmin as _DjangoJobExecutionAdmin

admin.site.unregister(DjangoJob)
admin.site.unregister(DjangoJobExecution)


@admin.register(DjangoJob)
class DjangoJobAdmin(_DjangoJobAdmin):
    search_fields = ["id"]
    list_display = ["id", "local_run_time", "average_duration"]

    def average_duration(self, obj):
        try:
            return self.avg_duration_qs.get(job_id=obj.id)[1]
        except DjangoJobExecution.DoesNotExist:
            return "None"

    def local_run_time(self, obj):
        dt = obj.next_run_time
        if dt and settings.USE_TZ and timezone.is_aware(dt):
            dt = timezone.localtime(dt)
        return dt or "(paused)"

    average_duration.short_description = "平均运行用时（秒）"
    local_run_time.short_description = '下一次运行时间'


@admin.register(DjangoJobExecution)
class DjangoJobExecutionAdmin(_DjangoJobExecutionAdmin):
    list_display = ["id", "job", "html_status", "local_run_time", "duration_text"]
    list_filter = ["job__id", "run_time", "status"]

    def html_status(self, obj):
        return mark_safe(
            f'<p style="color: {self.status_color_mapping[obj.status]}">{obj.status}</p>'
        )

    def local_run_time(self, obj):
        dt = obj.run_time
        if dt and settings.USE_TZ and timezone.is_aware(dt):
            dt = timezone.localtime(dt)
        return dt

    def duration_text(self, obj):
        return obj.duration or "N/A"

    html_status.short_description = '状态'
    duration_text.short_description = '执行时间（秒）'
    local_run_time.short_description = '运行时间'
