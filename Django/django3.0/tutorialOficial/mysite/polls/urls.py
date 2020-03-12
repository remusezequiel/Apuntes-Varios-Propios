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
app_name = 'polls'

"""
# Configuracion de urls para vistas no genericas.
# Tengamos en cuenta, que los parametros pasados se haran con "_" y no con "."
# Tambien notemos que primero debemos pasarte el tipo de la variable pasada

urlpatterns = [
    #path('', views.hola_mundo, name='hola_mundo'),
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
"""

# Configuracion de las url utilizando las vistas genericas
# Notemos que en vez de pasarle question_id al slug le pasamos directamente pk

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
################################################################################
