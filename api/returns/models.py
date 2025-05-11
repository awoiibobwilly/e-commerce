from django.db import models
from order.models import Order

# Create your models here.


class Returns(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    condition = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    refund_option = models.CharField(max_length=50)
    pickup_scheduled = models.BooleanField(default=False)
    return_warehouse_location = models.CharField(max_length=100)

    def __str__(self):
        return self.order
