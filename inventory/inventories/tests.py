"""
These tests are not enough but I am running out of time :'(
"""

from django.urls import reverse


def test_redirect_view(client):
    """
    Accessing redirect view should return HTTP 301 since it is a
    permanent redirect
    """

    res = client.get(reverse("inventories:redirect"))
    assert res.status_code == 301


def test_inventory_list_template(client):
    """
    Accessing inventory list view should always return 200
    """

    res = client.get(reverse("inventories:list"))
    assert res.status_code == 200


def test_inventory_list_api(db, client):
    """
    Accessing the inventory list api view should always return 200
    """

    res = client.get(reverse("inventories:list_api"))
    assert res.status_code == 200
