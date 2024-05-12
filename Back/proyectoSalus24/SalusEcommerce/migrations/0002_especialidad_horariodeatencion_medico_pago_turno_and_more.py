# Generated by Django 5.0.4 on 2024-05-12 22:49

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalusEcommerce', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duracion', models.TimeField(default=datetime.timedelta(seconds=3600))),
                ('foto', models.ImageField(default='especialidades/no-especialidad.jpg', upload_to='especialidades', verbose_name='foto especialidad')),
                ('descripcion', models.CharField(blank=True, default='lorem', max_length=254)),
            ],
            options={
                'verbose_name': 'Especialidad',
                'verbose_name_plural': 'Especialidad',
                'db_table': 'Especialidad',
            },
        ),
        migrations.CreateModel(
            name='HorarioDeAtencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_de_la_semana', models.CharField(max_length=150)),
                ('hora_entrada', models.TimeField(default=datetime.time(8, 0))),
                ('hora_salida', models.TimeField(default=datetime.time(16, 0))),
            ],
            options={
                'verbose_name': 'HorarioDeAtencion',
                'verbose_name_plural': 'HorarioDeAtencion',
                'db_table': 'HorarioDeAtencion',
            },
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=11, unique=True)),
                ('nombre', models.CharField(blank=True, max_length=150)),
                ('apellido', models.CharField(blank=True, max_length=150)),
                ('email', models.CharField(blank=True, max_length=254)),
                ('clave', models.CharField(max_length=128)),
                ('telefono', models.CharField(blank=True, max_length=15)),
            ],
            options={
                'verbose_name': 'Medico',
                'verbose_name_plural': 'Medicos',
                'db_table': 'Medico',
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id_pago', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.IntegerField()),
                ('fecha', models.DateField(default=datetime.datetime.now)),
                ('hora', models.TimeField(default=datetime.datetime.now)),
                ('estado', models.CharField(blank=True, choices=[('Rechazado', 'Rechazado'), ('Aceptado', 'Aceptado'), ('Pendiento', 'Pendiento')], default='Rechazado', max_length=45)),
            ],
            options={
                'verbose_name': ' Pago de turns reservado por paciente',
                'verbose_name_plural': 'PagosDeTurnos',
                'db_table': 'pago',
            },
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('horario', models.TimeField()),
                ('pagado', models.BooleanField()),
                ('estado', models.CharField(blank=True, choices=[('Concluido', 'Concluido'), ('Rechazado', 'Rechazado'), ('Pendiento', 'Pendiento')], default='Rechazado', max_length=45)),
            ],
            options={
                'verbose_name': 'Turno',
                'verbose_name_plural': 'Turnos',
                'db_table': 'Turno',
            },
        ),
        migrations.AddField(
            model_name='paciente',
            name='foto',
            field=models.ImageField(default='paciente/perfil/no-img.png', upload_to='paciente/perfil', verbose_name='foto perfil paciente'),
        ),
        migrations.AddConstraint(
            model_name='especialidad',
            constraint=models.UniqueConstraint(fields=('nombre',), name='Uk_Especialidad_nombre'),
        ),
        migrations.AddConstraint(
            model_name='horariodeatencion',
            constraint=models.UniqueConstraint(fields=('dia_de_la_semana', 'hora_entrada', 'hora_salida'), name='Uk_HorarioDeAtencion'),
        ),
        migrations.AddField(
            model_name='medico',
            name='id_especialidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SalusEcommerce.especialidad'),
        ),
        migrations.AddField(
            model_name='medico',
            name='id_horario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SalusEcommerce.horariodeatencion'),
        ),
        migrations.AddField(
            model_name='medico',
            name='medicoUser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='turno',
            name='id_medico',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='SalusEcommerce.medico'),
        ),
        migrations.AddField(
            model_name='turno',
            name='id_paciente',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='SalusEcommerce.paciente'),
        ),
        migrations.AddField(
            model_name='pago',
            name='id_turno',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='SalusEcommerce.turno'),
        ),
        migrations.AddConstraint(
            model_name='medico',
            constraint=models.UniqueConstraint(fields=('matricula',), name='Uk_Medico'),
        ),
    ]
