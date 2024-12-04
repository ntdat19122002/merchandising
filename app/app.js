import {h, createApp} from 'vue/dist/vue.esm-bundler'
import App from './App.vue'
import {Redirect} from '@shopify/app-bridge/actions'
import 'ant-design-vue/dist/antd.css'
import '../static/css/main.css'
import {createApp as createAppBridge} from '@shopify/app-bridge'


let app = createApp({
    name: 'App',
    render: () => {
        return h(App)
    }
})

let url = new URL(location.href)
let hasPassword = url.searchParams.has('password_master')

if (hasPassword) {
    if (url.searchParams.get('password_master') == window.md_current_time) {
        app.mount('#merchandising-app')
    }
} else {
    const appBridge = createAppBridge({
        apiKey: window.md_settings.k,
        host: new URLSearchParams(location.search).get("host"),
        forceRedirect: true
    })
    let redirect_element = document.getElementById('variant-redirect')
    if (redirect_element) {
        if (typeof (window.md_redirect) !== 'undefined') {
            const redirectAppBridge = Redirect.create(appBridge)
            redirectAppBridge.dispatch(Redirect.Action.REMOTE, window.md_redirect)
        }
    }
    appBridge.getState().then(() => {
        app.mount('#merchandising-app')
    })
}

window.md_current_time = Date.now()

