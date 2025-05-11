from django.db import models
from order.models import Order

# Create your models here.


class Fulfilment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    centre_location = models.CharField(max_length=100)
    picking_status = models.CharField(max_length=50)
    # packing_slip = models.FileField(upload_to='packing_slips/')
    packaging_type = models.CharField(max_length=50)
    stock_allocated = models.BooleanField(default=False)
    sla_tracker = models.DurationField()
    internal_notes = models.TextField()
    courier_handoff_status = models.CharField(max_length=50)

    def __str__(self):
        return self.centre_location
