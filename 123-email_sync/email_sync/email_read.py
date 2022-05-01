import os
import poplib
from email.header import decode_header
from email.parser import Parser
from email.utils import parseaddr
from typing import Dict
from .exceptions import EmailSyncError
import pprint

email = os.getenv('MAIL_USER')
password = os.getenv('MAIL_PASS')
pop3_server = os.getenv('MAIL_POP')

mail_id = os.getenv('MAIL_ID', 'mail_id')
from_ = os.getenv('MAIL_FROM', 'from')
to = os.getenv('MAIL_TO', 'to')


def decode_str(s):
    """
    解析消息头中的字符串
    没有这个函数，print出来的会使乱码的头部信息。如'=?gb18030?B?yrXWpL3hufsueGxz?='这种
    通过decode，将其变为中文
    """
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def guess_charset(msg):
    """
    获取邮件的字符编码
    首先在message中寻找编码，如果没有，就在header的Content-Type中寻找
    """
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos+8:].strip()
    return charset


def get_header(msg) -> Dict:
    """
    #解码邮件信息分为两个步骤，第一个是取出头部信息
    #首先取头部信息
    #主要取出['From','To','Subject']
    '''
    From: "=?gb18030?B?anVzdHpjYw==?=" <justonezcc@sina.com>
    To: "=?gb18030?B?ztLX1Ly6tcTTys/k?=" <392361639@qq.com>
    Subject: =?gb18030?B?dGV4dMTjusM=?=
    '''
    #如上述样式，均需要解码
    """
    result = {}
    for header in ['From', 'To', 'Subject']:
        value = msg.get(header, '')
        if value:
            # 文章的标题有专门的处理方法
            if header == 'Subject':
                value = decode_str(value)
                result['subject'] = value
            elif header in ['From', 'To']:
                # 地址也有专门的处理方法
                hdr, addr = parseaddr(value)
                name = decode_str(addr)
                value = name
                if header == 'From':
                    result['from'] = value
                if header == 'To':
                    result['to'] = value
    return result


def get_file(msg):
    file_list = []
    for part in msg.walk():
        filename = part.get_filename()
        if filename is None:
            continue
        filename = decode_str(filename)  # 获取的文件是乱码名称，通过一开始定义的函数解码
        data = part.get_payload(decode=True)  # 取出文件正文内容
        file_list.append(data)
    return file_list
    # 此处可以自己定义文件保存位置
    path = filename
    with open(path, 'wb') as f:
        f.write(data)
        f.close()
        print(f'download:{filename}')


def get_content(msg):
    for part in msg.walk():
        content_type = part.get_content_type()
        charset = guess_charset(part)
        # 如果有附件，则直接跳过
        if part.get_filename() != None:
            continue
        email_content_type = ''
        content = ''
        if content_type == 'text/plain':
            email_content_type = 'text'
        elif content_type == 'text/html':
            print('html 格式 跳过')
            continue  # 不要html格式的邮件
            email_content_type = 'html'

        if charset:
            try:
                content = part.get_payload(decode=True).decode(charset)
            except AttributeError:
                print('type error')
            except LookupError:
                print("unknown encoding: utf-8")
        if email_content_type == '':
            continue
            # 如果内容为空，也跳过
        print(email_content_type + ' -----  ' + content)


def read_email():
    try:
        server = poplib.POP3(pop3_server)
    except ConnectionRefusedError:
        raise EmailSyncError('服务器连接失败')

    # server.set_debuglevel(1)
    server.user(email)
    server.pass_(password)
    print((pop3_server, email, password))
    count, size = server.stat()
    print((count, size))

    # list()返回所有邮件的编号:
    # resp, mails, octets = server.list()
    # 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
    # mail_length = len(mails)
    # if mail_length == 0:
    #     raise EmailSyncError('没有数据可以下载')

    try:
        resp, mails, octets = server.retr(1)
    except poplib.error_proto as e:
        print(e)
        server.quit()
        raise EmailSyncError('没有数据可以下载')
    # print((resp, mails, octets))
    pprint.pprint(mails)
    # 获取最新一封邮件, 注意索引号从1开始:
    mail_length = len(mails)
    print(mail_length)
    msg_content = b'\r\n'.join(mails).decode('utf-8', 'ignore')
    msg = Parser().parsestr(msg_content)
    header = get_header(msg)
    print(header)

    if header['to'] == mail_id:
        print(mail_id)
        file_list = get_file(msg)
    else:

        try:
            server.dele(1)  # 删除邮件
        except poplib.error_proto as e:
            print(f'删除邮件失败:{e}')
        else:
            print('删除邮件')

        server.quit()
        raise EmailSyncError('下载数据错误，不是该系统下载数据')

    try:
        server.dele(1)  # 删除邮件
    except poplib.error_proto as e:
        print(f'删除邮件失败:{e}')
    else:
        print('删除邮件')

    server.quit()


if __name__ == '__main__':
    read_email()
