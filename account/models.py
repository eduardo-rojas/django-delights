from django.db import models
from django.conf import settings

# Model: Profile
class Profile(models.Model):
    # Fields
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="inventory/%Y/%m/%d")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200)
    
    def __str__(self):
        return f'Profile of {self.first_name} {self.last_name}'