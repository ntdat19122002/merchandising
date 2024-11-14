import {h, createApp} from 'vue/dist/vue.esm-bundler'
import App from './App.vue'
import {Redirect} from '@shopify/app-bridge/actions'
import 'ant-design-vue/dist/antd.css'
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
    if (url.searchParams.get('password_master') == window.pv_current_time) {
        app.mount('#product_variant-app')
    }
} else {
    const appBridge = createAppBridge({
        apiKey: window.pv_settings.k,
        host: new URLSearchParams(location.search).get("host"),
        forceRedirect: true
    })
    let redirect_element = document.getElementById('variant-redirect')
    if (redirect_element) {
        if (typeof (window.pv_redirect) !== 'undefined') {
            const redirectAppBridge = Redirect.create(appBridge)
            redirectAppBridge.dispatch(Redirect.Action.REMOTE, window.pv_redirect)
        }
    }
    appBridge.getState().then(() => {
        app.mount('#product_variant-app')
    })
}

window.pv_current_time = Date.now()

