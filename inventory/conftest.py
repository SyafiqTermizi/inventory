import pytest
from inventories.models import Inventory


@pytest.fixture
def create_inventory():
    """
    A fixture that returns a function that creates inventory instance
    """

    def _create_inventory(supplier_name=None, stock_count=None):
        supplier_name = supplier_name or "supplier_name"
        stock_count = stock_count if stock_count is not None else 100

        return Inventory.create(
            supplier=supplier_name,
            name="test",
            description="test",
            note="test",
            stock=stock_count,
        )

    return _create_inventory
