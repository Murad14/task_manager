# Generated by Django 5.0 on 2024-01-14 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_task_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='image',
        ),
    ]
