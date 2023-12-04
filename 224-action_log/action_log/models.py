from django.db import models


class ActionLog(models.Model):
    # id = models.BigAutoField(primary_key=True, db_comment='主键')
    action = models.CharField(max_length=64, db_comment='操作')
    type = models.IntegerField(db_comment='操作类型。1新增；2修改；3删除；-1其他')
    table_name = models.CharField(max_length=64, db_comment='表名称')
    row_id = models.CharField(max_length=64, db_comment='数据id')
    row_repr = models.CharField(max_length=64, db_comment='数据名称')
    action_at = models.DateTimeField(db_comment='操作时间', auto_now=True)
    actor = models.CharField(max_length=64, db_comment='操作者')
    change_text = models.TextField(db_comment='操作信息')

    class Meta:
        managed = True
        db_table = 'action_log'

    ADD = 1
    UPDATE = 2
    DELETE = 3
    OHTER = -1
