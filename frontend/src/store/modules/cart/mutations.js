export const ADD_TO_CART = (state, { id, shop, product, quantity, user }) => {
    let productInCart = state.cart.find(item => {
        return item.product.id === product.id;
    });

    if (productInCart) {
        productInCart.quantity += quantity;
        return;
    }

    state.cart.push({
        product,
        quantity,
        id,
        shop,
        user
    })
}

export const SET_CART = (state, cartItems) => {
    state.cart = cartItems;
}

export const REMOVE_PRODUCT_FROM_CART = (state, cart) => {
    var idx = state.cart.indexOf(cart)
    state.cart.splice(idx, 1)
}

export const CLEAR_CART_ITEMS = (state) => {
    state.cart = [];
}