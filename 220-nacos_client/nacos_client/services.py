import threading
from time import sleep
from django.conf import settings

import nacos

from nacos_client.logger import logger

NACOS_CONFIG = getattr(settings, 'NACOS_CONFIG')


def init_nacos_client(address, namespace, data_id, group, server_name, client_host, client_port):
    logger.info(f'address:{address}')
    logger.info(f'namespace:{namespace}')
    logger.info(f'server name:{server_name}')
    logger.info(f'client_host:{client_host}')
    logger.info(f'client_port:{client_port}')

    client = nacos.NacosClient(address, namespace=namespace)
    content = client.get_config(data_id, group)
    # logger.info(content)
    result = client.add_naming_instance(server_name, client_host, client_port)
    if result:
        logger.info('nacos 连接成功')
    else:
        logger.info('nacos 连接失败')
    return client


class NacosClientThread(threading.Thread):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.is_connected = False
        self.client = None

    def run(self) -> None:
        address = NACOS_CONFIG['NACOS_SERVER_ADDRESSES']
        server_name = NACOS_CONFIG['NACOS_SERVER_NAME']
        namespace = NACOS_CONFIG['NACOS_NAMESPACE']

        client_host = NACOS_CONFIG['NACOS_CLIENT_HOST']
        client_port = NACOS_CONFIG['NACOS_CLIENT_PORT']
        data_id = NACOS_CONFIG['NACOS_DATA_ID']
        group = NACOS_CONFIG['NACOS_GROUP']

        while True:
            if not self.is_connected:
                try:
                    self.client = init_nacos_client(
                        address=address,
                        namespace=namespace,
                        data_id=data_id,
                        server_name=server_name,
                        group=group,
                        client_host=client_host,
                        client_port=client_port
                    )
                except nacos.exception.NacosRequestException as e:
                    logger.error(e)
                else:
                    self.is_connected = True
            else:
                try:
                    # 发送心跳
                    self.client.send_heartbeat(server_name, client_host, client_port)
                except nacos.exception.NacosRequestException as e:
                    logger.error(e)
                    self.is_connected = False
            sleep(5)
