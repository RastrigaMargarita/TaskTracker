# Generated by Django 5.0.2 on 2024-02-26 17:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.CharField(max_length=500, verbose_name='Описание')),
                ('status', models.BooleanField(verbose_name='Выполнено')),
                ('estimated_duration', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Оценка выполнения в часах')),
                ('previouse_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task', verbose_name='Предыдущий таск')),
                ('responsible_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee', verbose_name='Ответственный')),
            ],
        ),
    ]