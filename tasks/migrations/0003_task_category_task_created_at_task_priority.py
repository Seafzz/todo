# Generated by Django 5.1.4 on 2024-12-07 01:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('W', 'Work'), ('P', 'Personal'), ('O', 'Others')], default='O', max_length=1),
        ),
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('L', 'Low'), ('U', 'Urgent'), ('A', 'Asap')], default='M', max_length=1),
        ),
    ]
