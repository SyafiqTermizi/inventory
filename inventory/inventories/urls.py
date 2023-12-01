from django.urls import path

from .views import APIListInventoryView, ListInventoryView

app_name = "inventories"
urlpatterns = [
    path("api/inventory", APIListInventoryView.as_view(), name="list_api"),
    path("inventory", ListInventoryView.as_view(), name="list"),
]
