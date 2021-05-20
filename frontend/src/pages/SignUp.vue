<template>
    <div>
        <div class="flex">
            <div class="text-center">
                <form @submit.prevent="submitForm" class="form-signin">
                    <img alt="Vue logo" width="120px" src="../assets/logo.png">
                    <h1 class="h3 mb-3 font-weight-normal">Cadastrar</h1>

                    <label for="inputEmail" class="sr-only">Email</label>
                    <input type="email" class="form-control" placeholder="E-mail" required autofocus v-model="username">

                    <label for="inputPassword1" class="sr-only">Password</label>
                    <input type="password" id="inputPassword1" class="form-control" placeholder="Senha" required v-model="password1">

                    <label for="inputPassword2" class="sr-only">Repeat password</label>
                    <input type="password" id="inputPassword2" class="form-control" placeholder="Repetir Senha" required v-model="password2">

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <button class="btn btn-lg btn-primary btn-block" type="submit">Salvar</button>
                </form>
                <router-link :to="{name: 'Login'}">Login</router-link>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'SignUp',
        data() {
            return {
                username: '',
                password1: '',
                password2: '',
                errors: []
            }
        },
        methods: {
            async submitForm() {
                this.errors = []
                if (this.username === '') {
                    this.errors.push('The username is missing')
                }
                if (this.password1 === '') {
                    this.errors.push('The password is too short')
                }
                if (this.password1 !== this.password2) {
                    this.errors.push('The password are not matching')
                }
                if (!this.errors.length) {
                    this.$store.dispatch('setIsLoading', true)
                    const formData = {
                        username: this.username,
                        password: this.password1
                    }
                    await axios
                        .post('/api/v1/users/', formData)
                        .then(() => {
                            this.$router.push('/login')
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
                    
                    this.$store.dispatch('setIsLoading', false)
                }
            }
        }
    }
</script>


<style>
.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: 0 auto;
}
.form-signin .checkbox {
  font-weight: 400;
}
.form-signin .form-control {
  position: relative;
  box-sizing: border-box;
  height: auto;
  padding: 10px;
  font-size: 16px;
}
.form-signin .form-control:focus {
  z-index: 2;
}
.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
#inputPassword1 {
  margin-bottom: -1px;
  border-radius: 0;
}
#inputPassword2 {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
.flex {
  display: flex;
  justify-content: center;
}
</style>