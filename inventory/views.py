from django.shortcuts import render
from .models import Ingredient
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView





class IngredientList(ListView):
    model = Ingredient
    template_name = "inventory/ingredient_list.html"

class IngredientCreate(CreateView):
    model = Ingredient
    template_name = "inventory/ingredient_create_form.html"
    fields = ["name", "quantity", "unit_price",  "unit"]
    success_url = "/inventory/ingredient/list"

