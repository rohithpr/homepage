import pytest

from ..factories import CollectionFactory, ItemFactory
from ..models import Collection, Item

pytestmark = pytest.mark.django_db


def test_item___str__():
    item = ItemFactory()
    assert f"{item.key}::{item.row}::{item.collection.key}" == item.__str__()


def test_collection___str__():
    collection = CollectionFactory()
    assert f"{collection.key}::{collection.column}::{collection.row}" == collection.__str__()
