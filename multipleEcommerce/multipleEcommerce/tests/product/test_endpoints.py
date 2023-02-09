import json

import pytest

pytestmark = pytest.mark.django_db


class TestCategoryEndpoints:
    endpoints = "/api/category/"

    def test_category_get(self, category_factory, api_client):
        # Arrange (I created 4 new records in the database)
        category_factory.create_batch(4)
        response = api_client.get(self.endpoints)

        assert response.status_code == 200

        # the data base return is in a json format
        # we parse the json string and covert it to a python dictionary we count the length
        # of the dictionary and it indicate the amount of data that is return for our request
        assert len(json.loads(response.content)) == 4


class TestProductEndpoints:
    endpoints = "/api/product/"

    def test_product_get(self, product_factory, api_client):
        product_factory.create_batch(4)
        response = api_client.get(self.endpoints)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4


class TestBrandEndpoints:
    endpoints = "/api/brand/"

    def test_brand_get(self, brand_factory, api_client):
        brand_factory.create_batch(4)
        response = api_client.get(self.endpoints)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4
