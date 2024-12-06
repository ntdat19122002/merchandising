<template>
    <div v-if="!isReviewed">
        <Rate v-model:value="rating" @change="submitStar"/>
    </div>
    <div v-else>
        Thanks for your feedback!
    </div>
</template>

<script>
import {Rate} from 'ant-design-vue'
import axios from "axios";
export default {
    components:{Rate},
    data(){
        return {
            rating: 0,
            isReviewed: false
        }
    },
    methods:{
        submitStar(){
            this.isReviewed = true
            axios.post('/apps/merchandising/md/review',{
                jsonrpc: 2.0,
                params: {
                    store_url:window.Shopify.shop,
                    product_shopify_id:window.ShopifyAnalytics.meta.product.id,
                    rating:this.rating
                }
            })
        }
    }
}
</script>
<style scoped>

</style>