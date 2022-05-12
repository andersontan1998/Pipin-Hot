# Generated by Django 4.0.4 on 2022-05-10 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order_system', '0002_ordermodel_items'),
        ('forums', '0005_remove_forum_posts_reviewed_by_manager_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.AddField(
            model_name='review',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order_system.ordermodel'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(blank=True, default=10),
        ),
        migrations.AlterField(
            model_name='review',
            name='subject',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]