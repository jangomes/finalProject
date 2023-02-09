import factory

from multipleEcommerce.product.models import Brand, Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    # we are going to generate a random name for the category to not hardcode it
    name = factory.Sequence(lambda n: "Category_%d" % n)


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Sequence(lambda n: "Brand_%d" % n)


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    is_active = True
    name = "test_product"
    description = "test_description"
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
