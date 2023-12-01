from django.views.generic import TemplateView
from rest_framework import generics

from .models import Inventory
from .serializers import InventorySerializer


class APIListInventoryView(generics.ListAPIView):
    """
    Returns list of available inventories
    """

    serializer_class = InventorySerializer

    def get_queryset(self):
        # If `name` exist on url query param, do a case insensitive filter by name
        if name := self.request.GET.get("name"):
            return Inventory.objects.filter(name__icontains=name).select_related(
                "supplier"
            )
        return Inventory.objects.select_related("supplier").all()


class ListInventoryView(TemplateView):
    """
    Display a list.html template. This template would have a JS script
    to call the above views.
    """

    template_name = "inventories/list.html"
