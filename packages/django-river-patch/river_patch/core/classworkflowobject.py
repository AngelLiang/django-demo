from django.contrib.contenttypes.models import ContentType

from river.driver.mssql_driver import MsSqlDriver
from river.driver.orm_driver import OrmDriver
from river.models import State, TransitionApprovalMeta, Workflow, app_config, TransitionMeta
from ..driver.mysql_driver import MySqlDriver


class ClassWorkflowObject(object):


    @property
    def _river_driver(self):
        from django.db import connection

        if self._cached_river_driver:
            return self._cached_river_driver
        else:
            if app_config.IS_MSSQL:
                self._cached_river_driver = MsSqlDriver(self.workflow, self.wokflow_object_class, self.field_name)
            elif connection.vendor == 'mysql':
                self._cached_river_driver = MySqlDriver(self.workflow, self.wokflow_object_class, self.field_name)
            else:
                self._cached_river_driver = OrmDriver(self.workflow, self.wokflow_object_class, self.field_name)
            return self._cached_river_driver
