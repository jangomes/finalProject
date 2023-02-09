from rest_framework import serializers

from .models import Brand, Category, Product, ProductDetails

# this is going to serialize the data from the models and send it to the frontend


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    # this links the brand and category to the product
    brand = BrandSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = "__all__"


class ProductDetailsSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductDetails
        fields = "__all__"
