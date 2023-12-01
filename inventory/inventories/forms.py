from typing import Any
from django import forms

from .models import Inventory
from .utils import generate_unique_sku


class AdminInvetoryForm(forms.ModelForm):
    """
    Inventory form that is used specifically for admin.

    This form will generate SKU automatically when saving the inventory
    using admin page.
    """

    def save(self, commit) -> Any:
        inventory = super().save(commit=False)
        inventory.sku = generate_unique_sku(
            supplier_name=inventory.supplier.name,
            product_name=inventory.name,
            product_description=inventory.description,
        )
        inventory.save()
        return inventory

    class Meta:
        model = Inventory
        fields = ["name", "description", "note", "stock", "supplier"]
