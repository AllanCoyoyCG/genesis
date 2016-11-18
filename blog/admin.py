from django.contrib import admin
from .models import Producto, ProductoAdmin, Tienda, TiendaAdmin

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Tienda, TiendaAdmin)

# Register your models here.
