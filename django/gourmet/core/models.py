from django.db import models

# Create your models here.

class Seccion(models.Model):
    NombreSeccion = models.CharField(max_length=100, primary_key=True)
    Description = models.CharField(max_length=200)

class Familia(models.Model):
    NombreFamilia = models.CharField(max_length=100, primary_key=True)
    Description = models.CharField(max_length=200)
    NombreSeccion = models.ForeignKey(Seccion, on_delete=models.DO_NOTHING)

class SubFamilia(models.Model):
    NombreSubFamilia = models.CharField(max_length=100, primary_key=True)
    Description = models.CharField(max_length=200)
    NombreFamilia = models.ForeignKey(Familia, on_delete=models.DO_NOTHING)

class Proveedor(models.Model):
    CodProveedor = models.CharField(max_length=10, primary_key=True)
    NombreProveedor = models.CharField(max_length=100)
    PersonaContacto = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=25)
    PeriodoPago = models.SmallIntegerField(null=True)
    PagoPendiente = models.FloatField(null=True)
    TipoProveedor = models.CharField(max_length=100)
    Alcance = models.CharField(max_length=25)

class Producto(models.Model):
    CodProducto = models .CharField(max_length=25, primary_key=True)
    Description = models.CharField(max_length=100)
    NombrePais = models.CharField(max_length=100)
    Coste = models.FloatField(null=True)
    PrecioVenta = models.FloatField(null=True)
    TipoUnidad = models.CharField(max_length=100)
    NombreSubFamilia = models.ForeignKey(SubFamilia, on_delete=models.DO_NOTHING)
    Marca = models.CharField(max_length=100)
    CodProveedor = models.ForeignKey(Proveedor, on_delete=models.DO_NOTHING)

class RegionGeografica(models.Model):
    NombreRegion = models.CharField(max_length=100, primary_key=True)
    Continente = models.CharField(max_length=100)

class Pais(models.Model):
    NombrePais = models.CharField(max_length=100, primary_key=True)
    Extension = models.BigIntegerField(null=True)
    Poblacion = models.BigIntegerField(null=True)
    NombreRegion = models.ForeignKey(RegionGeografica, on_delete=models.DO_NOTHING)

class Tienda(models.Model):
    Nombre = models.CharField(max_length=100, primary_key=True)
    Direccion = models.CharField(max_length=100)
    Superficie = models.FloatField(null=True)
    FormatoTienda = models.CharField(max_length=100)
    Pais = models.ForeignKey(Pais, on_delete=models.DO_NOTHING)
    TipoZona = models.CharField(max_length=100)

class Cliente(models.Model):
    CodCliente = models.CharField(max_length=10, primary_key=True)
    NombreCliente = models.CharField(max_length=100)
    Sexo = models.CharField(max_length=25)
    FechaNacimiento = models.DateField(null=True)
    EstadoCivil = models.CharField(max_length=25)
    Direccion = models.CharField(max_length=100)
    Profesion = models.CharField(max_length=100)
    NumeroHijos = models.SmallIntegerField(null=True)
    Region = models.CharField(max_length=100)
    Nacionalidad = models.CharField(max_length=100)
    TotalCompras = models.SmallIntegerField(null=True)
    PuntosAcumulados = models.IntegerField(null=True)

class CabeceraTicket(models.Model):
    CodVenta = models.CharField(max_length=25, primary_key=True)
    NombreTienda = models.ForeignKey(Tienda, on_delete=models.DO_NOTHING, blank=True, null=True)
    Fecha = models.DateField(null=True)
    Hora = models.TimeField(null=True)
    FormaPago = models.CharField(max_length=100)
    CodCliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, blank=True, null=True)
    ImporteTotal = models.FloatField(null=True)
    TotalUnidades = models.IntegerField(null=True)
    PuntosTicket = models.IntegerField(null=True)

class Promocion(models.Model):
    NombrePromocion = models.CharField(max_length=100, primary_key=True)
    TipoPromocion = models.CharField(max_length=100)
    Coste = models.SmallIntegerField(null=True)
    FechaInicio = models.DateField(null=True)
    FechaFin = models.DateField(null=True)
    CodProducto = models.CharField(max_length=25)
    NombreFamilia = models.CharField(max_length=25)
    NombreSeccion = models.CharField(max_length=25)
    NombreTienda = models.CharField(max_length=25)
    NombreRegion = models.CharField(max_length=25)
    NombrePais = models.CharField(max_length=25)

class LineasTicket(models.Model):
    CodLinea = models.SmallIntegerField(null=True)
    CodVenta = models.ForeignKey(CabeceraTicket, on_delete=models.DO_NOTHING)
    NombreTienda = models.CharField(max_length=100)
    CodProducto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
    Cantidad = models.SmallIntegerField(null=True)
    PrecioVenta = models.FloatField(null=True)
    NombrePromocion = models.ForeignKey(Promocion, on_delete=models.DO_NOTHING, null=True)
    CodCabecera = models.IntegerField(null=True)

class Pedido(models.Model):
    CodPedido = models.CharField(max_length=25, primary_key=True)
    NombreTienda = models.ForeignKey(Tienda, on_delete=models.DO_NOTHING)
    CodProducto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
    PrecioCompra = models.FloatField(null=True)
    CantidadSolicitada = models.SmallIntegerField(null=True)
    FechaSolicitud = models.DateField(null=True)
    CantidadEntregada = models.SmallIntegerField(null=True)
    FechaEntrega = models.DateField(null=True)

