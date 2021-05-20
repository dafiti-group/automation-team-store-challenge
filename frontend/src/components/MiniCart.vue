<template>
  <div
    class="dropdown-menu p-2"
    style="min-width:320px; right:0; left:auto"
    aria-labelledby="triggerId"
  >
    <div v-for="item in cart" :key="item.product.id">
      <div class="px-2 d-flex justify-content-between">
        <div>
          <strong>{{ item.product.title }}</strong>
          <br />
          {{ item.quantity }} x R$ {{ item.product.price }}
        </div>
        <div>
          <a
            href="#"
            class="badge badge-danger"
            @click.prevent="removeProductFromCart(item)"
          >deletar</a>
        </div>
      </div>
      <hr />
    </div>

    <div class="d-flex justify-content-between">
      <span>Total: <strong>R$ {{ cartTotalPrice }}</strong></span>
      <a v-if="cartShop" href="#" class="btn btn-primary" @click.prevent="completePurchase(cartShop)">Finalizar compra</a>
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from "vuex";

export default {
  computed: {
    ...mapState("cart", ["cart"]),
    ...mapGetters("cart", ["cartTotalPrice"]),
    ...mapGetters("cart", ["cartShop"])
  },

  mounted() {
    this.getCartItems();
  },

  methods: {
    ...mapActions("cart", [
      "removeProductFromCart",
      "completePurchase",
      "getCartItems"
    ])
  }
};
</script>

<style>
</style>