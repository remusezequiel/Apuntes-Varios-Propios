################################################################################
from django.shortcuts import render
from django.http import HttpResponse
################################################################################

# Create your views here.

################################################################################
def hola_mundo(request):
    """
    Funcion inicial Hola mundo, la cual en el tutorial se
    encuentra como index en la pagina 7 del pdf
    """
    return HttpResponse("Hola a todos! ¿como estan?")
################################################################################
