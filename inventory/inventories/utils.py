from django.utils.text import slugify


def generate_unique_sku(
    supplier_name: str,
    product_name: str,
    product_description: str,
):
    """
    Utility to help generate unique sku by concatinating:
    1. Supplier name
    2. Product name
    3. Product description
    """

    supplier_name = slugify(supplier_name[:100]).upper()
    product_name = slugify(product_name[:55]).upper()
    description = slugify(product_description[:100]).upper()

    return f"{supplier_name}-{product_name}-{description}"
