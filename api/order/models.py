from django.db import models
from product.models import Product

# Create your models here.


class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_contact = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_instructions = models.TextField(blank=True, null=True)
    # invoice = models.FileField(upload_to='invoices/', null=True, blank=True)

    def __str__(self):
        return self.customer_name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.order
