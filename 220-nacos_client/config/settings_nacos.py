import os


def str2bool(s):
    """
    如果 s 为 '0', 'n', 'no', 'false' ，返回 False
    其他情况返回 True
    """
    if isinstance(s, bool):
        return s
    return s.lower() not in ('0', 'n', 'no', 'false')


NACOS_ENABLE = str2bool(os.getenv('NACOS_ENABLE', True))
NACOS_SERVER_ADDRESSES = os.getenv('NACOS_SERVER_ADDRESSES')
NACOS_SERVER_NAME = os.getenv('NACOS_SERVER_NAME')
NACOS_NAMESPACE = os.getenv('NACOS_SERVER_ADDRESSES', 'dev')
NACOS_CLIENT_HOST = os.getenv('NACOS_SERVER_ADDRESSES')
NACOS_CLIENT_PORT = int(os.getenv('NACOS_CLIENT_PORT', 8848))
NACOS_DATA_ID = os.getenv('NACOS_DATA_ID')
NACOS_GROUP = os.getenv('NACOS_GROUP')
