# Generated by Django 4.2.7 on 2023-12-04 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(db_comment='操作', max_length=64)),
                ('type', models.IntegerField(db_comment='操作类型。1新增；2修改；3删除；-1其他')),
                ('table_name', models.CharField(db_comment='表名称', max_length=64)),
                ('row_id', models.CharField(db_comment='数据id', max_length=64)),
                ('row_repr', models.CharField(db_comment='数据名称', max_length=64)),
                ('action_at', models.DateTimeField(auto_now=True, db_comment='操作时间')),
                ('actor', models.CharField(db_comment='操作者', max_length=64)),
                ('change_text', models.TextField(db_comment='操作信息')),
            ],
            options={
                'db_table': 'action_log',
                'managed': True,
            },
        ),
    ]