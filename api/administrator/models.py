from django.db import models
# from django.contrib.auth.models import User
# Create your models here.


class Role(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


# class Role(models.Model):
#     name = models.CharField(max_length=50)
#     permissions = models.TextField()

#     def __str__(self):
#         return self.name


# class SystemSetting(models.Model):
#     timezone = models.CharField(max_length=50)
#     currency = models.CharField(max_length=10)
#     notifications_enabled = models.BooleanField(default=True)

#     def __str__(self):
#         return self.currency


# class AuditLog(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     action = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.user


# class PlatformConfiguration(models.Model):
#     theme = models.CharField(max_length=50)
#     # logo = models.ImageField(upload_to='logos/')

#     def __str__(self):
#         return self.theme


# class APIKey(models.Model):
#     name = models.CharField(max_length=100)
#     key = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name
