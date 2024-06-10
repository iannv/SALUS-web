# Generated by Django 5.0.6 on 2024-06-08 07:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalusEcommerce', '0002_turno_obra_social_turnosdisponibles_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turno',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='turno',
            name='horario',
        ),
        migrations.AddField(
            model_name='turno',
            name='turno_disponible',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SalusEcommerce.turnosdisponibles'),
            preserve_default=False,
        ),
    ]