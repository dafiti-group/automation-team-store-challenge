from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.orm import create_schema

from .models import Product

router = Router()

ProductSchema = create_schema(Product)


@router.get("/products", response=List[ProductSchema])
def list_products(request):
    qs = Product.objects.all()
    return qs


@router.get("/products/{id}", response=ProductSchema)
def get_product(request, id: int):
    product = get_object_or_404(Product, id=id)
    return product
