from django.contrib import admin


from gestionPedidos.models import clientes
from gestionPedidos.models import articulos
from gestionPedidos.models import pedidos
from gestionPedidos.models import proveedores

# Register your models here.
admin.site.register(clientes)
admin.site.register(articulos)
admin.site.register(pedidos)
admin.site.register(proveedores)    
