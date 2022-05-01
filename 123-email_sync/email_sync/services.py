from django.utils import timezone
from .models import EmailSyncLog


def emailsynclog_add_upload_log(*, operater, is_success, md5=''):
    model = EmailSyncLog(
        operate_at=timezone.now(),
        operate_type=EmailSyncLog.UPLOAD,
        operater=operater,
        is_success=is_success,
        md5=md5,
    )

    # model.full_clean()
    model.save()
    return model


def emailsynclog_add_download_log(*, operater, is_success, md5=''):
    model = EmailSyncLog(
        operate_at=timezone.now(),
        operate_type=EmailSyncLog.DOWNLOAD,
        operater=operater,
        is_success=is_success,
        md5=md5,
    )

    # model.full_clean()
    model.save()
    return model
