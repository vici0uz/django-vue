<template>
    <div class="pt-5">
      <v-form ref="form" @submit.prevent="create" method="post">
        <div class="form-group">

          <label for="nombre">Libro</label>
          <validation-provider rules="required" v-slot="{ errors }">
          <input
            type="text"
            name="nombre"
            class="form-control"
            v-model="libro.nombre"
            placeholder="Ingrese un nombre">
            <span>{{ errors[0] }}</span>
          </validation-provider>

        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </v-form>
    </div>
</template>
<script>
import { ValidationProvider } from 'vee-validate'
// import { required } from 'vee-validate/dist/rules'
import axios from 'axios'
export default{
  name: 'Edit',
  components: {
    ValidationProvider
  },
  data () {
    return {
      libro: {
        'nombre': ''
      },
      submited: false
    }
  },
  mounted () {
    axios.get('https://django.xiton.net/api.libros/' + this.$route.params.id)
      .then(response => {
        this.libro = response.data
      })
  }
}
</script>
