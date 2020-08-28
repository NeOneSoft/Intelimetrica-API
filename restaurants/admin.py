# Django
from django.contrib import admin

# Models
from .models import Restaurant


@admin.register(Restaurant)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('rating', 'name', 'site', 'email', 'phone', 'street', 'city', 'state', 'lat', 'lng')
