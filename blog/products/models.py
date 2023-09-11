from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(default="")
    owner_token = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.title