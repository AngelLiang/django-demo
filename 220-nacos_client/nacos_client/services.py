import threading
from time import sleep
from django.conf import settings

import nacos

from nacos_client.logger import logger

NACOS_ENABLE = getattr(settings, 'NACOS_ENABLE')
NACOS_SERVER_ADDRESSES = getattr(settings, 'NACOS_SERVER_ADDRESSES', '192.168.42.1:8848')
NACOS_SERVER_NAME = getattr(settings, 'NACOS_SERVER_NAME', 'mox-weixin')
NACOS_NAMESPACE = getattr(settings, 'NACOS_NAMESPACE', 'dev')
NACOS_CLIENT_HOST = getattr(settings, 'NACOS_CLIENT_HOST', '192.168.42.8')
NACOS_CLIENT_PORT = getattr(settings, 'NACOS_CLIENT_PORT', 7606)
NACOS_DATA_ID = getattr(settings, 'NACOS_DATA_ID', 'mox-weixin-dev.yml')
NACOS_GROUP = getattr(settings, 'NACOS_GROUP', 'DEFAULT_GROUP')


def init_nacos_client():
    client = nacos.NacosClient(NACOS_SERVER_ADDRESSES, namespace=NACOS_NAMESPACE)

    # get config
    data_id = NACOS_DATA_ID
    group = NACOS_GROUP
    content = client.get_config(data_id, group)
    # logger.debug(content)

    logger.info('===nacos===')
    logger.info(f'server:{NACOS_SERVER_ADDRESSES}')
    logger.info(f'namespace:{NACOS_NAMESPACE}')
    logger.info(f'server name:{NACOS_SERVER_NAME}')
    logger.info(f'host:{NACOS_CLIENT_HOST}')
    logger.info(f'port:{NACOS_CLIENT_PORT}')
    result = client.add_naming_instance(NACOS_SERVER_NAME, NACOS_CLIENT_HOST, NACOS_CLIENT_PORT)
    if result:
        logger.info('nacos 连接成功')
    else:
        logger.info('nacos 连接失败')
    logger.info('===nacos===')
    return client


class NacosClientThread(threading.Thread):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.is_connected = False
        self.client = None

    def run(self) -> None:
        while True:
            if not self.is_connected:
                try:
                    self.client = init_nacos_client()
                except nacos.exception.NacosRequestException as e:
                    logger.error(e)
                else:
                    self.is_connected = True
            else:
                try:
                    # 发送心跳
                    self.client.send_heartbeat(NACOS_SERVER_NAME, NACOS_CLIENT_HOST, NACOS_CLIENT_PORT)
                except nacos.exception.NacosRequestException as e:
                    logger.error(e)
                    self.is_connected = False
            sleep(5)
