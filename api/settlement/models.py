from django.db import models
from vendor.models import Vendor
from order.models import Order

# Create your models here.


class Settlement(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=50)
    settlement_cycle = models.CharField(max_length=50)
    transaction_fees = models.DecimalField(max_digits=10, decimal_places=2)
    payout_method = models.CharField(max_length=50)
    # statement = models.FileField(upload_to='statements/')

    def __str__(self):
        return self.name
