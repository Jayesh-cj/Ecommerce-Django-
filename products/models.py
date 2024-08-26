from django.db import models
from base.mdels import BaseModel

# Create your models here.

# Category model 
class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug =models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to='Files\Category')


# Product model 
class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug =models.SlugField(unique=True, null=True, blank=True)
    cagtegory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField()
    product_description = models.TextField()

# Product Images 
class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='Files\Product')