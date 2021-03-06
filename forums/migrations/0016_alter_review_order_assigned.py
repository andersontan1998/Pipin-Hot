# Generated by Django 4.0.4 on 2022-05-17 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order_system', '0008_ordermodel_is_paid'),
        ('forums', '0015_review_order_assigned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='order_assigned',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order_system.ordermodel'),
        ),
    ]
