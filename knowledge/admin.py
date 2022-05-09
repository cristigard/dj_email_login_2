from django.contrib import admin
from .models import Manufacturer, Category, Equipment, Error

# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(Category)
admin.site.register(Equipment)
admin.site.register(Error)
