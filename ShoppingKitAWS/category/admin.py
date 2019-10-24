from django.contrib import admin
from category.models import Category, Private_Category, Private_Users
# Register your models here.
admin.site.register(Category)
admin.site.register(Private_Category)
admin.site.register(Private_Users)