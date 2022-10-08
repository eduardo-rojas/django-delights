from django.contrib import admin
from .models import Ingredient

# Register Ingredient model to admin site
@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = [
        'name' , 
        'quantity' , 
        'unit_price' , 
        'unit' 
    ]
