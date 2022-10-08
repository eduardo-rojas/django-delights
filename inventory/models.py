from django.db import models
from django.conf import settings

# Model: Ingredient
class Ingredient(models.Model):
    # Fields
    name = models.CharField(max_length=30)
    quantity = models.FloatField()
    # Using DecimalField instead of FloatField for monetary fields
    # in order to avoid rounding issues
    unit_price = models.DecimalField(max_digits=10, 
                                    decimal_places=2)
    slug = models.SlugField(max_length=200)
    unit = models.CharField(max_length=30)

    # Meta class with attributes to order ingredients by name
    # Database Index to improve query performance
    class Meta:
        ordering = [ 'name']
        indexes = [
            models.Index(fields=['name'])
        ]
    
    # String method returns readable ingredient instance name
    def __str__(self):
        return self.name
    
# Model: MenuItem
class MenuItem(models.Model):
    # Fields
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, 
                                decimal_places=2)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='inventory/%Y/%m/%d',
                            blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Meta class. Order by title
    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['title']), 
            models.Index(fields=['-created'])
        ]
    
    # String format method
    def __str__(self):
        return self.title
    
# Model: RecipeRequirement
class RecipeRequirement(models.Model):
    # Fields
    quantity = models.FloatField()
    menu_item = models.ForeignKey(MenuItem,
                                on_delete=models.CASCADE,   
                                related_name="menuitem_recipes")
    ingredient = models.ForeignKey(Ingredient,  
                                on_delete=models.CASCADE,
                                related_name="ingredient_recipes")
    slug = models.SlugField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    
    # Meta class. Order by quantity
    class Meta:
        ordering = ['quantity']
        indexes = [
            models.Index(fields=['menu_item']),
            models.Index(fields=['ingredient'])
        ] 
    
    # String format method
    def __str__(self):
        return f'Recipe for {self.menu_item} with ingredient {self.ingredient}'
    
# Model: Purchase
class Purchase(models.Model):
    # Fields
    menu_item = models.ForeignKey(MenuItem,
                                on_delete=models.CASCADE,
                                related_name='purchase_menuitems')
    timestamp = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10,
                                    decimal_places=2)
    slug = models.SlugField(max_length=200)

    # Meta class. Order by total_price
    ordering = ['total_price']
    indexes = [
        models.Index(fields=['menu_item']),
        models.Index(fields=['total_price']),
    ]

    # String format method
    def __str__(self):
        return f'Purchase with id#: {self.id} - Date:{self.timestamp} - Total: ${self.total_price}'
    
# Model: Profile
class Profile(models.Model):
    # Fields
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="inventory/%Y/%m/%d")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    purchase_dispatched = models.ForeignKey(Purchase,
                                        on_delete=models.CASCADE,
                                        related_name='profile_purchase')
    slug = models.SlugField(max_length=200)
    
    def __str__(self):
        return f'Profile of {self.username}'
    



    

