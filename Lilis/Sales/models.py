from django.db import models
from Products.models import Product, Batch
from Accounts.models import Profile

#Lista de Precios - No existe en el modelo hay que modificarlo otra vez
class PriceList(models.Model):
    """
    La historia de usuario CST-US02 pide listas para definir precios por cliente
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

#Precio de la lista- No existe en el modelo hay que modificarlo otra vez
class Price(models.Model):
    price_list = models.ForeignKey(PriceList, on_delete=models.CASCADE, related_name="prices")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.product.name} en {self.price_list.name} tiene un valor de: {self.unit_price}"


class Client(models.Model):
    bussiness_name = models.CharField(max_length=100)
    rut = models.CharField(max_length=20, unique=True)
    email = models.EmailField(null=True, blank=True)
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    max_debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_suspended = models.BooleanField(default=False)
    #price_list lo pide la historia de usuario O2C-001
    price_list = models.ForeignKey(PriceList, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.bussiness_name} - {self.rut}'

#Pedido   
class Order(models.Model):
    STATUS_CHOICES = [
        ('Pendiente'),
        ('En Proceso'),
        ('Completado'),
        ('Cancelado'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendiente')
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Orden #{self.id} creada por {self.client.bussiness_name}"

#DetallePedido
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.order

class Movement(models.Model):
    MOVEMENT_TYPES = [
        ("Ingreso"),
        ("Salida"),
        ("Transferencia"),
        ("Ajuste")
    ]

    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    movement_type = models.CharField(max_length=20, choices=MOVEMENT_TYPES)

class Location (models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    total_area = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    location = models.ForeignKey("Location", on_delete=models.PROTECT, related_name="warehouses")

    def __str__(self):
        return f'{self.name} - {self.location.name}'