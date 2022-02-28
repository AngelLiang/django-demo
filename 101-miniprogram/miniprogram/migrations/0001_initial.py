# Generated by Django 2.2.26 on 2022-01-21 08:03

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
            name='WeChatUserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickName', models.CharField(default='', max_length=100, verbose_name='微信昵称')),
                ('avatarUrl', models.CharField(max_length=255, null=True, verbose_name='微信头像')),
                ('gender', models.CharField(choices=[(0, '未知'), (1, '男性'), (2, '女性')], max_length=2, null=True, verbose_name='性别')),
                ('city', models.CharField(default='', max_length=100, verbose_name='城市')),
                ('province', models.CharField(default='', max_length=100, verbose_name='省份')),
                ('country', models.CharField(default='', max_length=100, verbose_name='国家')),
            ],
            options={
                'verbose_name': '微信个人信息',
                'verbose_name_plural': '微信个人信息',
                'permissions': (('add_wechatuserinfo', '允许添加微信个人信息'), ('view_wechatuserinfo', '允许查看微信个人信息'), ('change_wechatuserinfo', '允许修改微信个人信息'), ('delete_wechatuserinfo', '允许删除微信个人信息')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='WeChatAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openId', models.CharField(default='', max_length=255, verbose_name='OPENID')),
                ('unionId', models.CharField(blank=True, default='', max_length=255, verbose_name='UNIONID')),
                ('session_key', models.CharField(default='', max_length=255, verbose_name='SESSION_KEY')),
                ('user', models.OneToOneField(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='帐号')),
                ('userinfo', models.OneToOneField(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='miniprogram.WeChatUserInfo', verbose_name='微信个人信息')),
            ],
            options={
                'verbose_name': '微信帐号',
                'verbose_name_plural': '微信帐号',
                'permissions': (('add_wechataccount', '允许添加微信帐号'), ('view_wechataccount', '允许查看微信帐号'), ('change_wechataccount', '允许修改微信帐号'), ('delete_wechataccount', '允许删除微信帐号')),
                'default_permissions': (),
            },
        ),
    ]