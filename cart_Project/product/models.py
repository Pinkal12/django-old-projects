from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_rate = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    
    def __str__(self):
        return self.product_name
