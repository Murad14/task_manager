# Generated by Django 5.0 on 2024-01-17 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0010_task_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='task_photos/'),
        ),
    ]