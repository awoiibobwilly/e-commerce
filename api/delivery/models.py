from django.db import models
from order.models import Order
from courier.models import Courier

# Create your models here.


class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50)
    route_details = models.TextField()
    eta = models.DateTimeField()
    # proof_of_delivery = models.ImageField(upload_to='proofs/')
    failure_reason = models.TextField(blank=True, null=True)
    reattempt_date = models.DateTimeField(blank=True, null=True)
    customer_rating = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.order
