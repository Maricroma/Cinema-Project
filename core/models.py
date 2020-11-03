from django.db import models

# Create your models here.
class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

#python manage.py makemigrations <-- lee el archivo models y crea un archivo de migración
#python manage.py migrate <-- tomar las migraciones pendientes y volcarlas a la DB
#python manage.py createsuperuser

class Pelicula(models.Model):
    nombre = models.CharField(max_length=100)
    duracion = models.IntegerField(verbose_name="Duración")
    anio = models.IntegerField(verbose_name="Año")
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE) #si se borra un genero, se borran todas las peliculas de ese genreo
    sinopsis = models.TextField(null=True, blank=True)
    fecha_estreno = models.DateField()  
    imagen = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nombre