<template>
    <div class="banner">
        <select v-model="banner_type">
            <option value="banner_1">Banner 1</option>
            <option value="banner_2">Banner 2</option>
            <option value="banner_3">Banner 3</option>
            <option value="custom">Custom URL</option>
        </select>
        <div class="option">
            <div class="label">Description</div>
            <input type="text">
        </div>
        <div class="option">
            <div class="label">Width</div>
            <input type="text">
        </div>
        <div class="option">
            <div class="label">Height</div>
            <input type="text">
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    data(){
      return{
          banner_type:'banner_1',
          banner_url:''
      }
    },
    methods:{
    }
}
</script>

<style scoped>

</style>