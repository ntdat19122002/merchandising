<template>
    <div class="banner" @click="redirect_to_product_page" v-if="product_url && product_img">
        <div>
            <img :src="product_img"/>
        </div>
        <div class="md-title">
            See our best seller
        </div>
    </div>
</template>

<script>
import axios from "axios";
import {log} from "../../../../addons/web_editor/static/lib/odoo-editor/test/lib/mocha";

export default {
    data() {
        return {
            product_img: null,
            product_url: null,
        }
    },
    methods:{
      redirect_to_product_page(){
          window.location.href = this.product_url
      }
    },
    mounted() {
        axios.get('/apps/merchandising/md/banner', {
            params: {
                store_url: window.Shopify.shop
            }
        }).then(res => {
            console.log(res.data.product_img)
            this.product_img = res.data.product_img
            this.product_url = res.data.product_url
        })
    }
};
</script>

<style scoped>
.banner {
    cursor: pointer;
    display: flex;
    background: url("https://odoo.website/merchandising/static/images/banner/banner.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    height: 60px;
    align-items: center;
    justify-content: center;
}

.md-title {
    font-size: 20px;
    color: white;
    font-weight: 700;
}

img{
    width: 50px;
    height: 50px;
    margin-right: 10px;
}
</style>
