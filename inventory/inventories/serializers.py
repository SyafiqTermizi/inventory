from rest_framework import serializers

from .models import Inventory


class InventorySerializer(serializers.ModelSerializer):
    """
    Serializes model data into JSON
    """

    # We want to display supplier's name instead of PK
    supplier = serializers.StringRelatedField()

    class Meta:
        model = Inventory
        fields = [
            "name",
            "supplier",
            "is_available",
        ]
