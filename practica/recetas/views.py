from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Recetas

# Create your views here.
def index(request):
    recetas = Recetas.objects.order_by('type')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'recetas':recetas}, request))

def specific_recipes(request, receta_id):
    receta = Recetas.objects.get(id=receta_id)
    template = loader.get_template('specific_recipes.html')
    context={
        'receta': receta
    }
    return HttpResponse(template.render(context, request))