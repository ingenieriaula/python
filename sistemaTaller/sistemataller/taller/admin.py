from django.contrib import admin
from taller.models import *
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display    = [ 'id']


admin.site.register(Cliente, ClienteAdmin)

class ReservaAdmin(admin.ModelAdmin):
    list_display    = [ 'fechaReserva']

admin.site.register(Reserva , ClienteAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    list_display    = ['nombre', 'telefono']

admin.site.register(Usuario, UsuarioAdmin)

class RepuestoAdmin(admin.ModelAdmin):
    list_display = ['nombreRespuesto', 'stock']

admin.site.register(Repuesto, RepuestoAdmin)

class MecanicoAdmin(admin.ModelAdmin):
    list_display    = ['nombreMecanico', 'especializacion']

admin.site.register(Mecanico, MecanicoAdmin)

class MarcaAdmin(admin.ModelAdmin):
    list_display    = ['nombreMarca']

admin.site.register(Marca, MarcaAdmin)

class ModeloAdmin(admin.ModelAdmin):
    list_display    = ['marca', 'nombreModelo']

admin.site.register(Modelo, ModeloAdmin)

class VehiculoAdmin(admin.ModelAdmin):
    list_display    = ['modelo', 'patente']

admin.site.register(Vehiculo, VehiculoAdmin)


class OrdenTrabajoAdmin(admin.ModelAdmin):
    list_display    = ['usuario', 'cliente', 'repuesto', 'mecanico', 'vehiculo', 'tipoTrabajo', 'fechaComienzo']


admin.site.register(OrdenTrabajo, OrdenTrabajoAdmin)
