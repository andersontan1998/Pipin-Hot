# Generated by Django 4.0.4 on 2022-05-12 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0007_complaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='description',
            field=models.CharField(default='no description', max_length=100),
            preserve_default=False,
        ),
    ]
