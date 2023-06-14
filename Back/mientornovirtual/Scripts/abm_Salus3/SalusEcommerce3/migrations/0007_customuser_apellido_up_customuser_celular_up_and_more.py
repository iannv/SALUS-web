# Generated by Django 4.2.2 on 2023-06-12 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalusEcommerce3', '0006_alter_customuser_nombre_up'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='Apellido_UP',
            field=models.CharField(blank=True, default='Apellido_UP', max_length=45),
        ),
        migrations.AddField(
            model_name='customuser',
            name='Celular_UP',
            field=models.CharField(blank=True, default='Celular_UP', max_length=45),
        ),
        migrations.AddField(
            model_name='customuser',
            name='Direccion_UP',
            field=models.CharField(blank=True, default='Direccion_UP', max_length=100),
        ),
        migrations.AddField(
            model_name='customuser',
            name='Dni_UP',
            field=models.CharField(blank=True, default='Dni_UP', max_length=8),
        ),
        migrations.AddField(
            model_name='customuser',
            name='Localidad_UP',
            field=models.CharField(blank=True, default='Localidad_UP', max_length=45),
        ),
        migrations.AddField(
            model_name='customuser',
            name='id_C',
            field=models.IntegerField(null=True, unique=True, verbose_name='cuenta corriente'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Nombre_UP',
            field=models.CharField(blank=True, default='Nombre_UP', max_length=45),
        ),
    ]
