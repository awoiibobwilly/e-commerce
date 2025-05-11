from django.urls import path
from .views import create, list_many, list_one, details, update, delete
from .views import create_order_item, list_order_items, get_order_item, order_item_detail, update_order_item, delete_order_item


urlpatterns = [
    path("create", create, name="create"),
    path("list_many", list_many, name="list_many"),
    path("list_one", list_one, name="list_one"),
    path('details/<int:pk>/', details, name='details'),
    path("update/<int:pk>/", update, name="update"),
    path("delete/<int:pk>/", delete, name="delete"),
    path("create_order_item", create_order_item, name="create_order_item"),
    path("list_order_items", list_order_items, name="list_order_items"),
    path("get_order_item", get_order_item, name="get_order_item"),
    path('order_item_detail/<int:pk>/', order_item_detail, name='order_item_detail'),
    path("update_order_item/<int:pk>/", update_order_item, name="update_order_item"),
    path("delete_order_item/<int:pk>/", delete_order_item, name="delete_order_item"),
]
