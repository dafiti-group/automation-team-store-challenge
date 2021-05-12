from typing import List
from uuid import UUID

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from ninja import Router, Schema

from backend.product.api import ProductSchema
from backend.product.models import Product

from .models import Cart, Shop

router = Router()


class ShopSchema(Schema):
    id: int
    uuid: UUID
    user_id: int
    purchased: bool


class CartSchema(Schema):
    id: int
    uuid: UUID
    shop: ShopSchema
    product: ProductSchema
    quantity: int
    price: float


class CartSchemaIn(Schema):
    product_id: int
    quantity: int
    user_id: int


@router.get("/carts", response=List[CartSchema])
def list_carts(request):
    qs = Cart.objects.filter(shop__purchased=False)
    return qs


@router.post("/carts", response=CartSchema)
def create_cart(request, payload: CartSchemaIn):
    # Get params
    product_id = payload.dict().pop('product_id')
    quantity = payload.dict().pop('quantity')
    user_id = payload.dict().pop('user_id')

    # Instance models
    # Get user
    user = get_object_or_404(User, id=user_id)

    # Get shop
    shop_exists = Shop.objects.filter(user=user, purchased=False).first()
    if shop_exists:
        shop = shop_exists
    else:
        shop = Shop.objects.create(user=user)

    # Get product
    product = get_object_or_404(Product, id=product_id)
    # Get price
    price = product.price

    # Mount dict data
    data = dict(
        shop=shop,
        product=product,
        price=price
    )

    # Search product on cart
    product_exists = Cart.objects.filter(shop=shop, product=product).first()
    if product_exists:
        product_exists.quantity += quantity
        product_exists.save()
        cart = product_exists
    else:
        data['quantity'] = quantity
        # Create Cart
        cart = Cart.objects.create(**data)

    return cart


@router.delete("/carts/{id}")
def delete_cart(request, id: int):
    cart = get_object_or_404(Cart, id=id)
    cart.delete()
    return {"success": True}


@router.put("/shops/{id}/purchase")
def complete_purchase(request, id: int):
    shop = get_object_or_404(Shop, id=id)
    shop.purchased = True
    shop.save()
    return {"success": True}
