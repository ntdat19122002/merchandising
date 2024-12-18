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
        <div>
            <Table :dataSource="productDataSource" :columns="columns"/>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import {notification, Table} from "ant-design-vue"

export default {
    name: "Review.vue",
    components: {Table},
    data() {
        return {
            productDataSource: [],
            columns: [
                {
                    title: 'Id',
                    dataIndex: 'id',
                    key: 'id',
                },
                {
                    title: 'Shopify id',
                    dataIndex: 'shopify_id',
                    key: 'shopify_id',
                },
                {
                    title: 'Title',
                    dataIndex: 'title',
                    key: 'title',
                },
            ],
        }
    },
    methods: {
        fetchProduct() {
            axios.post('/md/shopify/product/all', {
                jsonrpc: 2.0,
                params: {
                    store_url: window.md_settings.store_url
                }
            })
                .then((res) => {
                    this.productDataSource = JSON.parse(res.data.result).product_data
                    notification['success']({
                        message: 'Judgeme',
                        description:
                          'Fetch products successfully',
                        placement:'bottomRight',
                      });
                })
        }
    },
    mounted() {
        axios.get('/md/shopify/product', {
            params: {
                store_url: window.md_settings.store_url
            }
        })
            .then((res) => {
                this.productDataSource = res.data.product_data
            })
    }
}
</script>

<style scoped>

</style>