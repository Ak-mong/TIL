
import { createApp } from 'vue'
import { PiniaVuePlugin, createPinia } from 'pinia'
import App from './App.vue'
import { createPersistedState } from 'pinia-plugin-persistedstate'
const app = createApp(App)

// pinia
const pinia = createPinia()
pinia.use(createPersistedState)
// app.use(createPinia())
app.use(pinia)

app.mount('#app')
