import csv, sys, os
import datetime

project_dir = "C:/dev/PACS/gourmet-exercise/django/gourmet"
data_dir = "C:/dev/PACS/gourmet-exercise/data"

sys.path.append(project_dir)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gourmet.settings')

import django
django.setup()

from core.models import Seccion
from core.models import Familia
from core.models import SubFamilia
from core.models import Proveedor
from core.models import Producto
from core.models import RegionGeografica
from core.models import Pais
from core.models import Cliente
from core.models import Tienda
from core.models import CabeceraTicket
from core.models import Promocion
from core.models import Pedido
from core.models import LineasTicket

"""
data = csv.reader(open(data_dir+"/seccion.cvs", encoding="utf8"), delimiter=",")
for row in data:
    oID = row[0]
    oDesc = row[1]

    seccion = Seccion()
    seccion.NombreSeccion = oID
    seccion.Description = oDesc
    seccion.save()

data = csv.reader(open(data_dir+"/familia.cvs", encoding="utf8"), delimiter=",")
for row in data:
    oID = row[0]
    oDesc = row[1]
    oSeccionId = row[2]
    oSeccion = Seccion.objects.get(pk=oSeccionId)

    familia = Familia()
    familia.NombreFamilia = oID
    familia.Description = oDesc
    familia.NombreSeccion = oSeccion
    familia.save()

data = csv.reader(open(data_dir+"/subfamilia.cvs", encoding="utf8"), delimiter=",")
for row in data:
    oID = row[0]
    oDesc = row[1]
    oNombreFamilia = row[2]
    oFamilia = Familia.objects.get(pk=oNombreFamilia)

    subfamilia = SubFamilia()
    subfamilia.NombreSubFamilia = oID
    subfamilia.Description = oDesc
    subfamilia.NombreFamilia = oFamilia
    subfamilia.save()

data = csv.reader(open(data_dir+"/proveedor.cvs", encoding="utf8"), delimiter=",")
for row in data:
    oID = row[0]
    oNombreProveedor = row[1]
    oPersonaContacto = row[2]
    oDireccion = row[3]
    oTelefono = row[4]
    oPeriodoPago = row[5]
    oPagoPendiente = row[6]
    oTipoProveedor = row[7]
    oAlcance = row[8]

    proveedor = Proveedor()
    proveedor.CodProveedor = oID
    proveedor.NombreProveedor = oNombreProveedor
    proveedor.PersonaContacto = oPersonaContacto
    proveedor.Direccion = oDireccion
    proveedor.Telefono = oTelefono
    proveedor.PeriodoPago = oPeriodoPago
    try:
        proveedor.PagoPendiente = float(oPagoPendiente)
    except:
        proveedor.PagoPendiente = None

    proveedor.TipoProveedor = oTipoProveedor
    proveedor.Alcance = oAlcance
    proveedor.save()

data = csv.reader(open(data_dir+"/producto.cvs", encoding="utf8"), delimiter=",")
for row in data:
    oID = row[0]
    oDesc = row[1]
    oPais = row[2]
    oCoste = row[3]
    oPrecioVenta = row[4]
    oTipoUnidad = row[5]
    oSubfamiliaID = row[6]
    oNombreSubFamilia = SubFamilia.objects.get(pk=oSubfamiliaID)
    oMarca = row[7]
    oProveedorID = row[8]
    oCodProveedor = Proveedor.objects.get(pk=oProveedorID)

    producto = Producto()
    producto.CodProducto = oID
    producto.Description = oDesc
    producto.NombrePais = oPais
    producto.Coste = oCoste
    producto.PrecioVenta = oPrecioVenta
    producto.TipoUnidad = oTipoUnidad
    producto.NombreSubFamilia = oNombreSubFamilia
    producto.Marca = oMarca
    producto.CodProveedor = oCodProveedor
    producto.save()

data = csv.reader(open(data_dir+"/regiongeografica.cvs", encoding="utf8"), delimiter=",")
for row in data:
    oID = row[0]
    oDesc = row[1]

    region = RegionGeografica()
    region.NombreRegion = oID
    region.Continente = oDesc
    region.save()

data = csv.reader(open(data_dir+"/pais.cvs", encoding="utf8"), delimiter=",")
for row in data:
    oID = row[0]
    oExtension = row[1]
    oPoblacion = row[2]
    oRegionID = row[3]
    oRegion = RegionGeografica.objects.get(pk=oRegionID)

    pais = Pais()
    pais.NombrePais = oID
    pais.Extension = int(oExtension[1:-1])
    pais.Poblacion = int(oPoblacion[1:-1])
    pais.NombreRegion = oRegion
    pais.save()

data = csv.reader(open(data_dir+"/cliente.cvs", encoding="utf8"), delimiter=",")
for row in data:
    oID = row[0]
    oNombreCliente = row[1]
    oSexo = row[2]
    oFechaNacimiento = row[3]
    oEstadoCivil = row[4]
    oDireccion = row[5]
    oProfesion = row[6]
    oNumeroHijos = row[7]
    oRegion = row[8]
    oNacionalidad = row[9]
    oTotalCompras = row[10]
    oPuntosAcumulados = row[11]

    try:
        oFechaNacimiento = datetime.date(int(oFechaNacimiento[0:4]), int(oFechaNacimiento[4:6]), int(oFechaNacimiento[6:8]))
    except:
        oFechaNacimiento = None

    if oNumeroHijos == '':
        oNumeroHijos = None

    cliente = Cliente()
    cliente.CodCliente = oID
    cliente.NombreCliente = oNombreCliente
    cliente.Sexo = oSexo
    cliente.FechaNacimiento = oFechaNacimiento
    cliente.EstadoCivil = oEstadoCivil
    cliente.Direccion = oDireccion
    cliente.Profesion = oProfesion
    cliente.NumeroHijos = oNumeroHijos
    cliente.Region = oRegion
    cliente.Nacionalidad = oNacionalidad
    cliente.TotalCompras = oTotalCompras
    cliente.PuntosAcumulados = oPuntosAcumulados
    cliente.save()

data = csv.reader(open(data_dir+"/tienda.cvs", encoding="utf8"), delimiter=",")
for row in data:
    oID = row[0]
    oDireccion = row[1]
    oSuperficie = row[2]
    oFormatoTienda = row[3]
    oPaisID = row[4]
    oPais = Pais.objects.get(pk=oPaisID)
    oTipoZona = row[5]

    tienda = Tienda()
    tienda.Nombre = oID
    tienda.Direccion = oDireccion
    tienda.Superficie = oSuperficie
    tienda.FormatoTienda = oFormatoTienda
    tienda.Pais = oPais
    tienda.TipoZona = oTipoZona
    tienda.save()

"""

