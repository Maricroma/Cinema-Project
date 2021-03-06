# Generated by Django 3.0 on 2020-09-11 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('duracion', models.IntegerField(verbose_name='Duración')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Genero')),
            ],
        ),
    ]
