# Generated by Django 4.0.4 on 2022-05-10 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_system', '0006_ordermodel_deliver_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='is_delivery',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
