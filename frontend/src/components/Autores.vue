<template>
<div class="pt-5">
  <div v-if="autores && autores.length > 0">
    <div class="card mb-3" v-for="(autor) of autores" v-bind:key="autor.id">
      <div class="row no-gutters">
        <div class="col-md-4">
          <svg class="bd-placeholder-img" width="200" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail"><title>{{ autor.nombre }}</title><rect width="100%" height="100%" fill="#55595c"/><text x="50%" y="50%" fill="#eceeef" dy=".3em">{{ autor.nombre.charAt(0) }}</text></svg>
        </div>
        <div class="col-md-8">
          <div class="card-body">
            <div class="card-title">{{ autor.nombre}}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'Autores',
  data () {
    return {
      autores: []
    }
  },
  mounted () {
    this.all()
  },
  methods: {
    all: function () {
      axios.get('https://django.xiton.net/api.autores')
        .then(response => {
          this.autores = response.data
        })
    }
  }
}
</script>
