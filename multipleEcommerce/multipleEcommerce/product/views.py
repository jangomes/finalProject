from django.db import connection
from drf_spectacular.utils import extend_schema
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import SqlLexer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from sqlparse import format

from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer

# simple view set to view the categories


class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


# simple view set to view the brands


class BrandViewSet(viewsets.ViewSet):
    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


# simple view set to view the products


class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all().isactive()
    lookup_field = "slug"

    def retrieve(self, request, slug=None):
        serializer = ProductSerializer(
            self.queryset.filter(slug=slug).select_related("category", "brand"), many=True
        )
        data = Response(serializer.data)

        q = list(connection.queries)
        print(len(q))

        # for qs in q:
        #    sqlformatted = format(str(qs["sql"]), reindent=True)
        #    print(highlight(sqlformatted, SqlLexer(), TerminalFormatter()))

        return data

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

    # endpoint: list the products by category I used a filter to return the products by category
    # we will pass a parameter and utilize this parameter to filter the products
    @action(detail=False, methods=["get"], url_path=r"category/(?P<slug>[\w-]+)")
    def list_product_by_category_slug(self, request, slug=None):
        serializer = ProductSerializer(self.queryset.filter(category__slug=slug), many=True)
        return Response(serializer.data)
