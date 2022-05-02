from django.conf import settings
from django.utils import timezone
from import_export import widgets
from datetime import datetime


class DatetimeMultiFormatWidget(widgets.DateTimeWidget):

    def __init__(self, format=None):
        if format is None:
            if not settings.DATETIME_INPUT_FORMATS:
                formats = ("%Y-%m-%d %H:%M:%S",)
            else:
                formats = settings.DATETIME_INPUT_FORMATS
        elif isinstance(format, list) or isinstance(format, tuple):
            formats = format
        else:
            formats = (format,)
        self.formats = formats

    def clean(self, value, row=None, *args, **kwargs):
        if not value:
            return None
        if isinstance(value, datetime):
            if settings.USE_TZ:
                # make datetime timezone aware so we don't compare
                # naive datetime to an aware one
                value = timezone.make_aware(value, timezone.get_default_timezone())
            return value
        for format in self.formats:
            try:
                dt = datetime.strptime(value, format)
                if settings.USE_TZ:
                    # make datetime timezone aware so we don't compare
                    # naive datetime to an aware one
                    dt = timezone.make_aware(dt,
                                             timezone.get_default_timezone())
                return dt
            except (ValueError, TypeError):
                continue
        raise ValueError("Enter a valid date/time.")

    def render(self, value, obj=None):
        if not value:
            return ""
        if settings.USE_TZ:
            print(value)
            value = timezone.localtime(value)
        return value.strftime(self.formats[0])
