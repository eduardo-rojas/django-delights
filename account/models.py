from django.db import models
from django.conf import settings


# Model: Profile
class Profile(models.Model):
    # Fields
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="inventory/%Y/%m/%d")
    slug = models.SlugField(max_length=200)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'