data = csv.reader(open(data_dir+"/cabeceraticket.cvs", encoding="utf8"), delimiter=",")
for row in data:
    oID = row[0]
    oNombreTiendaID = row[1]
    oTienda = None
    try:
        oTienda = Tienda.objects.get(pk=oNombreTiendaID)
    except:
        pass

    oFecha = row[2]
    oHora = row[3]
    oFormaPago = row[4]
    oCodClienteID = row[5]
    oCliente = None
    try:
        oClientId = CodClienteID.strip()
        oCliente = Cliente.objects.get(pk=oCodClienteID)
    except:
        pass

    oImporteTotal = row[6]
    oTotalUnidades = row[7]
    oPuntosTicket = row[8]

    try:
        oFecha = datetime.date(int(oFecha[0:4]), int(oFecha[4:6]), int(oFecha[6:8]))
    except:
        oFecha = None

    try:
        oHora = datetime.time(int(oHora), 0)
    except:
        oHora = None

    cabecera = CabeceraTicket()
    cabecera.CodVenta = oID
    cabecera.NombreTienda = oTienda
    cabecera.Fecha = oFecha
    cabecera.Hora = oHora
    cabecera.FormaPago = oFormaPago
    cabecera.CodCliente = oCliente
    cabecera.ImporteTotal = oImporteTotal
    cabecera.TotalUnidades = oTotalUnidades
    cabecera.PuntosTicket = oPuntosTicket
    cabecera.save()

