<template>
    <div :style="{fontSize: `${label_size}px`}" style="display: flex" class="pv-title-heading">
            <div style="white-space: nowrap">{{ name }}</div>
            <div style="white-space: nowrap"
                 v-if="label_show ">
                :&nbsp;{{ selectedVariant }}
            </div>
        </div>
</template>
<script>
export default {
    props:['label_show','label_size','name','label_case','label_value'],
    computed:{
        selectedVariant() {
            switch (this.label_case) {
                case "uppercase":
                    return this.label_value.toUpperCase();
                case "lowercase":
                    return this.label_value.toLowerCase();
                default:
                    return this.label_value;
            }
        },
    }
}
</script>