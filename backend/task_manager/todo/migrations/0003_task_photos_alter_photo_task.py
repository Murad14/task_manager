# Generated by Django 5.0 on 2024-01-13 07:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='photos',
            field=models.ManyToManyField(blank=True, related_name='tasks', to='todo.photo'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_photos', to='todo.task'),
        ),
    ]
