from django.urls import path
from .views import create_delivery, list_deliveries, detail, update_delivery, delete_delivery


urlpatterns = [
    path("create_delivery", create_delivery, name="create_delivery"),
    path("list_deliveries", list_deliveries, name="list_deliveries"),
    path('detail/<int:pk>/', detail, name='detail'),
    path("update_delivery/<int:pk>/", update_delivery, name="update_delivery"),
    path("delete_delivery/<int:pk>/", delete_delivery, name="delete_delivery"),
]