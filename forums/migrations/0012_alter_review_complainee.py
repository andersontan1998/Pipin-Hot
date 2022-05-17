# Generated by Django 4.0.4 on 2022-05-17 02:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forums', '0011_remove_review_description_remove_review_is_complaint_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='complainee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]