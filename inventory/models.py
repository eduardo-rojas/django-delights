from django.db import models

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
    


    

