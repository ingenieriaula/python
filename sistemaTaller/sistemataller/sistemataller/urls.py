"""sistemataller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from taller.models import *
from rest_framework import routers, serializers, viewsets

# -------USUARIO------

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre','telefono','tipoUsuario']

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# ------------CLIENTE----------

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nombre','rut','telefono','direccion','correo']

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

# -------------------- RESERVA--------------------

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['tipoReserva','fechaReserva','horaReserva','descripcion','cliente']

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

# ------------------------REPUESTO--------------
class RepuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repuesto
        fields = ['nombreRepuestro','stock','precio']

class RepuestoViewSet(viewsets.ModelViewSet):
    queryset = Repuesto.objects.all()
    serializer_class = RepuestoSerializer

# -----------------MECANICO-------------------

class MecanicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mecanico
        fields = ['nombreMecanico','especializacion']

class MecanicoViewSet(viewsets.ModelViewSet):
    queryset = Mecanico.objects.all()
    serializer_class = MecanicoSerializer

# --------Marca------------------

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['nombreMarca']

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

 # -----------------------Modelo-----------

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = ['nombreModelo','marca']

class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer

# ---------------VEHICULO------------

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['patente','year','modelo']

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

# ------------------ORDENTRABAJO----------------

class OrdenTrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenTrabajo
        fields = ['tipoTrabajo','fechaComienzo',
                  'fechaTermino','descripcion',
                  'precio','abono',
                  'total','usuario',
                  'cliente','repuesto',
                  'mecanico','vehiculo']

class OrdenTrabajoViewSet(viewsets.ModelViewSet):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer

# --------------NOMBRE DE RUTA EN LA URL--------------

router = routers.DefaultRouter()
router.register(r'usuario', UsuarioViewSet)
router.register(r'cliente', ClienteViewSet)
router.register(r'reserva', ReservaViewSet)
router.register(r'repuesto', RepuestoViewSet)
router.register(r'mecanico', MecanicoViewSet)
router.register(r'marca', MarcaViewSet)
router.register(r'modelo', ModeloViewSet)
router.register(r'vehiculo', VehiculoViewSet)
router.register(r'ordenTrabajo', OrdenTrabajoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
