# Generated by Django 4.2.5 on 2023-09-23 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCitasMedicas', '0002_alter_clinica_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='fecha_de_cita',
            field=models.DateField(),
        ),
    ]
