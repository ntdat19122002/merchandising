<template>
    <div class="">
        <div class="space-between">
            <h1>
                Customer
            </h1>
            <button @click="connectPixel">
                Connect pixel
            </button>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "Review.vue",
    methods:{
        connectPixel(){
            axios.post('/pixel/connect',{
                jsonrpc:2.0,
                params:{
                    store_url: window.md_settings.store_url
                }
            })
        }
    }
}
</script>

<style scoped>

</style>