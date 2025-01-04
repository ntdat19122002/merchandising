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
        <div>
            <Table :dataSource="customerDataSource" :columns="columns"/>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import {Table} from 'ant-design-vue'

export default {
    components: {Table},
    data() {
        return {
            customerDataSource:[],
            columns: [
                {
                    title: 'Email',
                    dataIndex: 'email',
                    key: 'email',
                },
                {
                    title: 'Phone',
                    dataIndex: 'phone',
                    key: 'phone',
                },
                {
                    title: 'IP',
                    dataIndex: 'ip',
                    key: 'ip',
                },
                {
                    title: 'Order',
                    dataIndex: 'order',
                    key: 'order',
                },
                {
                    title: 'Total spend',
                    dataIndex: 'total_spend',
                    key: 'total_spend',
                },
            ],
        }
    },
    methods: {
        connectPixel() {
            axios.post('/pixel/connect', {
                jsonrpc: 2.0,
                params: {
                    store_url: window.md_settings.store_url
                }
            })
        }
    },
    mounted() {
        axios.get('/md/customer',{
            params:{
                store_url: window.md_settings.store_url
            }
        })
            .then((res) => {
                for (let customer of res.data.customer_data){
                    this.customerDataSource.push({
                        email: customer.email ? customer.email : 'Unkown',
                        phone: customer.phone ? customer.phone : 'Unkown',
                        order: customer.order,
                        total_spend: customer.total_spend
                    })
                }
            })
    }
}
</script>

<style scoped>

</style>