# Generated by Django 2.2.27 on 2022-03-24 05:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.CharField(max_length=20, unique=True, verbose_name='单据编号')),
                ('order_date', models.DateField(verbose_name='单据日期')),
                ('prefix', models.CharField(max_length=8, verbose_name='单号前缀')),
                ('number', models.PositiveIntegerField(verbose_name='单据号数')),
                ('title', models.CharField(max_length=128, verbose_name='标题')),
                ('content', models.TextField(default='', max_length=1024, verbose_name='内容')),
                ('creator', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
            ],
            options={
                'verbose_name': '单据',
                'verbose_name_plural': '单据',
                'permissions': (('add_order', '允许添加单据'), ('view_order', '允许查看单据'), ('change_order', '允许修改单据'), ('delete_order', '允许删除单据')),
                'default_permissions': (),
            },
        ),
    ]
