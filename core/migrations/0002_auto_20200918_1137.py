# Generated by Django 3.0 on 2020-09-18 14:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='fecha_estreno',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pelicula',
            name='sinopsis',
            field=models.TextField(blank=True, null=True),
        ),
    ]
