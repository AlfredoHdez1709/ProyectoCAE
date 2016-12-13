from django.contrib import admin
from .models import Perfil
from .models import RegistroClie

admin.site.register(Perfil)
admin.site.register(RegistroClie)
list_display = ('nombre','apellido','fecha')