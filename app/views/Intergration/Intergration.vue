<template>
    <div class="">
        <button @click="connectGoogleAds">Connect Google ads</button>
    </div>
</template>

<script>
import axios from "axios";

export default {
    methods:{
        connectGoogleAds(){
            axios.post('/integration/google_ads',{
                jsonrpc: 2.0,
                params: {
                    store_url: window.md_settings.store_url
                }
            })
        }
    }
}
</script>

<style scoped>

</style>