# Generated by Django 4.0.4 on 2022-05-07 02:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forums', '0003_alter_forum_posts_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum_posts',
            name='post_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
