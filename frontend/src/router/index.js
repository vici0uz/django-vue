import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Create from '@/components/Create'
import Edit from '@/components/Edit'
import Autores from '@/components/Autores'
// import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

// export default new Router({
//   routes: [
//     {
//       path: '/',
//       name: 'HelloWorld',
//       component: HelloWorld
//     }
//   ]
// })

export default new Router({
  routes: [
    {
      path: '/',
      redirect: 'index'
    },
    {
      path: '/libro_edit/:id',
      name: 'libro_edit',
      component: Edit
    },
    {
      path: '/libro-create',
      name: 'libro-create',
      component: Create
    },
    {
      path: '/index',
      name: 'index',
      component: Index
    },
    {
      path: '/autores',
      name: 'autores',
      component: Autores
    }

  ]
})
