# Generated by Django 4.1.7 on 2023-04-01 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaEmpresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Area', models.CharField(max_length=30)),
                ('Cantidad_Trabajadores', models.PositiveIntegerField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Empleado', models.CharField(max_length=30)),
                ('Apellido_Empleado', models.CharField(max_length=30)),
                ('Cargo_Empleado', models.CharField(max_length=50)),
                ('Fecha_Ingreso', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ciudad', models.CharField(max_length=30)),
                ('Numero_Sucursal', models.PositiveIntegerField(default=False)),
            ],
        ),
    ]