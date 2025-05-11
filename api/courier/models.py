from django.db import models

# Create your models here.


class Courier(models.Model):
    name = models.CharField(max_length=100)
    company_profile = models.TextField()
    # assigned_orders = models.ManyToManyField('Order', blank=True)
    geo_logs = models.TextField()
    vehicle_or_rider = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CourierPerformance(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    on_time_percentage = models.FloatField()
    rating = models.FloatField()

    def __str__(self):
        return self.courier
