import json
import datetime
from typing import Dict
from action_log.models import ActionLog


class ActionLogService:
    Model = ActionLog

    def __init__(self, request=None) -> None:
        self.request = request

    def get_queryset(self):
        return self.Model.objects.get_queryset()

    def add(self, data: Dict):
        obj = self.Model(**data)
        obj.save()
        return obj

    def compare_value(self, old_value, new_value):
        """对比值"""
        if isinstance(old_value, datetime.datetime) and isinstance(new_value, datetime.datetime):
            return old_value.timestamp() == new_value.timestamp()
        # elif isinstance(old_value, datetime.time) and isinstance(new_value, datetime.time):
        #     return old_value == new_value.timestamp()
        else:
            return old_value == new_value

    def compare_dict(self, old_dict, new_dict) -> Dict:
        """对比字典"""
        changed_fields = {}

        for key in old_dict:
            if key in new_dict:
                if not self.compare_value(old_dict[key], new_dict[key]):
                    changed_fields[key] = (old_dict[key], new_dict[key])
            else:
                changed_fields[key] = (old_dict[key], None)

        for key in new_dict:
            if key not in old_dict:
                changed_fields[key] = (None, new_dict[key])

        return changed_fields

    def get_obj_data(self, obj, fields):
        data = {}
        if obj:
            for field in fields:
                value = getattr(obj, field)
                data[field] = value
        return data

    def make_change_text(self, old, new, fields):
        old_dict = self.get_obj_data(old, fields)
        new_dict = self.get_obj_data(new, fields)
        change_data = self.compare_dict(old_dict, new_dict)
        return json.dumps(change_data, default=str)

    def add_add_log(self, obj, fields, action=None, actor='', row_repr=None):
        """添加创建日志"""
        action_log = ActionLog()
        action_log.action = action if action else f'添加{obj._meta.verbose_name}'
        action_log.type = ActionLog.ADD
        action_log.actor = actor
        action_log.table_name = obj._meta.db_table
        action_log.row_id = obj.pk
        if row_repr is None:
            action_log.row_repr = repr(obj)
        action_log.change_text = self.make_change_text(None, obj, fields)
        action_log.save()

    def add_update_log(self, old, new, fields, action=None, actor='', row_repr=None):
        """添加更新日志"""
        action_log = ActionLog()
        action_log.action = action if action else f'修改{old._meta.verbose_name}'
        action_log.type = ActionLog.UPDATE
        action_log.actor = actor
        action_log.table_name = old._meta.db_table
        action_log.row_id = old.pk
        if row_repr is None:
            action_log.row_repr = repr(old)
        action_log.change_text = self.make_change_text(old, new, fields)
        action_log.save()

    def add_del_log(self, obj, action=None, actor='', row_repr=None):
        """添加删除日志"""
        action_log = ActionLog()
        action_log.action = action if action else f'删除{obj._meta.verbose_name}'
        action_log.type = ActionLog.DELETE
        action_log.actor = actor
        action_log.table_name = obj._meta.db_table
        if row_repr is None:
            action_log.row_repr = repr(obj)
        action_log.row_id = obj.pk
        action_log.save()
