# Generated by Django 4.0.4 on 2022-05-08 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_fooditem'),
        ('order_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='items',
            field=models.ManyToManyField(blank=True, related_name='order', to='menu.fooditem'),
        ),
    ]
