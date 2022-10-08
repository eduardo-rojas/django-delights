from django.contrib import admin
from .models import Ingredient, MenuItem

# Register Ingredient model to admin site
@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name' , 'slug', 'quantity' , 
        'unit_price' , 'unit' ]
    prepopulated_fields= {'slug': ('name', )}

@admin.register(MenuItem)
class MenuItemadmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'slug',
                    'created', 'updated']
    list_filter = ['created', 'updated']
    list_editable = ['price']
    prepopulated_fields= {'slug': ('title', )}