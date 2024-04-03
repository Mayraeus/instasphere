from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Publicacion

# Create your views here.
def holamundo(request):
    return HttpResponse('hola mundo')

def holaapi(request):
    data = {
        'test' : 'test1'
    }
    return JsonResponse(list (data), safe = False)

def publicaciones(request):
    publicaciones = Publicacion.objects.all().values()
    return JsonResponse(list(publicaciones), safe = False)