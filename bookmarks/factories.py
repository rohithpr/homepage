import factory
import factory.fuzzy

from .models import Collection, Item


class CollectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Collection

    key = factory.fuzzy.FuzzyText()
    column = factory.fuzzy.FuzzyInteger(0, 5)
    row = factory.fuzzy.FuzzyInteger(0, 5)


class ItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Item

    key = factory.fuzzy.FuzzyText()
    # TODO: Implement custom field to generate URLs
    # https://factoryboy.readthedocs.io/en/latest/fuzzy.html#custom-fuzzy-fields
    value = factory.fuzzy.FuzzyText()

    kind = factory.fuzzy.FuzzyChoice([x[0] for x in Item.Kinds.choices])
    row = factory.fuzzy.FuzzyInteger(0, 5)
    collection = factory.SubFactory(CollectionFactory)
