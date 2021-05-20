<template>
  <div class="col-3 mt-3">
    <div class="card h-80 text-left">
      <img class="w-100 cropped" :src="product.image" alt />
      <div class="card-body">
        <h4 class="card-title">
          <router-link :to="{name: 'product', params: {id: product.id}}">{{ product.title }}</router-link>
        </h4>
        <strong>R$ {{ product.price }}</strong>
        <p class="card-text">{{ product.description }}</p>
      </div>
      <div class="px-4 pb-3">
        <button class="btn btn-secondary" @click="addToCart()">Adicionar ao carrinho</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  props: ["product"],

  methods: {
    ...mapActions("cart", ["addProductToCart"]),

    addToCart() {
      this.addProductToCart({
        product: this.product,
        quantity: 1,
        user: this.$store.state.user
      });
    }
  }
};
</script>

<style>
.h-80 {
  height: 80% !important;
}
.cropped {
  height: 50%;
  object-fit: cover;
}
</style>