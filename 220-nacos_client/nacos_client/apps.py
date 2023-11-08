from django.apps import AppConfig
from nacos_client.services import NACOS_ENABLE
from nacos_client.services import NacosClientThread


class NacosClientConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nacos_client'

    def ready(self):
        if NACOS_ENABLE:
            client = NacosClientThread(daemon=True)
            client.start()
