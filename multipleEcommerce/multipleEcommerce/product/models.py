from django.core.exceptions import ValidationError
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from .fields import OrderField

# Create your models here, they are going to be used to create a file of what is
#  expected to be created at the database.


class ActiveQueryset(models.QuerySet):
    def isactive(self):
        return self.filter(is_active=True)


class Category(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=255)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    objects = ActiveQueryset.as_manager()

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    objects = ActiveQueryset.as_manager()

    # this use the name used in the input in the front end
    # if you don't use this, the name will be object 1, object 2, etc
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True)
    donator_Name = models.CharField(max_length=100)
    donator_contact = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    objects = ActiveQueryset.as_manager()

    def __str__(self):
        return self.name


class ProductDetails(models.Model):
    is_active = models.BooleanField(default=False)
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_details")
    order = OrderField(unique_for_field="product", blank=True)
    objects = ActiveQueryset.as_manager()

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        qs = ProductDetails.objects.filter(product=self.product)
        for obj in qs:
            if self.id == obj.id and self.order == obj.order:
                raise ValidationError("The order must be unique for each product")

    def __str__(self):
        return str(self.order)
