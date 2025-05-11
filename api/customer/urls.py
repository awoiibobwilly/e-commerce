from django.urls import path
from .views import create_customer, list_customers, detail, update_customer, delete_customer


urlpatterns = [
    path("create_customer", create_customer, name="create_customer"),
    path("list_customers", list_customers, name="list_customers"),
    path('detail/<int:pk>/', detail, name='detail'),
    path("update_customer/<int:pk>/", update_customer, name="update_customer"),
    path("delete_customer/<int:pk>/", delete_customer, name="delete_customer"),
]