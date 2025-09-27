from django.db import models

class Supplier(models.Model):
    bussiness_name = models.CharField(max_length=100)
    rut = models.CharField(max_length=20, unique=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    trade_terms = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.bussiness_name} - {self.rut}'
    
class RawMaterial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    stock_quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    expiration_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey("Category", on_delete=models.PROTECT, related_name="products")
    min_stock = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    max_stock = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    current_stock = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    expiration_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.sku}'
    