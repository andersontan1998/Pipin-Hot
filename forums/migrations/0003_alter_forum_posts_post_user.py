# Generated by Django 4.0.4 on 2022-05-07 02:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forums', '0002_forum_posts_reviewed_by_manager_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum_posts',
            name='post_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
