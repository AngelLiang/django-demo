import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from .exceptions import EmailSyncError

# 第三方 SMTP 服务
mail_host = os.getenv('MAIL_HOST')
mail_user = os.getenv('MAIL_USER')
mail_pass = os.getenv('MAIL_PASS')

mail_sender = os.getenv('MAIL_SENDER')
mail_receiver = os.getenv('MAIL_RECEIVER')

# mail_from = os.getenv('MAIL_FROM')
# mail_to = os.getenv('MAIL_TO')
# mail_subject = os.getenv('MAIL_SUBJECT')


def send_email(from_, to, subject):
    # message = generate_email_message()
    message = MIMEText(subject, 'plain', 'utf-8')
    message['From'] = Header(from_, 'utf-8')
    message['To'] = Header(to, 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(mail_sender, mail_receiver, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
    except ConnectionRefusedError:
        raise EmailSyncError('服务器连接失败')
