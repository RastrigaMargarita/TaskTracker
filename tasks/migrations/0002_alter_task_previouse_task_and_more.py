# Generated by Django 5.0.2 on 2024-02-26 20:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='previouse_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.task', verbose_name='Предыдущий таск'),
        ),
        migrations.AlterField(
            model_name='task',
            name='responsible_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.employee', verbose_name='Ответственный'),
        ),
    ]