# Generated by Django 4.0.2 on 2022-02-28 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_alter_productbasket_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productbasket',
            name='user',
        ),
    ]