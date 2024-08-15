from django.contrib import admin
from .models import Contact,Team,MenuCategory,MenuItem
admin.site.register((Contact,Team,MenuCategory,MenuItem))

# Register your models here.
