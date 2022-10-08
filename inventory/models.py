from django.db import models

# Ingredient model
class Ingredient(models.Model):

    name = models.CharField(max_length=30)
    quantity = models.FloatField()
    unit_price = models.FloatField()
    unit = models.CharField(max_length=30)

    # Meta attributes to order ingredients by name. Database Index for better performance
    class Meta:
        ordering = [ 'name']
        indexes = [
            models.Index(fields=['name'])
        ]
    
    # String method returns ingredient instance name
    def __str__(self):
        return self.name
    



