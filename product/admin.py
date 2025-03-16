from django.contrib import admin
from .models import Product, ProductBrand, ProductCategories, Comment

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductBrand)
admin.site.register(ProductCategories)
admin.site.register(Comment)

