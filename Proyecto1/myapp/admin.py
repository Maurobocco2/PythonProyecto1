from django.contrib import admin
from .models import Cliente, Equipo, Tecnico, Reparacion


admin.site.site_header = "Admin de NovaRepara"
admin.site.site_title = "Panel de Administración de NovaRepara"
admin.site.index_title = "Bienvenido al Panel de Administración de NovaRepara"
admin.site.register(Cliente)
admin.site.register(Equipo)
admin.site.register(Tecnico)
admin.site.register(Reparacion)