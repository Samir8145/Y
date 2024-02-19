from django.contrib import admin
from .models import Product, Size, Color, Category
admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Category)