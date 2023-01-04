from django.contrib import admin
from .models import Product, Category, CategoryProduct
from .models import Picture


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(CategoryProduct)
admin.site.register(Picture)