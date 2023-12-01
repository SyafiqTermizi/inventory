from django.core.validators import MinValueValidator
from django.db import models

from suppliers.models import Supplier

from .utils import generate_unique_sku


class Inventory(models.Model):
    """
    Store inventory data.
    """

    # Store info like Levi's jeans or Nike shoes
    name = models.CharField(max_length=255)

    # Describes the item detail. Eg. XL Brown Levi's jeans
    description = models.CharField(max_length=255)
    note = models.TextField(blank=True)

    # Count the number of available stock
    stock = models.PositiveIntegerField()

    # Unique ID for easy stock keeping.
    sku = models.CharField(max_length=255, unique=True)

    # Supplier that this item belongs to
    supplier = models.ForeignKey(
        to=Supplier,
        related_name="inventories",
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            # Don't allow a supplier to add the same items
            models.UniqueConstraint(
                fields=["supplier", "name", "description"],
                name="unique_supplier_items",
            )
        ]

    def __str__(self) -> str:
        """
        Return name for easy tracking purposes
        """
        return self.name

    @property
    def is_available(self):
        """
        Check if the product is available by checking the product count.

        By adding this method, we don't need to add another `availibility` field
        to the model.
        """

        return self.stock > 0

    @classmethod
    def create(cls, supplier: str, name: str, description: str, note: str, stock: int):
        """
        A shortcut to quickly create an item in the inventory.
        """
        supplier_instance = Supplier.objects.get_or_create(name=supplier)

        sku = generate_unique_sku(
            supplier_name=supplier, product_name=name, product_description=description
        )

        return cls.objects.create(
            name=name,
            description=description,
            note=note,
            stock=stock,
            sku=sku,
            supplier=supplier_instance[0],
        )
