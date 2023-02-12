from rest_framework import serializers

from .models import Brand, Category, Product, ProductDetails

# this is going to serialize the data from the models and send it to the frontend


class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="name")

    class Meta:
        model = Category
        fields = [
            "category_name",
        ]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = ("id",)


class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        exclude = ("id", "is_active", "product")


class ProductSerializer(serializers.ModelSerializer):
    # this links the brand and category to the product
    brand_name = serializers.CharField(source="brand.name")
    category_name = serializers.CharField(source="category.name")
    product_details = ProductDetailsSerializer(many=True)

    class Meta:
        model = Product
        fields = ("name", "slug", "description", "brand_name", "category_name", "product_details")
