from django.shortcuts import render
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.views.generic import  ListView
from django.views.generic.edit import CreateView, DeleteView,  UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.db.models import Sum
from decimal import Decimal
import math

# Display Restaurant Menu
@login_required
def menu(request):
    
    menu_items = MenuItem.objects.all()
    recipie_requirements = RecipeRequirement.objects.all()
    context = { "menu_items": menu_items,
                "recipie_requirements": recipie_requirements}
    return render(request, 'inventory/menu.html', context)

# Display total revenue, total cost of ingredients used 
# and total profit(revenue - cost)
@login_required
def revenue_report(request):

    #------ Total Revenue ------
    total_revenue = Purchase.objects.aggregate(Sum('total_price'))
    total_revenue = float(total_revenue['total_price__sum'])

    #------ Total cost of ingredients ------

    #purchase_menu_items_ids = Purchase.objects.values_list('menu_item', flat=True) 
    total_cost = 0
    menu_item_total_cost = 0

    # 1. Obtain total sells per Menu Item
    purchases = Purchase.objects.all().values('menu_item').annotate(total=Count("menu_item"))
	#Example Query : <QuerySet [{'menu_item': 1, 'total': 2}, {'menu_item': 2, 'total': 1}]>
    
    # 2. Obtain total price per Menu Item (sum price of each ingredient)
	# ----------------
    for index in range(len(purchases)):
        # Multiply each menu item total price by the times it was sold
        if menu_item_total_cost > 0 :
            total_cost += menu_item_total_cost * purchases[index]['total']
        # Variable menu_item_total_cost represents the sum of the price
        # of all required ingredients per menu item
        menu_item_total_cost = 0
        # menu_item_id is used to query all ingredients per recipie
        menu_item_id = purchases[index]['menu_item']
        recipe_ingredients = RecipeRequirement.objects.filter(menu_item= menu_item_id)
        # Example Query: <QuerySet [<RecipeRequirement: Recipe for Django Djaffa Cake with ingredient Flour>, 
	    # 			<RecipeRequirement: Recipe for Django Djaffa Cake with ingredient Large Egg>, 
	    # 			<RecipeRequirement: Recipe for Django Djaffa Cake with ingredient Cane Sugar>, 
	    # 			<RecipeRequirement: Recipe for Django Djaffa Cake with ingredient Milk Chocolate>,
	    # 			<RecipeRequirement: Recipe for Django Djaffa Cake with ingredient Orange Jelly>]>	
	    # For loop to obtain total price for a Menu Item per ingredient, 
        # considering quantity of each ingredient per recipie
        for item in recipe_ingredients:
            ingredient_price = item.quantity * float(item.ingredient.unit_price)
            menu_item_total_cost += ingredient_price

    # Total Profit ------
    profit = total_revenue - total_cost
    # Context variable
    context = { "total_revenue":  '${:,.2f}'.format(total_revenue),
                "total_cost":  '${:,.2f}'.format(total_cost),
                "profit": '${:,.2f}'.format(profit)}
    
    return render(request, 'inventory/revenue_report.html', context)

# ------ CRUD Section ------

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
    fields = ["menu_item",   "profile"]
    success_url = "/inventory/purchase/list"

# Purchase Update View

class PurchaseDelete(LoginRequiredMixin, DeleteView):
    model = Purchase
    template_name = "inventory/purchase/purchase_delete_form.html"
    success_url = "/inventory/purchase/list"

