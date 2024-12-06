<template>
    <div class="">
        <div class="space-between">
            <h1>
                Product
            </h1>
            <button @click="fetchProduct">
                Fetch product
            </button>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "Review.vue",
    methods:{
        fetchProduct(){
            axios.post('/md/shopify/product/all',{
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