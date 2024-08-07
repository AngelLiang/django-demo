# Generated by Django 4.2.14 on 2024-08-02 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_created_at_user_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('key', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'user_token',
            },
        ),
    ]
