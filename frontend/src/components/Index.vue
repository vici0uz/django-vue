<template>
<div class="pt-5">
  <div v-if="libros && libros.length > 0">
      <div class="card mb-3" v-for="(libro) of libros" v-bind:key="libro.id">
        <div class="row no-gutters">
          <div class="col-md-4">
            <svg class="bd-placeholder-img" width="200" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail"><title>{{ libro.nombre }}</title><rect width="100%" height="100%" fill="#55595c"/><text x="50%" y="50%" fill="#eceeef" dy=".3em">{{ libro.nombre.charAt(0) }}</text></svg>
          </div>
          <div class="col-md-8">
              <div class="card-body">
                  <h5 class="card-title">{{ libro.nombre }}</h5>
                  <p class="card-text">{{ autorLibro(libro.autor) }}</p>
                  <router-link :to="{name: 'libro_edit', params: { id:libro.id }}" class="btn btn-sm btn-primary">Edit</router-link>
                  <!-- <button class="btn btn-danger btn-sm ml-1" v-on:click="deleteSubscription(subscription)">Delete</button> -->
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
  name: 'Index',
  data () {
    return {
      libros: [],
      autores: []
    }
  },
  mounted () {
    this.all()
  },
  methods: {
    all: function () {
      axios.get('https://django.xiton.net/api.libros')
        .then(response => {
          this.libros = response.data
        })
      axios.get('https://django.xiton.net/api.autores')
        .then(response => {
          this.autores = response.data
        })
    },
    autorLibro: function (autorId) {
      console.log(autorId)
      for (const a in this.autores) {
        if (this.autores[a].id === autorId) {
          return this.autores[a].nombre
        }
      }
    }
  }
}
</script>
<style>
p {
  color: green;
}
</style>
