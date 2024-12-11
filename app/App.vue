<template>
    <Layout style="min-height: 100vh">
        <LayoutSider v-model:collapsed="collapsed" collapsible>
            <div class="logo"/>
            <Menu theme="dark" v-model:selectedKeys="menu" mode="inline">
                <MenuItem key="Customer">
                    <PieChartOutlined/>
                    <span>Customer</span>
                </MenuItem>
                <MenuItem key="Journey">
                    <FileOutlined/>
                    <span>Journey</span>
                </MenuItem>
                <MenuItem key="Product">
                    <PieChartOutlined/>
                    <span>Product</span>
                </MenuItem>
                <MenuItem key="Order">
                    <PieChartOutlined/>
                    <span>Order</span>
                </MenuItem>
                <MenuItem key="Review">
                    <PieChartOutlined/>
                    <span>Review</span>
                </MenuItem>
                <MenuItem key="Intergration">
                    <PieChartOutlined/>
                    <span>Intergration</span>
                </MenuItem>
            </Menu>
        </LayoutSider>
        <Layout>
            <LayoutHeader style="background: #fff; padding: 0">

            </LayoutHeader>
            <LayoutContent style="margin: 0 16px">
                <Breadcrumb style="margin: 16px 0">
<!--                    <BreadcrumbItem>{{ menu[0] }}</BreadcrumbItem>-->
                </Breadcrumb>
                <div :style="{ padding: '24px', background: '#fff', minHeight: '360px' }">
                    <Customer v-if='menu[0] == "Customer"'/>
                    <Journey v-if="menu[0] == 'Journey'"/>
                    <Product v-if="menu[0] == 'Product'"/>
                    <Order v-if="menu[0] == 'Order'"/>
                    <Review v-if="menu[0] == 'Review'"/>
                    <Intergration v-if="menu[0] == 'Intergration'"> </Intergration>
                </div>
            </LayoutContent>
            <LayoutFooter style="text-align: center">
                Thank you for using this app, upgrade here to use more!
            </LayoutFooter>
        </Layout>
    </Layout>
</template>

<script>
import {
    PieChartOutlined,
    DesktopOutlined,
    UserOutlined,
    TeamOutlined,
    FileOutlined,
} from '@ant-design/icons-vue';
import {
    Layout,
    LayoutContent,
    LayoutFooter,
    LayoutHeader,
    LayoutSider,
    Menu,
    MenuItem,
    Breadcrumb,
    BreadcrumbItem
} from "ant-design-vue";
import CustomerAction from "/components/Pixel/CustomerAction.vue"
import Customer from "./views/Customer/Customer.vue"
import Order from "/views/OrderManagement/Order.vue"
import Journey from "/views/Journey/Jouney.vue"
import Product from "/views/Product/Product.vue"
import Review from "/views/ReviewManagement/Review.vue"
import Intergration from "/views/Intergration/Intergration.vue"

export default {
    components: {
        CustomerAction, Customer, Order, Journey, Review,Product,Intergration,
        Menu, MenuItem, Layout, LayoutSider, LayoutHeader, LayoutContent, LayoutFooter, Breadcrumb, BreadcrumbItem,
        PieChartOutlined,
        DesktopOutlined,
        UserOutlined,
        TeamOutlined,
        FileOutlined,
    },
    data() {
        return {
            collapsed: false,
            menu: ['Customer'],
        };
    },
};
</script>
<style scoped>
.logo {
    height: 32px;
    margin: 16px;
    background: rgba(255, 255, 255, 0.3);
}

.site-layout .site-layout-background {
    background: #fff;
}

[data-theme='dark'] .site-layout .site-layout-background {
    background: #141414;
}
</style>