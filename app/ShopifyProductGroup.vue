<template>
    <div v-if="list_product_group.length >0">
        <div v-for="(product_group, index) in list_product_group">
            <div v-if="product_group.status">
                <product-group-component :id="'pv-frontend-block-group' + index"
                                         :name="product_group['name']"
                                         :group_index="index"
                                         style="margin-bottom: 10px"
                                         :list_option_data_img_product_group="list_option_data_img_product_group"
                                         :product_id="product_id"
                                         page="product"
                                         :card_product_info="{}"
                                         :pv_data="product_group"/>
            </div>
        </div>
    </div>
</template>
<script>

import '../static/css/shopify_store.css'
import ProductGroupComponent from "./component/product_group_component.vue";

export default {
    name: "ShopifyProductGroup",
    components: {ProductGroupComponent},
    data() {
        return {
            list_variants: [],
            list_option: null,

            list_variant_img: [],
            max_width: 500,
            default_url_img: '',
            list_input_type: [],

            list_product_group: [],
            list_option_data_img_product_group: {},
            product_id: null
        }
    },
    async mounted() {
        this.product_id = parseInt(nestvairant_product_id)
        try {
            this.list_product_group = JSON.parse(JSON.stringify(nestvariant_product_group_data['list_option']))
            this.list_option_data_img_product_group = JSON.parse(JSON.stringify(nestvariant_product_group_data['list_option_data_img']))

            this.list_product_group = JSON.parse(JSON.stringify(this.list_product_group.filter(group => {
                return this.product_id in group.list_product
            })))
        } catch (e) {

        }
    },
    methods: {}
}
</script>