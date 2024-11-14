<template>
    <div style="gap: 10px;padding-top: 10px" class="pv-flex-column pv-card-product">

        <div v-if="list_product_group.length >0">
            <div v-for="(product_group, index) in list_product_group">
                <div v-if="product_group.status_collection_page">
                    <product-group-component :id="'pv-frontend-block-group' + index"
                                             @change_product_group_image="change_product_group_image"
                                             :group_index="index"
                                             :name="product_group['name']"
                                             style="margin-bottom: 10px"
                                             :list_option_data_img_product_group="list_option_data_img_product_group"
                                             :max_width="max_width"
                                             :product_id="product_id"
                                             page="collection"
                                             :card_product_info="card_product_info"
                                             :pv_data="product_group"/>
                </div>

            </div>
        </div>
        <div v-for="(variant_option, index) in this.pv_data">
            <card-product @set_list_selected_variant="set_list_selected_variant"
                          :object_selected_variant="object_selected_variant"
                          :variant_list_processed="processVariantList" :variant_option="variant_option"
                          :card_product_info="card_product_info" :default_feature_image="default_feature_image"/>
        </div>
        <div class="add-to-cart__button" v-if="add_to_cart_event">
            <button @click="add_to_cart">
                Add to cart
            </button>
        </div>
    </div>
</template>
<script>


import '../../static/css/shopify_store.css'
import CardProduct from "./card_product.vue";
import ProductGroupComponent from "./product_group_component.vue";
import {add_to_cart} from "../../utils/AjaxShopify";

