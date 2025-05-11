from django.db import models
from product.models import Product
from vendor.models import SupportTicket
# Create your models here.


class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    loyalty_points = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name


class Wishlist(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer


class CustomerSupport(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ticket = models.ForeignKey(SupportTicket, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer
