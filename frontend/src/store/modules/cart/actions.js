import Cart from "../../../apis/Cart";

export const addProductToCart = ({ commit, dispatch }, { product, quantity, user }) => {
    dispatch('addNotification', {
        type: 'success',
        message: 'Product added to cart.'
    }, { root: true });

    Cart.store({
        product_id: product.id,
        quantity,
        user_id: user.id
    }).then(response => {
        commit('ADD_TO_CART', { ...response.data, id: response.data.id, cartShop: response.data.shop.id , product, quantity });
    })
}

export const getCartItems = ({ commit }) => {
    Cart.all().then(response => {
        commit('SET_CART', response.data);
    })
}

export const removeProductFromCart = ({ commit, dispatch }, cart) => {
    commit('REMOVE_PRODUCT_FROM_CART', cart);

    dispatch('addNotification', {
        type: 'success',
        message: 'Product removed from cart.'
    }, { root: true });

    Cart.delete(cart.id);
}

export const completePurchase = ({ commit, dispatch }, cartShop) => {
    commit('CLEAR_CART_ITEMS');

    dispatch('addNotification', {
        type: 'success',
        message: 'All products removed from cart.'
    }, { root: true });

    Cart.deleteAll(cartShop);
}