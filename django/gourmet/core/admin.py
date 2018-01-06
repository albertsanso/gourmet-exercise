from django.contrib import admin

# Register your models here.

from .models import Seccion
from .models import Familia
from .models import SubFamilia
from .models import Producto
from .models import Proveedor
from .models import RegionGeografica
from .models import Pais
from .models import Tienda
from .models import Cliente
from .models import CabeceraTicket
from .models import Promocion
from .models import LineasTicket
from .models import Pedido

admin.site.register(Seccion)
admin.site.register(Familia)
admin.site.register(SubFamilia)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(RegionGeografica)
admin.site.register(Pais)
admin.site.register(Cliente)
admin.site.register(Tienda)
admin.site.register(CabeceraTicket)
admin.site.register(Promocion)
admin.site.register(LineasTicket)
admin.site.register(Pedido)
