from django.contrib import admin

from .forms import AdminInvetoryForm
from .models import Inventory


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ["name", "sku", "stock", "supplier"]
    form = AdminInvetoryForm
