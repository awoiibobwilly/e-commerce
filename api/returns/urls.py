from django.urls import path
from .views import create, list_many, list_one, details, update, delete


urlpatterns = [
    path("create", create, name="create"),
    path("list_many", list_many, name="list_many"),
    path("list_one", list_one, name="list_one"),
    path('details/<int:pk>/', details, name='details'),
    path("update/<int:pk>/", update, name="update"),
    path("delete/<int:pk>/", delete, name="delete"),
]
