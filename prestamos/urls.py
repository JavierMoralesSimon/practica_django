from django.urls import path
from django.contrib.auth import views as auth_views
from prestamos import views as v

urlpatterns = [
    path('index/', v.index , name='prestamos.index'),
    path('crear/<int:id>/', v.prestamos_crear, name='prestamos.crear'),
    path('actualizar/<int:id>/', v.prestamos_actualizar, name='prestamos.actualizar'),
]
