# Generated by Django 4.0.4 on 2022-05-11 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_system', '0007_alter_ordermodel_is_delivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]