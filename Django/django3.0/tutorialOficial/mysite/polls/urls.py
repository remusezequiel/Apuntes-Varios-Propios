################################################################################
from django.urls import path
from . import views
################################################################################

################################################################################
"""
Recordemos que estas urls estan apuntadas a la URLconf del proyecto.
Estas se corresponderan a la url definida en "mysite/urls.py" como:
    path('polls/', include('polls.urls')),
"""
urlpatterns = [
    path('', views.hola_mundo, name='hola_mundo'),
]
################################################################################
