<template>
  <Layout style="min-height: 100vh">
    <LayoutSider v-model:collapsed="collapsed" collapsible>
      <div class="logo" />
      <Menu theme="dark" v-model:selectedKeys="selectedKeys" mode="inline">
        <MenuItem key="1">
          <PieChartOutlined />
          <span>Option 1</span>
        </MenuItem>
        <MenuItem key="9">
          <FileOutlined />
          <span>File</span>
        </MenuItem>
      </Menu>
    </LayoutSider>
    <Layout>
      <LayoutHeader style="background: #fff; padding: 0" >

      </LayoutHeader>
      <LayoutContent style="margin: 0 16px">
        <Breadcrumb style="margin: 16px 0">
          <BreadcrumbItem>User</BreadcrumbItem>
          <BreadcrumbItem>Bill</BreadcrumbItem>
        </Breadcrumb>
        <div :style="{ padding: '24px', background: '#fff', minHeight: '360px' }">
          <CustomerAction/>
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
import {Layout, LayoutContent, LayoutFooter, LayoutHeader, LayoutSider, Menu, MenuItem, Breadcrumb, BreadcrumbItem} from "ant-design-vue";
import CustomerAction from "/components/Pixel/CustomerAction.vue"
export default {
  components: {
      CustomerAction,
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
      selectedKeys: ['1'],
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