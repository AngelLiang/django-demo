from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model
User = get_user_model()

from .utils import (
    file_generate_upload_path
)
from .enums import FileUploadStorage


class File(models.Model):
    file = models.FileField(
        _('文件'),
        upload_to=file_generate_upload_path,
        blank=True,
        null=True
    )

    original_file_name = models.TextField(_('原文件名'))

    file_name = models.CharField(_('文件名称'), max_length=255, unique=True)
    file_type = models.CharField(_('文件类型'), max_length=255)

    # As a specific behavior,
    # We might want to preserve files after the uploader has been deleted.
    # In case you want to delete the files too, use models.CASCADE & drop the null=True
    uploaded_by = models.ForeignKey(
        User,
        verbose_name=_('上传者'),
        null=True,
        on_delete=models.SET_NULL,
        db_constraint=False,
    )

    upload_finished_at = models.DateTimeField(verbose_name=_('上传时间'), blank=True, null=True)

    created_at = models.DateTimeField(_('创建时间'), db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(_('更新时间'), auto_now=True)

    def __str__(self):
        return self.file_name

    @property
    def is_valid(self):
        """
        We consider a file "valid" if the the datetime flag has value.
        """
        return bool(self.upload_finished_at)
    # is_valid.short_description = _('是否有效')

    # @property
    # def url(self):
    #     if settings.FILE_UPLOAD_STORAGE == FileUploadStorage.S3:
    #         return self.file.url

    #     return f"{settings.APP_DOMAIN}{self.file.url}"
