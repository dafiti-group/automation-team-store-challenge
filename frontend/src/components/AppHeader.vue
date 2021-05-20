<template>
  <div>
    <nav class="navbar navbar-expand navbar-dark bg-dark">
      <div class="container">
        <div class="nav navbar-nav">
          <router-link to="/" class="nav-tem nav-link active">Produtos</router-link>
        </div>

        <div style="display: flex">
          <div class="buttons">
              <template v-if="!$store.state.isAuthenticated">
                  <router-link to="/signup" class="btn btn-success"><strong>Cadastrar</strong></router-link>
                  <router-link to="/login" class="btn btn-light">Login</router-link>
              </template>

              <template v-else>
                <span class="user mr-2">{{ $store.state.user.username }}</span>
                  <router-link to="/dashboard/my-account" class="button is-info">Minha conta</router-link>
              </template>
          </div>
          <div class="dropdown open">
            <button
              class="btn btn-secondary dropdown-toggle"
              type="button"
              id="triggerId"
              data-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="false"
            >{{ cartItemCount }} carrinho</button>
            <div @click="$event.stopPropagation()">
              <mini-cart />
            </div>
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import MiniCart from "./MiniCart";

export default {
  components: { MiniCart },

  computed: {
    ...mapGetters("cart", ["cartItemCount"])
  }
};
</script>

<style>
.buttons {
  margin: auto 8px;
}
.buttons a {
  margin: auto 2px;
}
.user {
  color: white;
}
</style>