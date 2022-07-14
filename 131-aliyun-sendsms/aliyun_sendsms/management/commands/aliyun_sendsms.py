
from django.core.management.base import BaseCommand
from django.core import management

from ...sendsms import AliyunSendSms


class Command(BaseCommand):
    help = '发送阿里云短信'

    def add_arguments(self, parser):
        parser.add_argument('phone', type=str, help='要发送验证码的手机号')

    def handle(self, *args, **options):
        phone = options['phone']
        aliyun_send_sms = AliyunSendSms()
        code = aliyun_send_sms.gen_code()
        aliyun_send_sms.sendmsg_code(phone, code)
