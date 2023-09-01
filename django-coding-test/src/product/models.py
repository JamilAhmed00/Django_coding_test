

from django.db import models
from config.g_model import TimeStampMixin


# Create your models here.
class Variant(TimeStampMixin):
    
    id = models.BigIntegerField(max_length=20, primary_key=True)
    title = models.CharField(max_length=40, unique=True)
    description = models.TextField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(TimeStampMixin):
    
    
    id = models.BigIntegerField(max_length=20, primary_key=True)
    title = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # title = models.CharField(max_length=255)
    # sku = models.SlugField(max_length=255, unique=True)
    # description = models.TextField()


class ProductImage(TimeStampMixin):
    
    id = models.BigIntegerField(max_length=20, primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file_path = models.URLField()
    #thumbnail = tinyint()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # file_path = models.URLField()


class ProductVariant(TimeStampMixin):
    
    
    id = models.BigIntegerField(max_length=20,unique=True,primary_key=True)
    # variant = models.ForeignKey(Variant, )
    variant_title = models.CharField(max_length=255)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    


class ProductVariantPrice(TimeStampMixin):
    
    
    product_variant_one = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True, related_name='product_variant_one')
    product_variant_two = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True, related_name='product_variant_two')
    product_variant_three = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,related_name='product_variant_three')
    price = models.FloatField()
    stock = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)


























