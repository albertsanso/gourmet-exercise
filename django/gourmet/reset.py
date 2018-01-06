import csv, sys, os

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

LineasTicket.objects.all().delete()
CabeceraTicket.objects.all().delete()
Pedido.objects.all().delete()
Promocion.objects.all().delete()
Cliente.objects.all().delete()
Tienda.objects.all().delete()
Pais.objects.all().delete()
RegionGeografica.objects.all().delete()
Producto.objects.all().delete()
Proveedor.objects.all().delete()
SubFamilia.objects.all().delete()
Familia.objects.all().delete()
Seccion.objects.all().delete()

