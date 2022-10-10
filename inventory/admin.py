from django.contrib import admin
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase, Profile


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

@admin.register(RecipeRequirement)
class RecipeRequirementAdmin(admin.ModelAdmin):
    list_display = ['menu_item', 'ingredient', 'quantity',
                     'slug', 'created']
    list_filter = ['quantity', 'created']
    prepopulated_fields = {'slug':('menu_item', 'ingredient')}


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['menu_item', 'timestamp', 'total_price', 'slug', 'profile']
    list_filter = ['menu_item', 'timestamp','total_price', 'profile']
    prepopulated_fields = {'slug': ('menu_item', 'profile')}

@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'date_of_birth', 'created', 
                    'updated']
    list_filter = ['user', 'date_of_birth']
    prepopulated_fields = {'slug': ('first_name', 'last_name', 'user'  )}

