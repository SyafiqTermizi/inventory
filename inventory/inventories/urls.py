from django.urls import path

from .views import (
    APIListInventoryView,
    DetailInventoryView,
    ListInventoryView,
    RedirectToInventoryList,
)

app_name = "inventories"
urlpatterns = [
    path("", RedirectToInventoryList.as_view(), name="redirect"),
    path("api/inventory", APIListInventoryView.as_view(), name="list_api"),
    path("inventory", ListInventoryView.as_view(), name="list"),
    path("inventory/<slug:sku>", DetailInventoryView.as_view(), name="detail"),
]
