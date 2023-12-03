from inventories.models import Inventory
from suppliers.models import Supplier


def test_inventory_create_method_new_supplier(db, create_inventory):
    """
    Inventory.create method should create
    1. A supplier, since its a new one
    2. Inventory
    """
    # Proof that no supplier and inventory in the db
    assert not Inventory.objects.count()
    assert not Supplier.objects.count()

    create_inventory()

    # Inventory.create method should create a supplier and an inventory
    assert Inventory.objects.count() == 1
    assert Supplier.objects.count() == 1


def test_inventory_create_method_existing_supplier(db, create_inventory):
    """
    Inventory.create method should only create an inventory if supplier
    already exist
    """
    supplier_name = "test_supplier"
    supplier = Supplier.objects.create(name=supplier_name)

    # Proof that there's an existing supplier and no inventory in the db
    assert Supplier.objects.count() == 1
    assert not Inventory.objects.count()

    inventory = create_inventory(
        supplier_name=supplier_name,
        stock_count=100,
    )

    # Inventory.create method should create a supplier and an inventory
    assert Inventory.objects.count() == 1
    assert Supplier.objects.count() == 1
    assert inventory.supplier.pk == supplier.pk


def test_inventory_create_method_available(db, create_inventory):
    """
    Inventory create method should return True if stock count is more
    than 0
    """
    inventory = create_inventory()
    assert inventory.is_available


def test_inventory_create_method_not_available(db, create_inventory):
    """
    Inventory create method should return False if stock count is equal to 0
    """
    inventory = create_inventory(stock_count=0)
    assert not inventory.is_available
