from inventories.forms import AdminInvetoryForm
from suppliers.models import Supplier


def test_admin_inventory_form(db):
    """
    AdminInvetoryForm should automatically generate sku for the inventory
    """
    supplier = Supplier.objects.create(name="test_supplier")

    data = {
        "name": "test",
        "description": "test",
        "note": "test",
        "stock": 0,
        "supplier": supplier.pk,
    }

    form = AdminInvetoryForm(data=data)
    assert form.is_valid()

    inventory = form.save(commit=True)

    # The SKU should have been generated automatically
    assert inventory.sku
