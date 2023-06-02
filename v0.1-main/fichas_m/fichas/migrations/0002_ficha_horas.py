# Generated by Django 4.2.1 on 2023-05-31 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fichas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=13)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateTimeField()),
                ('previcion_salud', models.CharField(max_length=13)),
                ('domicilio', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Horas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('ocupada', models.BooleanField()),
                ('id_medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fichas.personalsalud')),
            ],
        ),
    ]