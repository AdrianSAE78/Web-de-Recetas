from django.contrib import admin
from .models import Recetas

# Register your models here.

@admin.register(Recetas)
class RecetasAdmin(admin.ModelAdmin):
    pass

