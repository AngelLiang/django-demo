# Generated by Django 2.2.28 on 2022-05-01 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_sync', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailsynclog',
            name='is_success',
            field=models.BooleanField(default=True, verbose_name='操作成功'),
        ),
    ]
