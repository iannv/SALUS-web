# Generated by Django 4.2.2 on 2023-06-12 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalusEcommerce3', '0004_remove_customuser_date_joined_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='Nombre_UP',
            field=models.CharField(default='Nombre', max_length=45, null=True),
        ),
    ]
