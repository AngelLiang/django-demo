# Generated by Django 5.0.2 on 2024-02-19 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passkeys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpasskey',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]