from django.shortcuts import render
from django. http import HttpResponse, JsonResponse
# Create your views here.

def holamundo(request):
    return HttpResponse("Hola mundo")

def holaapi(request):
    data = {
        'test': 'test1'
    }
    return JsonResponse(data, safe = False)