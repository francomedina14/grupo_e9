from django.contrib import admin
from django.urls import path
from productos.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', listar_productos),
    path('crear/producto/', crear_producto, name='crear'),
    path('editar/producto/<pk>', editar_producto, name='editar'),
    path('actualizar/producto/<pk>', actualizar_producto, name='actualizar'),
    path('eliminar/producto/<pk>', eliminar_producto, name='eliminar'),
]
