from django.shortcuts import render
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.views.generic import  ListView
from django.views.generic.edit import CreateView, DeleteView,  UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


@login_required
def menu(request):
    
    menu_items = MenuItem.objects.all()
    recipie_requirements = RecipeRequirement.objects.all()
    context = { "menu_items": menu_items,
                "recipie_requirements": recipie_requirements}
    return render(request, 'inventory/menu.html', context)

# CRUD Section ------

# Ingredient: CRUD class-based views

class IngredientList(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "inventory/ingredient/ingredient_list.html"

class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = "inventory/ingredient/ingredient_create_form.html"
    fields = ["name", "quantity", "unit_price",  "unit"]
    success_url = "/inventory/ingredient/list"

class IngredientUpdate(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = "inventory/ingredient/ingredient_update_form.html"
    fields = ["name", "quantity", "unit_price",  "unit"]
    success_url = "/inventory/ingredient/list"

class IngredientDelete(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient/ingredient_delete_form.html"
    success_url = "/inventory/ingredient/list"

# MenuItem: CRUD class-based views

class MenuItemList(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "inventory/menuitem/menuitem_list.html"

class MenuItemCreate(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name = "inventory/menuitem/menuitem_create_form.html"
    fields = ["title", "price", "image"]
    success_url = "/inventory/menuitem/list"

class MenuItemUpdate(LoginRequiredMixin, UpdateView):
    model = MenuItem
    template_name = "inventory/menuitem/menuitem_update_form.html"
    fields = ["title", "price", "image"]
    success_url = "/inventory/menuitem/list"

class MenuItemDelete(LoginRequiredMixin, DeleteView):
    model = MenuItem
    template_name = "inventory/menuitem/menuitem_delete_form.html"
    success_url = "/inventory/menuitem/list"

# RecipeRequirement: CRUD class-based views

class RecipeRequirementList(LoginRequiredMixin, ListView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement/reciperequirement_list.html"

class RecipeRequirementCreate(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement/reciperequirement_create_form.html"
    fields = ["quantity", "menu_item", "ingredient"]
    success_url = "/inventory/reciperequirement/list"

class RecipeRequirementUpdate(LoginRequiredMixin, UpdateView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement/reciperequirement_update_form.html"
    fields = ["quantity", "menu_item", "ingredient"]
    success_url = "/inventory/reciperequirement/list"

class RecipeRequirementDelete(LoginRequiredMixin, DeleteView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement/reciperequirement_delete_form.html"
    success_url = "/inventory/reciperequirement/list"

# Purchase: CRUD class-based views

class PurchaseList(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "inventory/purchase/purchase_list.html"

class PurchaseCreate(LoginRequiredMixin, CreateView):
    model = Purchase
    template_name = "inventory/purchase/purchase_create_form.html"
    fields = ["menu_item",  "total_price",  "profile"]
    success_url = "/inventory/purchase/list"

class PurchaseUpdate(LoginRequiredMixin, UpdateView):
    model = Purchase
    template_name = "inventory/purchase/purchase_update_form.html"
    fields = ["menu_item",    "profile"]
    success_url = "/inventory/purchase/list"

class PurchaseDelete(LoginRequiredMixin, DeleteView):
    model = Purchase
    template_name = "inventory/purchase/purchase_delete_form.html"
    success_url = "/inventory/purchase/list"

