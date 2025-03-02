from django.db import models

class Seccion(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Plato(models.Model):
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, related_name="platos")
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} - €{self.precio}"

class Galeria(models.Model):
    foto = models.ImageField(upload_to='galeria/')
    descripcion = models.CharField(max_length= 100, blank=True, null=True)

    def __str__(self):
        return self.descripcion
    
class Reseña(models.Model):
    nombre = models.CharField(max_length=100)
    comentario = models.TextField()
    puntuacion = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.puntuacion}⭐"