data = csv.reader(open(data_dir+"/promocion.cvs", encoding="utf8"), delimiter=",")
for row in data:
    oID = row[0]
    oTipoPromocion = row[1]
    oCoste = row[2]
    oFechaInicio = row[3]
    oFechaFin = row[4]
    oCodProducto = row[5]
    oNombreFamilia = row[6]
    oNombreSeccion = row[7]
    oNombreTienda = row[8]
    oNombreRegion = row[9]
    oNombrePais = row[10]

    try:
        oFechaInicio = datetime.date(int(oFechaInicio[0:4]), int(oFechaInicio[4:6]), int(oFechaInicio[6:8]))
    except:
        oFechaInicio = None

    try:
        oFechaFin = datetime.date(int(oFechaFin[0:4]), int(oFechaFin[4:6]), int(oFechaFin[6:8]))
    except:
        oFechaFin = None


    if oCoste == '':
        oCoste = None

    promocion = Promocion()
    promocion.NombrePromocion = oID
    promocion.TipoPromocion = oTipoPromocion
    promocion.Coste = oCoste
    promocion.FechaInicio = oFechaInicio
    promocion.FechaFin = oFechaFin
    promocion.CodProducto = oCodProducto
    promocion.NombreFamilia = oNombreFamilia
    promocion.NombreSeccion = oNombreSeccion
    promocion.NombreTienda = oNombreTienda
    promocion.NombreRegion = oNombreRegion
    promocion.NombrePais = oNombrePais
    promocion.save()

data = csv.reader(open(data_dir+"/pedido.cvs", encoding="utf8"), delimiter=",")
for row in data:
    oID = row[0]
    oNombreTiendaID = row[1]
    oNombreTienda = None
    try:
        oNombreTiendaID = oNombreTiendaID.strip()
        oNombreTienda = Tienda.objects.get(pk=oNombreTiendaID)
    except:
        pass

    oCodProductoID = row[2]
    oCodProducto = None
    try:
        oCodProductoID = oCodProductoID.strip()
        oCodProducto = Producto.objects.get(pk=oCodProductoID)
    except:
        pass

    oPrecioCompra = row[3]
    oCantidadSolicitada = row[4]
    oFechaSolicitud = row[5]
    oCantidadEntregada = row[6]
    oFechaEntrega = row[7]

    oFechaSolicitud = datetime.date(int(oFechaSolicitud[0:4]), int(oFechaSolicitud[4:6]), int(oFechaSolicitud[6:8]))
    oFechaEntrega = datetime.date(int(oFechaEntrega[0:4]), int(oFechaEntrega[4:6]), int(oFechaEntrega[6:8]))

    pedido = Pedido()
    pedido.CodPedido = oID
    pedido.NombreTienda = oNombreTienda
    pedido.CodProducto = oCodProducto
    pedido.PrecioCompra = oPrecioCompra
    pedido.CantidadSolicitada = oCantidadSolicitada
    pedido.CantidadEntregada = oCantidadEntregada
    pedido.FechaSolicitud = oFechaSolicitud
    pedido.FechaEntrega = oFechaEntrega
    pedido.save()

data = csv.reader(open(data_dir+"/lineasticket.cvs", encoding="utf8"), delimiter=",")
for row in data:
    oID = row[0]
    oCodVentaID = row[1]
    oCodVenta=None
    
    try:
        oCodVentaID = oCodVentaID.strip()
        oCodVenta = CabeceraTicket.objects.get(pk=oCodVentaID)
    except:
        pass

    oNombreTienda = row[2]

    oCodProductoID = row[3]
    oCodProducto = None

    try:
        oCodProductoID = oCodProductoID.strip()
        oCodProducto = Producto.objects.get(pk=oCodProductoID)
    except:
        pass

    oCantidad = row[4]
    oPrecioVenta = row[5]

    oNombrePromocionID = row[6]
    oNombrePromocion = None

    try:
        oNombrePromocionID = oNombrePromocionID.strip()
        oNombrePromocion = Promocion.objects.get(pk=oNombrePromocionID)
    except:
        pass

    oCodCabecera = row[7]

    linea = LineasTicket()
    linea.CodLinea = oID
    linea.CodVenta = oCodVenta
    linea.NombreTienda = oNombreTienda
    linea.CodProducto = oCodProducto
    linea.Cantidad = oCantidad
    linea.PrecioVenta = oPrecioVenta
    linea.NombrePromocion = oNombrePromocion
    linea.CodCabecera = oCodCabecera
    linea.save()
