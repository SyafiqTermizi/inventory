from django.urls import reverse

from inventories.models import Inventory

def test_redirect_view(client):
    """
    Accessing redirect view should return HTTP 301 since it is a
    permanent redirect
    """

    res = client.get(reverse("inventories:redirect"))
    assert res.status_code == 301


def test_inventory_list_template(client):
    """
    Accessing inventory list view should return 200
    """

    res = client.get(reverse("inventories:list"))
    assert res.status_code == 200


def test_inventory_list_template_query_param(client):
    """
    Accessing inventory list view with a query param
    should always should return 200 even if search param
    does not exist
    """

    res = client.get(f"{reverse("inventories:list")}?name=QbOfpKbTZ6tiibD")
    assert res.status_code == 200


def test_inventory_list_api(db, client):
    """
    Accessing the inventory list api view should always return 200
    even if the data is empty
    """

    res = client.get(reverse("inventories:list_api"))
    assert res.status_code == 200
    assert res.content.decode() == str([])


def test_inventory_detail_view_not_found(db, client):
    """
    Accessing the inventory detail view should return 404 if the data does not
    exist
    """
    res = client.get(reverse("inventories:detail", kwargs={"sku": "thbfxtg9salyjgk"}))
    assert res.status_code == 404


def test_inventory_detail_view_success(db, client):
    """
    Accessing the inventory detail view should return 200 if the data exist
    """
    inventory = Inventory.create(
        supplier="test", name="test", description="test", note="test", stock=10,
    )
    res = client.get(reverse("inventories:detail", kwargs={"sku": inventory.sku}))
    assert res.status_code == 200
