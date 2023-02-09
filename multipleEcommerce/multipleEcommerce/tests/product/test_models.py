import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(self, category_factory):
        # Create a new entry in the database (Act)
        x = category_factory(name="test_category")
        # bolian expression (Assert) when it's true the test passes
        assert x.__str__() == "test_category"


class TestBrandModel:
    def test_str_method(self, brand_factory):
        # Create a new entry in the database (Act)
        obj = brand_factory(name="test_brand")
        # bolian expression (Assert) when it's true the test passes
        assert obj.__str__() == "test_brand"


class TestProductModel:
    def test_str_method(self, product_factory):
        # Create a new entry in the database (Act)
        x = product_factory(name="test_product")
        # bolian expression (Assert) when it's true the test passes
        assert x.__str__() == "test_product"
