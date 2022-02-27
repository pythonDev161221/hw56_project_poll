# Generated by Django 4.0.2 on 2022-02-27 04:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0009_productbasket_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productbasket',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products_basket', to=settings.AUTH_USER_MODEL),
        ),
    ]