# Generated by Django 4.0.4 on 2022-05-16 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order', models.IntegerField(default=0)),
                ('Bid_Amount', models.IntegerField(default=100)),
                ('lowest_bid', models.IntegerField(blank=True)),
            ],
        ),
    ]