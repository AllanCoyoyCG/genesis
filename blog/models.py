from django.db import models
from django.utils import timezone
from django.contrib import admin


class Producto(models.Model):
    nombre  =   models.CharField(max_length=40)
    marca  =   models.CharField(max_length=40)
    proveedor  =   models.CharField(max_length=50)
    descripcion  =   models.CharField(max_length=70)

    def __str__(self):
        return self.nombre


class Tienda(models.Model):
    nombre    = models.CharField(max_length=60)
    direccion    = models.CharField(max_length=60)
    telefono      = models.IntegerField()
    productos   = models.ManyToManyField(Producto, through='Disposicion')
    def __str__(self):
        return self.nombre

class Disposicion (models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)


class DisposicionInLine(admin.TabularInline):
    model = Disposicion
    extra = 1


class ProductoAdmin(admin.ModelAdmin):
    inlines = (DisposicionInLine,)


class TiendaAdmin (admin.ModelAdmin):
    inlines = (DisposicionInLine,)
