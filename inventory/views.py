from django.shortcuts import render
from .models import Ingredient
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView




# Ingredient CRUD class-based views

class IngredientList(ListView):
    model = Ingredient
    template_name = "inventory/ingredient/ingredient_list.html"

class IngredientCreate(CreateView):
    model = Ingredient
    template_name = "inventory/ingredient/ingredient_create_form.html"
    fields = ["name", "quantity", "unit_price",  "unit"]
    success_url = "/inventory/ingredient/list"

class IngredientUpdate(UpdateView):
    model = Ingredient
    template_name = "inventory/ingredient/ingredient_update_form.html"
    fields = ["name", "quantity", "unit_price",  "unit"]
    success_url = "/inventory/ingredient/list"

class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient/ingredient_delete_form.html"
    success_url = "/inventory/ingredient/list"


