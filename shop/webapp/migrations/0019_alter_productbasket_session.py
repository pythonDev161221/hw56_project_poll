# Generated by Django 4.0.2 on 2022-03-04 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0018_productbasket_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productbasket',
            name='session',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
