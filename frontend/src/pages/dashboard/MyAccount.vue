<template>
  <div>
    <h1>Minha conta</h1>
    <div>
      <button class="btn btn-danger" @click="logout()">Sair</button>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'MyAccount',
    methods: {
      async logout() {
        await axios
          .post('/api/v1/token/logout/')
          .then(() => {
            console.log('Logged out')
          })
          .catch(error => {
            console.log(JSON.stringify(error))
          })

        axios.defaults.headers.common['Authorization'] = ''
        localStorage.removeItem('token')
        this.$store.dispatch('removeToken')

        this.$router.push('/')
      }
    }
  }
</script>