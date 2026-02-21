from django.urls import path
from cuentas import views as v

urlpatterns = [
    path('', v.index, name='cuentas.index'),
    path('register/', v.register_usuario, name='cuentas.register'),
    path('login/', v.login_usuario, name='cuentas.login'),
    path('logout/', v.logout_usuario, name='cuentas.logout'),
    path('contacto/', v.contacto, name='cuentas.contacto'),
]