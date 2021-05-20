<template>
    <div>
        <div class="flex">
            <div class="text-center">
                <form @submit.prevent="submitForm" class="form-login">
                    <img alt="Vue logo" width="120px" src="../assets/logo.png">
                    <h1 class="h3 mb-3 font-weight-normal">Login</h1>

                    <label for="inputEmail" class="sr-only">Email</label>
                    <input type="email" class="form-control" placeholder="E-mail" required autofocus v-model="username">

                    <label for="inputPassword" class="sr-only">Password</label>
                    <input type="password" id="inputPassword" class="form-control" placeholder="Senha" required v-model="password">

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <button class="btn btn-lg btn-primary btn-block">Entrar</button>
                </form>
                <router-link :to="{name: 'SignUp'}">Cadastre-se</router-link>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'Login',
        data() {
            return {
                username: '',
                password: '',
                errors: []
            }
        },
        methods: {
            async submitForm() {
                this.$store.dispatch('setIsLoading', true)

                axios.defaults.headers.common['Authorization'] = ''
                localStorage.removeItem('token')

                const formData = {
                    username: this.username,
                    password: this.password
                }

                let token

                await axios
                    .post('/api/v1/token/login/', formData)
                    .then(response => {
                        let token = response.data.auth_token

                        this.$store.dispatch('setToken', token)

                        axios.defaults.headers.common['Authorization'] = 'Token ' + token

                        localStorage.setItem('token', token)

                        this.$router.push('/')
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again!')
                        }
                    })

                await axios
                  .get('/api/v1/users/me/', 'Token ' + token)
                  .then(response => {
                    const user = {"id": response.data.id, "username": response.data.username}
                    this.$store.dispatch('setUser', user)
                  })

                this.$store.dispatch('setIsLoading', false)
            }
        }
    }
</script>


<style>
.form-login {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: 0 auto;
}
.form-login .checkbox {
  font-weight: 400;
}
.form-login .form-control {
  position: relative;
  box-sizing: border-box;
  height: auto;
  padding: 10px;
  font-size: 16px;
}
.form-login .form-control:focus {
  z-index: 2;
}
.form-login input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
#inputPassword {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
.flex {
  display: flex;
  justify-content: center;
}
</style>