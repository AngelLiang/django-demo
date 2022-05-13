from .monkey_patch import monkey_patch
import logging
from django.apps import AppConfig

LOGGER = logging.getLogger(__name__)


class RiverPatchConfig(AppConfig):
    name = 'river_patch'

    def ready(self):
        monkey_patch()
        LOGGER.debug('RiverPatch is loaded.')
