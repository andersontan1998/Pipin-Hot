# Generated by Django 4.0.4 on 2022-05-10 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_log', '0003_alter_chef_rating_alter_customer_account_funds_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='is_vip',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='warnings',
            field=models.IntegerField(default=0),
        ),
    ]