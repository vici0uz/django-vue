<template>
<v-app>
  <v-navigation-drawer permanent>
   </v-navigation-drawer>
   <v-app-bar app color="primary" dark>
      <div class="text-center">
    <v-menu bottom left>
      <template v-slot:activator="{ on, attrs }">
        <v-btn dark icon v-bind="attrs" v-on="on">
          <v-icon>mdi-dots-vertical</v-icon>
        </v-btn>
      </template>
      <v-list>
        <v-list-item v-for="(item, index) in items" :key="index">
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </div>
   </v-app-bar>
   <v-main>
    <v-container fluid>
    <div class="row justfiy-content-center">
      <div class="col-md-8">
        <h2><router-link to="/index">Libros</router-link></h2>
        <h2><router-link to="/autores">Autores</router-link></h2>
        <router-link to="/libro-create">Agregar Libro</router-link>
      </div>
    </div>
    <router-view/>
    </v-container>
   </v-main>
  <v-app-footer app></v-app-footer>
</v-app>
</template>
<script>
export default {
  data: () => ({
    name: 'app',
    items: [
      {title: 'Libros'},
      {title: 'Autores'}
    ],
    offset: true
  })
}
</script>
<style>
</style>
