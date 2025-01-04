import {h, createApp} from 'vue/dist/vue.esm-bundler'
import App from './App.vue'
import 'ant-design-vue/dist/antd.css'


let app = createApp({
    name: 'App',
    render: () => {
        return h(App)
    }
})

app.mount('#merchandising-banner-app')

