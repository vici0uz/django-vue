<template>
  <div class="pt-5">
    <form @submit.prevent="create" method="post">
      <div class="form-group">
        <label for="nombre">Libro</label>
        <validation-provider rules="required" v-slot="{ errors }">
          <input
            type="text"
            name="nombre"
            class="form-control"
            v-model="libro.nombre"
            placeholder="Ingrese un nombre"/>
            <span>{{ errors[0] }}</span>
        </validation-provider>
      </div>
      <div class="form-group">
        <label for="autor">Autor</label>
        <v-select v-model="libro.autor" label="nombre"  :reduce="autor => autor.id" :options="autores"/>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>
<script>
import vSelect from 'vue-select'
import { ValidationProvider, extend } from 'vee-validate'
import { required } from 'vee-validate/dist/rules'
import axios from 'axios'
extend('required', {
  ...required,
  message: 'El campo s xD'
})
export default{
  name: 'Create',
  components: {
    ValidationProvider,
    vSelect
  },
  data () {
    return {
      libro: {
        nombre: ''
      },
      autores: [],
      submitted: false
    }
  },
  mounted () {
    this.getAutores()
  },
  methods: {
    create: function (e) {
      /* axios.post('https://django.xiton.net/api.libros', this.libro)
        .then(response => {
          this.$router.push('/')
        }) */
      ValidationProvider.validate('nombre', 'required').then(result => {
        if (result.isvalid) {
          this.submitted = true
          axios.post('https://django.xiton.net/api.libros', this.libro)
            .then(response => {
              this.$router.push('/')
            })
        }
      })
    },
    getAutores: function () {
      axios.get('https://django.xiton.net/api.autores')
        .then(response => {
          this.autores = response.data
        })
    }
  }
}
</script>
