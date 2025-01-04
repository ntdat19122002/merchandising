<template>
    <div v-if="!isReviewed">
        <Rate v-model:value="rating" @change="submitStar"/>
        <div>
            <div class="label">Write your review</div>
            <textarea placeholder="Write your comment here"></textarea>
        </div>
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
textarea {
      width: 100%;
      max-width: 500px;
      height: 150px;
      padding: 10px;
      font-size: 16px;
      font-family: Arial, sans-serif;
      border: 2px solid #ccc;
      border-radius: 5px;
      background-color: #f9f9f9;
      color: #333;
      resize: both; /* Allows resizing in both directions */
      box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    }

    textarea:focus {
      border-color: #007BFF;
      outline: none;
      background-color: #fff;
      box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
    }
</style>