from django.urls import path
from .views import create, list_many, list_one, details, update, delete
from .views import create_courier_perf, list_couriers_perf, perf_detail, update_courier_perf, delete_courier_perf


urlpatterns = [
    path("create", create, name="create"),
    path("list_many", list_many, name="list_many"),
    path("list_one", list_one, name="list_one"),
    path('details/<int:pk>/', details, name='details'),
    path("update/<int:pk>/", update, name="update"),
    path("delete/<int:pk>/", delete, name="delete"),
    path("create_courier_perf", create_courier_perf, name="create_courier_perf"),
    path("list_couriers_perf", list_couriers_perf, name="list_couriers_perf"),
    path('perf_detail/<int:pk>/', perf_detail, name='perf_detail'),
    path("update_courier_perf/<int:pk>/", update_courier_perf, name="update_courier_perf"),
    path("delete_courier_perf/<int:pk>/", delete_courier_perf, name="delete_courier_perf"),
]
