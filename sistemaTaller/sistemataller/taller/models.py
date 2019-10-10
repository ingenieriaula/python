from django.db import models

# Create your models here.
class Cliente (models.Model):
    nombre = models.CharField(max_length=30)
    rut = models.CharField(max_length=12)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=45)
    correo = models.EmailField(max_length=30)

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipoReserva = models.CharField(max_length=50)
    fechaReserva = models.DateField()
    horaReserva = models.TimeField()
    descripcion = models.CharField(max_length=150)

class Usuario (models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    tipoUsuario = models.CharField(max_length=30)

class Repuesto (models.Model):
    nombreRespuesto = models.CharField(max_length=50)
    stock = models.IntegerField()
    precio = models.IntegerField()

class Mecanico (models.Model):
    nombreMecanico = models.CharField(max_length=50)
    especializacion = models.CharField(max_length=50)

class Marca (models.Model):
    nombreMarca = models.CharField(max_length=30)

class Modelo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nombreModelo = models.CharField(max_length=30)

class Vehiculo(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    patente = models.CharField(max_length=9)
    year = models.DateField()


class OrdenTrabajo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    repuesto = models.ForeignKey(Repuesto, on_delete=models.CASCADE)
    mecanico = models.ForeignKey(Mecanico, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    tipoTrabajo = models.CharField(max_length=50)
    fechaComienzo = models.DateField()
    fechaTermino = models.DateField()
    descripcion = models.CharField(max_length=150)
    precio = models.IntegerField()
    abono = models.IntegerField()
    total = models.IntegerField()
