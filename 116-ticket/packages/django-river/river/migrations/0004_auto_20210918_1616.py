# Generated by Django 2.2.24 on 2021-09-18 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('river', '0003_auto_20210825_1547'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='state',
            options={'verbose_name': '流程状态', 'verbose_name_plural': '流程状态'},
        ),
        migrations.AlterModelOptions(
            name='workflow',
            options={'verbose_name': '工作流程', 'verbose_name_plural': '工作流程'},
        ),
    ]
