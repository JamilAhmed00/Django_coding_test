from django.contrib import admin

# Register your models here.
from . import models


admin.site.register(models.Variant)
admin.site.register(models.Product)
admin.site.register(models.ProductImage)
admin.site.register(models.ProductVariant)
admin.site.register(models.ProductVariantPrice)
