<template>
    <div style="gap: 10px; display: flex; flex-direction: column" v-if="pv_data">
        <div v-for="(variant_template_ids, index) in array_variant_template_id">
            <product-variant :option_information="list_option[index]"
                             :list_img="list_img(index)"
                             :position="index"
                             :list_checked_option="list_checked_option"
                             :default_url_img="default_url_img"
                             :input_type="list_input_type[index]"
                             :variant_template_ids="variant_template_ids"
                             :max_width="max_width"
                             :pv_data="get_pv_data(index)"
                             :block_element_selector="block_element_selector"
                             :option_block_selector="option_block_selector"
                             :isConflictTheme="isConflictTheme"
                             :themeData="themeData"/>
        </div>
    </div>
</template>
<script>
import ProductVariant from "./component/product_variant.vue"
import axios from "axios"
import '../static/css/shopify_store.css'

export default {
    name: "Shopify",
    components: {ProductVariant},
    data() {
        return {
            list_variants: [],
            list_checked_option: [],
            list_option: null,
            pv_data: null,
            isConflictTheme: this.$.attrs.data.isConflictTheme,
            themeData: this.$.attrs.data.themeData,
            array_variant_template_id: [],
            list_variant_img: [],
            max_width: 500,
            default_url_img: '',
            list_input_type: [],
            block_element_selector: this.$.attrs.data.block_element_selector,
            option_block_selector: this.$.attrs.data.option_block_selector,

        }
    },
    methods: {
        list_img(option_index) {
            return this.get_list_img(this.list_variants, 0, option_index)
        },
        get_list_img(list_variants_temp, i, option_index) {
            if (i < this.list_option.length - 1) {
                if (i === option_index) {
                    let list_tmp = []
                    for (let j = 0; j < this.list_option[i].values.length; j++) {
                        list_tmp.push(this.get_list_img(list_variants_temp[j], i + 1,option_index))
                    }
                    return list_tmp
                }
                return this.get_list_img(list_variants_temp[this.list_checked_option[i]], i + 1,option_index)
            } else {
                if (i === option_index) {
                    let list_tmp = []
                    for (let j = 0; j < this.list_option[i].values.length; j++) {
                        list_tmp.push(list_variants_temp[j])
                    }
                    return list_tmp
                }
                return list_variants_temp[this.list_checked_option[i]]
            }
        },
        processResponse(res) {
            let array_data = []

            if (nestvariant_theme_settings_value !== null) {
                nestvariant_theme_settings_value.list_option_setting.forEach(option => {
                    let option_object_product = {
                        design_setting: JSON.parse(JSON.stringify(option.design_setting)),
                        option_setting: JSON.parse(JSON.stringify(option.option_setting_product)),
                    }
                    if ('option_setting_color_custom_image' in option) {
                        option_object_product.option_setting_color_custom_image = JSON.parse(JSON.stringify(option.option_setting_color_custom_image))
                    }
                    array_data.push(option_object_product)
                })
            }
            this.pv_data = JSON.parse(JSON.stringify(array_data))

            this.list_option = res.data.options
            this.default_url_img = res.data.images.length > 0 ? res.data.images[0] : 'https://app.nestscale.com/nestprdvariant/static/images/no_image.png'
            let temp_list_variants = [...res.data.variants]
            this.product_id = res.data.id
            const add_list_variants = (i, location) => {
                let list = []
                if (i < res.data.options.length - 1) {
                    for (let j = 0; j < res.data.options[i].values.length; j++) {
                        list.push(add_list_variants(i + 1, [...location, j]))
                    }
                } else {
                    for (let j = 0; j < res.data.options[i].values.length; j++) {
                        if (temp_list_variants.length) {
                            let temp_variant
                            if (location.length == 0) {
                                temp_variant = temp_list_variants.filter(variant => variant.option1 === this.list_option[0].values[j])
                            } else if (location.length == 1) {
                                temp_variant = temp_list_variants.filter(variant =>
                                    variant.option1 === this.list_option[0].values[location[0]]
                                    && variant.option2 === this.list_option[1].values[j]
                                )
                            } else if (location.length == 2) {
                                temp_variant = temp_list_variants.filter(variant =>
                                    variant.option1 === this.list_option[0].values[location[0]]
                                    && variant.option2 === this.list_option[1].values[location[1]]
                                    && variant.option3 === this.list_option[2].values[j]
                                )
                            }
                            if (temp_variant) {
                                list.push({
                                    title: temp_variant[0]?.title,
                                    src: temp_variant[0]?.featured_image?.src,
                                    available: temp_variant[0]?.available,
                                    price:temp_variant[0]?.price
                                })
                            } else {
                                list.push({
                                    title: null,
                                    src: null,
                                    available: false,
                                    price:0
                                })
                            }
                        } else {
                            list.push({
                                title: null,
                                src: null,
                                available: false,
                                price:0
                            })
                        }
                    }
                }
                return list
            }
            this.list_variants = add_list_variants(0, [])

            for (let variant of res.data.variants) {
                this.list_variant_img.push({
                    img: variant.featured_image != null ? variant.featured_image.src : null,
                    available: variant.available,
                    title: variant.title
                })
            }
        }
        ,
        get_pv_data(index) {
            for (let item of this.pv_data) {
                if ((!('error' in item) && this.list_option[index]?.name === item.option_setting.name)) {
                    return item
                }
            }
            return false
        },
    },
    async mounted() {
        let form = document.querySelector("form[action='/cart/add']")
        this.max_width = form?.offsetWidth === 0 ? this.max_width : form?.offsetWidth
        let product_url = window.location.origin + window.location.pathname + '.js'
        if (nestvairant_product_handle !== undefined) {
            product_url = `${window.location.origin}/products/${nestvairant_product_handle}.js`
        }
        try {
            const response = await axios.get(product_url);
            this.processResponse(response);
        } catch (error) {
            try {
                const fallbackUrl = window.location.origin + window.location.pathname + '.js';
                const responseFallback = await axios.get(fallbackUrl);
                this.processResponse(responseFallback);
            } catch (fallbackError) {

            }
        }

        let option_blocks
        if (this.isConflictTheme
        ) {
            let parent_target = document.querySelector(this.themeData.parent_type_value)
            option_blocks = parent_target.querySelectorAll(this.themeData.option_type_value)
            this.block_element_selector = this.themeData.parent_type_value
            this.option_block_selector = this.themeData.option_type_value
            for (let option of option_blocks) {
                option.style.setProperty('display', 'none', 'important');
            }
        } else {
            let block_element = document.querySelector(this.block_element_selector)
            option_blocks = block_element.querySelectorAll(this.option_block_selector)
        }
        for (let i = 0; i < option_blocks.length; i++) {
            let variant_ids = []
            let input_type
            let variant_template_ids = option_blocks[i].querySelector("select")
            if (variant_template_ids) {
                input_type = 'select'
                let option_list = variant_template_ids.querySelectorAll("option:not([disabled])")
                if (option_list.length != this.list_option[i].values.length) {
                    option_list = option_blocks[i].querySelectorAll('option')
                }
                for (let j = 0; j < option_list.length; j++) {
                    variant_ids.push(j)
                    if (option_list[j].selected) {
                        this.list_checked_option.push(j)
                    }
                }
            } else {
                variant_template_ids = option_blocks[i].querySelectorAll('input:not([type="hidden"])')
                input_type = 'checkbox'
                for (let j = 0; j < variant_template_ids.length; j++) {
                    variant_ids.push(j)
                    if (variant_template_ids[j].checked) {
                        this.list_checked_option.push(j)
                    }
                }
                if (variant_template_ids.length == 0) {
                    input_type = 'theme_forest'
                    variant_template_ids = option_blocks[i].querySelectorAll('div[data-swatch-item]')
                    for (let j = 0; j < variant_template_ids.length; j++) {
                        variant_ids.push(j)
                        if (variant_template_ids[j].classList.contains('is--selected')) {
                            this.list_checked_option.push(j)
                        }
                    }
                }
                if (variant_template_ids.length == 0) {
                    input_type = 'button'
                    variant_template_ids = option_blocks[i].querySelectorAll('button')
                    for (let j = 0; j < variant_template_ids.length; j++) {
                        variant_ids.push(j)
                        if (variant_template_ids[j].classList.contains('btnActive')) {
                            this.list_checked_option.push(j)
                        }
                    }
                }
            }
            this.list_input_type.push(input_type)
            this.array_variant_template_id.push(variant_ids)
        }
        if (this.list_checked_option.length === 0) {
            for (let i = 0; i < option_blocks.length; i++) {
                this.list_checked_option.push(0)
            }
        }
    }
}
</script>