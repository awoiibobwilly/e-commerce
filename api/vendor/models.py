from django.db import models

# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    tin = models.CharField(max_length=20)
    address = models.TextField()
    contact_info = models.CharField(max_length=100)
    payout_status = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SupportTicket(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
