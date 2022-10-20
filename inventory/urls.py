from django.urls import path 
from . import views

urlpatterns = [
    # Ingredients
    path("ingredient/list", views.IngredientList.as_view(), name="ingredientlist"),
    path("ingredient/create", views.IngredientCreate.as_view(), name="ingredientcreate" ),

]