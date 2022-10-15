from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ['user',  'date_of_birth', 'photo']
    list_filter = ['user', 'date_of_birth']
    prepopulated_fields = {'slug': ('user',  )}

