# Generated by Django 4.1.4 on 2023-02-21 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_alter_tarea_terminado_el'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='terminado_el',
        ),
        migrations.AddField(
            model_name='tarea',
            name='modificado_el',
            field=models.DateField(auto_now=True),
        ),
    ]
