# Generated by Django 3.2.12 on 2023-06-09 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichas', '0007_auto_20230602_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(choices=[('Administrador', 'Administrador'), ('Funcionario', 'Funcionario'), ('Usuario', 'Usuario')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.CharField(max_length=13, null=True),
        ),
    ]
