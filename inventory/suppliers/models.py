from django.db import models


class Supplier(models.Model):
    """
    Store supplier data.
    """

    name = models.CharField(
        max_length=255,
        # Since we don't have other identifier, `name` should be unique
        unique=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """Return name for easy tracking purposes"""
        return self.name