export default {
    name: "Collection",
    components: {ProductGroupComponent, CardProduct},
    data() {
        return {
            add_to_cart_event: true,
            object_selected_variant: {},
            pv_data: null,
            card_index: null,
            card_product_info: {},
            list_product_variant: [],
            default_feature_image: '',
            list_all_option_variant: [],
            object_selected_variant_index_data: -1,

            list_product_group: [],
            list_option_data_img_product_group: {},
            product_id: null,
            max_width: 500,
            list_input_type: [],
        }
    },
    methods: {
        add_to_cart() {
            add_to_cart({
                id: 43275603771544,
                quantity: 2
            })
        },
        change_product_group_image(group_index, product_id) {
            this.changeImageSource('product_group_mode', this.list_product_group[group_index]['list_product'][product_id])

        },
        generateImageSrcSet(img_src) {
            let list_resolution = ["165", "170", "180", "185", "198", "205", "210", "220", "245", "270", "290", "320", "355", "360", "370", "420", "430", "460", "470", "510", "523", "533", "534", "540", "570", "640", "665", "670", "720", "775", "785", "870", "900", "930", "935", "940", "1066", "1080", "1160", "1170", "1270", "1296", "1370", "1512", "1570", "1728", "1770", "1800", "1850", "1944", "2160", "2376", "2592", "2808", "3024"]
            let srcset_string = ''
            for (let i = 0; i < list_resolution.length; i++) {
                let resol = list_resolution[i];
                let replace_img_src = img_src.replace(/(\.jpg)$/, '_' + resol + 'x$1');
                srcset_string += replace_img_src + ' ' + resol + "w";
                if (i < list_resolution.length - 1) {
                    srcset_string += ', ';
                }
            }
            return srcset_string
        },
        changeImageSource(mode, object_selected_data) {
            let current_card_container_element = document.querySelectorAll('.product_variant-card-' + this.card_index)[0]
            let list_images = current_card_container_element.querySelectorAll('img:not([class*="pv"]):not([class*="imgWidthBigger"])');
            list_images = Array.from(list_images);
            let list_image = list_images.filter(img => img.hasAttribute('srcset') || img.hasAttribute('sizes'));
            let image_src = this.default_feature_image

            if (mode === 'collection_mode') {
                if (object_selected_data !== -1) {
                    if (this.list_product_variant[object_selected_data].featured_image !== null) {
                        image_src = this.list_product_variant[object_selected_data].featured_image.src
                    }
                }
            } else {
                image_src = object_selected_data.img_src
            }

            list_image.forEach(image => {
                if (image.hasAttribute('srcset')) {
                    image.srcset = this.generateImageSrcSet(image_src)
                }
                if (image.hasAttribute('src')) {
                    image.src = image_src
                }
            })
        },
        set_list_selected_variant(key, value, click_event) {
            this.object_selected_variant[key] = value
            if (click_event) {
                this.object_selected_variant_index_data = this.findAvailableVariantIndex(this.object_selected_variant, this.list_product_variant);

                this.changeImageSource('collection_mode', this.object_selected_variant_index_data)

            }
        },
        sortValuesByPosition(values) {
            let array = []
            this.card_product_info.product.options.forEach(object => {
                array.push(values[object.name])
            })
            return array
        },
        findAvailableVariantIndex(variant, variantsList) {
            const sortedObj = this.sortValuesByPosition(variant);
            let count_active_option = 0
            sortedObj.forEach(obj => {
                if (obj !== undefined) {
                    count_active_option++
                }
            })
            return variantsList.findIndex((item) => {
                let count = 0
                item.options.forEach((option, index) => {
                    if (option === sortedObj[index]) {
                        count++
                    }
                })
                if (count === item.options.length) return item;
                else if (this.card_product_info.product.options.length - Object.keys(variant).length >= 1 && count >= 1) {
                    if (Object.keys(variant).length !== 2) {
                        return item
                    } else {
                        if (count === count_active_option) return item
                        else return false
                    }
                }

            });
        },
        findDifferingElement(selectedOption, variantParts) {
            let matchCount = 0;
            let differingIndex = -1;
            for (let i = 0; i < variantParts.length; i++) {
                if (selectedOption[i] === variantParts[i]) {
                    matchCount++;
                } else {
                    differingIndex = i; // This part differs
                }
            }

            if (matchCount === variantParts.length - 1 && differingIndex !== -1) {
                return differingIndex
            }

            return null;
        },
        sortArray(itemsArray) {
            itemsArray.sort((a, b) => {
                // Extract labels, handling both direct strings and objects
                const labelA = typeof a === 'string' ? a : a.label;
                const labelB = typeof b === 'string' ? b : b.label;

                // Check if both labels are numbers
                const aIsNumber = !isNaN(parseFloat(labelA)) && isFinite(labelA);
                const bIsNumber = !isNaN(parseFloat(labelB)) && isFinite(labelB);

                // If both are numbers, sort numerically
                if (aIsNumber && bIsNumber) {
                    return parseFloat(labelA) - parseFloat(labelB);
                }

                // If only one is a number, the number should come first
                if (aIsNumber) return -1;
                if (bIsNumber) return 1;

                // If neither are numbers, sort based on uppercase first, then alphabetically
                const aIsUppercase = labelA[0] === labelA[0].toUpperCase();
                const bIsUppercase = labelB[0] === labelB[0].toUpperCase();

                if (aIsUppercase && !bIsUppercase) {
                    return -1;
                }
                if (!aIsUppercase && bIsUppercase) {
                    return 1;
                }
                return labelA.localeCompare(labelB);
            });
        }
    },
    computed: {
        processVariantList() {

            let finalOptionsList = []
            //init the with the first found value

            let selected_option = []
            let status = false
            let featured_image = this.default_feature_image
            if (this.object_selected_variant_index_data !== -1) {
                if (this.list_product_variant[this.object_selected_variant_index_data].available !== false) {
                    status = true
                }
                selected_option = this.list_product_variant[this.object_selected_variant_index_data]['options']

                if (this.list_product_variant[this.object_selected_variant_index_data].featured_image !== null) {
                    featured_image = this.list_product_variant[this.object_selected_variant_index_data].featured_image.src
                }
            }
            Object.keys(this.object_selected_variant).forEach(option => {
                finalOptionsList.push({
                    type: option,
                    label: this.object_selected_variant[option],
                    status: status,
                    url_image: featured_image
                })
            })
            for (let i = 0; i < this.list_product_variant.length; i++) {
                if (i === this.object_selected_variant_index_data) continue;

                let option_label_index = this.findDifferingElement(selected_option, this.list_product_variant[i]['options'])
                if (option_label_index !== null) {
                    finalOptionsList.push(JSON.parse(JSON.stringify({
                        type: this.card_product_info.product.options[option_label_index]['name'],
                        label: this.list_product_variant[i][`option${option_label_index + 1}`],
                        status: this.list_product_variant[i].available,
                        url_image: this.list_product_variant[i].featured_image !== null ? this.list_product_variant[i].featured_image.src : this.default_feature_image
                    })))
                } else if (this.card_product_info.product.options.length === 1) {
                    finalOptionsList.push(JSON.parse(JSON.stringify({
                        type: this.card_product_info.product.options[0].name,
                        label: this.list_product_variant[i]['option1'],
                        status: this.list_product_variant[i].available,
                        url_image: this.list_product_variant[i].featured_image !== null ? this.list_product_variant[i].featured_image.src : this.default_feature_image
                    })))
                }
            }

            if (finalOptionsList.length === this.list_all_option_variant.length) {
                return finalOptionsList
            } else {
                if (this.list_all_option_variant.length > finalOptionsList.length) {
                    this.list_all_option_variant.forEach(option => {
                        const exists = finalOptionsList.find(element => element.label === option.label && element.type === option.type);
                        if (!exists) {
                            finalOptionsList.push(JSON.parse(JSON.stringify(option)));
                        }
                    })
                    finalOptionsList.forEach(object => {
                        object.status = true
                    })
                }
            }
            // this.sortArray(finalOptionsList)
            return finalOptionsList
        }
    },
    async mounted() {
        this.card_index = this.$.attrs.data.card_index
        this.card_product_info = this.$.attrs.data.card_product_info
        this.pv_data = this.$.attrs.data.pv_data
        this.list_product_variant = JSON.parse(JSON.stringify(this.card_product_info.product.variants))
        this.default_feature_image = this.card_product_info.product.featured_image !== null ? 'https:' + this.card_product_info.product.featured_image : 'https://app.nestscale.com/nestprdvariant/static/images/no_image.png'

        let optionsInfo = {};
        for (let index_options = 0; index_options < this.card_product_info.product.options.length; index_options++) {
            let options = this.card_product_info.product.options[index_options]
            optionsInfo[options.name] = {}
            for (let option_value of options.values) {

                if (!(option_value in optionsInfo[options.name])) {
                    optionsInfo[options.name][option_value] = {
                        available: false,
                        featured_images: null
                    };
                }

                for (let variant of this.list_product_variant) {
                    let option_from_list = variant[`option${options.position}`];

                    let sibling_first_option = variant.options.length === 3 ? (options.position === 1 ? 2 : 1) : variant.options.length === 2 ? (options.position === 1 ? 2 : 1) : 1
                    let sibling_second_option = variant.options.length === 3 ? (options.position === 3 ? 2 : 3) : null
                    let option_first_sibling = this.card_product_info.product.options[sibling_first_option - 1]['name']
                    let option_second_sibling = sibling_second_option !== null ? this.card_product_info.product.options[sibling_second_option - 1]['name'] : null
                    if (option_first_sibling in optionsInfo) {
                        if (variant[`option${sibling_first_option}`] in optionsInfo[option_first_sibling]) {
                            if (variant.featured_image && optionsInfo[option_first_sibling][variant[`option${sibling_first_option}`]].featured_images === undefined) {
                                optionsInfo[option_first_sibling][variant[`option${sibling_first_option}`]].featured_images = variant.featured_image.src
                            }
                        }
                    }
                    if (option_second_sibling in optionsInfo) {
                        if (variant[`option${sibling_second_option}`] in optionsInfo[option_second_sibling]) {
                            if (variant.featured_image && optionsInfo[option_second_sibling][variant[`option${sibling_second_option}`]].featured_images === undefined) {
                                optionsInfo[option_second_sibling][variant[`option${sibling_second_option}`]].featured_images = variant.featured_image.src
                            }
                        }
                    }
                    if (option_value === option_from_list) {
                        optionsInfo[options.name][option_value].available = variant.available;
                        if (variant.featured_image && optionsInfo[options.name][option_value].featured_images !== undefined) {
                            optionsInfo[options.name][option_value].featured_images = variant.featured_image.src
                            break;
                        }
                    }
                }
            }
        }

        Object.keys(optionsInfo).forEach(option => {
            Object.keys(optionsInfo[option]).forEach(value => {
                this.list_all_option_variant.push({
                    type: option,
                    label: value,
                    status: optionsInfo[option][value].available,
                    url_image: optionsInfo[option][value].featured_images !== null ? optionsInfo[option][value].featured_images : this.default_feature_image
                })
            })
        })

        this.product_id = this.card_product_info.product.id
        try {
            this.list_product_group = JSON.parse(JSON.stringify(nestvariant_product_group_data['list_option']))
            this.list_option_data_img_product_group = JSON.parse(JSON.stringify(nestvariant_product_group_data['list_option_data_img']))

            this.list_product_group = JSON.parse(JSON.stringify(this.list_product_group.filter(group => {
                return this.product_id in group.list_product
            })))
        } catch (e) {
        }
    }
}
</script>


<style>
.add-to-cart__button {
    z-index: 3;
    position: absolute;
    width: 100% !important;
}
</style>