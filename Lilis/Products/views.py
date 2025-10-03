
from Products.models import Product

def product():
    products = Product.objects.all()
    return products