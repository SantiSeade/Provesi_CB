from django.db import models

# Create your models here.

class Product(models.Model):
    sku = models.CharField(max_length=64, unique=True)
    location = models.CharField(max_length=128)
    def __str__(self):
        return self.sku
    
class Withdrawal(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='withdrawals')
    quantity = models.PositiveIntegerField()
    motive = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)