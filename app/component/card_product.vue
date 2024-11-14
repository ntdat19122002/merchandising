<template>
    <div v-if="variant_option !== undefined && option_setting.status_collection_page" class="pv-flex-column">
        <div v-if="option_setting_color_custom_image.length > 0">


            <div v-if="design_setting.display_style === 'swatch_circle_in_square'">
                <div v-if="design_setting.label_show" :style="{fontSize: `${design_setting.label_size}px`}"
                     style="display: flex">
                    <div style="white-space: nowrap">{{ option_setting.name }}</div>
                    <div style="white-space: nowrap">:&nbsp;{{ labelText }}</div>
                </div>
                <div class="pv-flex-row" :style="[getCollectionPosition]">
                    <RadioGroup v-model:value="select_variant" style="display: flex; flex-wrap: wrap"
                                :style="[ { gap: `${design_setting.swatch_spacing}px` }, getCollectionPosition ]">

                        <Tooltip color="#FFFFFF" :autoAdjustOverflow="true"
                                 v-for="item in getVariantPreviewArray(list_variant)"
                                 @mouseenter="handleMouseEnter($event, item)"
                                 @mouseleave="hovered_item = null">
                            <template #title v-if="design_setting.hover_show_variant_description">
                                <span style="z-index: 999">
                                    {{ item.label }}
                                </span>
                            </template>
                            <Radio :value="item.label" style="padding: 0" @click="changeVariant(item.label)"
                                   @touchstart="touchStartEvent($event,item.label)">
                                <div class="pv-outer-border"
                                     :style="{...(outerBorder(item)), opacity: item.status ? 1 : 0.4}">
                                    <div :style="innerBorder(item)" style="overflow: hidden">
                                        <div v-if="item.option_swatch === 'color'"
                                             style="height: 100%; width: 100%; position: relative">
                                            <div v-if="item.color_code" :style="{background: `${item.color_code}`}"
                                                 style="height: 100%; width: 100%; display: flex !important">
                                            </div>
                                            <img v-if="!item.status" alt="" class="pv-outstock"
                                                 src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png">
                                        </div>
                                        <div v-if="item.option_swatch === 'upload'" style="height: 100%; width: 100%">
                                            <div
                                                style="height: 100%; width: 100%; display: flex !important; position: relative; background: white">
                                                <img :src="`https://app.nestscale.com${item.upload_img_url}`"
                                                     alt=""
                                                     @load="trackImage" :style="[getImageStyle(item) ]"
                                                     style="position: absolute">
                                                <img v-if="!item.status" alt="" class="pv-outstock"
                                                     src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png">
                                            </div>
                                        </div>
                                        <div v-if="item.option_swatch === 'add_url'" style="height: 100%; width: 100%">
                                            <div
                                                style="height: 100%; width: 100%; display: flex !important; position: relative; background: white">
                                                <img :src="item.swatch_img_url"

                                                     @load="trackImage" alt=""
                                                     :style="[getImageStyle(item) ]"
                                                     style="position: absolute">
                                                <img v-if="!item.status" alt="" class="pv-outstock"
                                                     src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </Radio>
                        </Tooltip>
                        <div v-if="num_of_extra_item !== 0">
                            <div @click="clickExtraItem"
                                 @mouseenter="handleMouseEnter($event, list_variant[list_variant.length - num_of_extra_item])"
                                 @mouseleave="hovered_item = null" style="cursor: pointer"
                                 class="pv-outer-border"
                                 :style="{...(outerBorder(list_variant[list_variant.length - num_of_extra_item]))}">
                                <div style="border: none !important;position: relative;overflow: hidden;cursor: pointer;
                                    " :style="combinedStyles">
                                    <div class="pv-plus-variant-hidden"
                                         :style="{color:design_setting.image_overlay ? '#FFFFFF' : ''}">
                                        +{{ num_of_extra_item }}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </RadioGroup>
                </div>
            </div>
            <div v-if="design_setting.display_style === 'circular_swatch'">
                <div v-if="design_setting.label_show" :style="{fontSize: `${design_setting.label_size}px`}"
                     style="display: flex">
                    <div style="white-space: nowrap">{{ option_setting.name }}</div>
                    <div style="white-space: nowrap">:&nbsp;{{ labelText }}</div>
                </div>
                <div class="pv-flex-row" :style="[getCollectionPosition]">
                    <RadioGroup v-model:value="select_variant" style="display: flex; flex-wrap: wrap"
                                :style="[ { gap: `${design_setting.swatch_spacing}px` }, getCollectionPosition ]">

                        <Tooltip color="#FFFFFF" v-for="item in getVariantPreviewArray(list_variant)"
                                 :autoAdjustOverflow="true"
                                 @mouseenter="handleMouseEnter($event, item)"
                                 @mouseleave="hovered_item = null">
                            <template #title v-if="design_setting.hover_show_variant_description">
                                <span style="z-index: 999">
                                    {{ item.label }}
                                </span>
                            </template>
                            <Radio :value="item.label" style="padding: 0" @click="changeVariant(item.label)"
                                   @touchstart="touchStartEvent($event,item.label)"
                                   :style="{opacity: item.status ? 1 : 0.4}">
                                <div class="pv-outer-border"
                                     :style="{...(outerBorder(item)), opacity: item.status ? 1 : 0.4}">
                                    <div :style="innerBorder(item)" style="overflow: hidden">
                                        <div v-if="item.option_swatch === 'color'"
                                             style="height: 100%; width: 100%; position: relative">
                                            <div v-if="item.color_code" :style="{background: `${item.color_code}`}"
                                                 style="height: 100%; width: 100%; display: flex !important">
                                            </div>
                                            <img v-if="!item.status" alt="" class="pv-outstock"
                                                 src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png">
                                        </div>
                                        <div v-if="item.option_swatch === 'upload'" style="height: 100%; width: 100%">
                                            <div
                                                style="height: 100%; width: 100%; display: flex !important; position: relative">
                                                <img :src="`https://app.nestscale.com${item.upload_img_url}`"
                                                     alt=""
                                                     @load="trackImage" :style="[getImageStyle(item) ]"
                                                     style="position: absolute">
                                                <img v-if="!item.status" alt="" class="pv-outstock"
                                                     src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png">
                                            </div>
                                        </div>
                                        <div v-if="item.option_swatch === 'add_url'" style="height: 100%; width: 100%">
                                            <div
                                                style="height: 100%; width: 100%; display: flex !important; position: relative">
                                                <img :src="item.swatch_img_url"

                                                     @load="trackImage" alt=""
                                                     :style="[getImageStyle(item) ]"
                                                     style="position: absolute">
                                                <img v-if="!item.status" alt="" class="pv-outstock"
                                                     src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </Radio>
                        </Tooltip>
                        <div v-if="num_of_extra_item !== 0">
                            <div @click="clickExtraItem"
                                 @mouseenter="handleMouseEnter($event, list_variant[list_variant.length - num_of_extra_item])"
                                 @mouseleave="hovered_item = null"
                                 class="pv-outer-border"
                                 :style="{...(outerBorder(list_variant[list_variant.length - num_of_extra_item]))}">
                                <div style="position: relative;overflow: hidden;cursor: pointer;
                                            " :style="combinedStyles">
                                    <div class="pv-plus-variant-hidden"
                                         :style="{color:design_setting.image_overlay ? '#FFFFFF' : ''}">
                                        +{{ num_of_extra_item }}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </RadioGroup>
                </div>
            </div>
            <div v-if="design_setting.display_style === 'square_swatch'">
                <div v-if="design_setting.label_show" :style="{fontSize: `${design_setting.label_size}px`}"
                     style="display: flex">
                    <div style="white-space: nowrap">{{ option_setting.name }}</div>
                    <div style="white-space: nowrap">:&nbsp;{{ labelText }}</div>
                </div>
                <div class="pv-flex-row" :style="[getCollectionPosition]">
                    <RadioGroup v-model:value="select_variant" style="display: flex; flex-wrap: wrap;position: relative"
                                :style="[ { gap: `${design_setting.swatch_spacing}px` }, getCollectionPosition ]">

                        <Tooltip color="#FFFFFF" v-for="item in getVariantPreviewArray(list_variant)"
                                 :autoAdjustOverflow="true"
                                 @mouseenter="handleMouseEnter($event, item)"
                                 @mouseleave="hovered_item = null">
                            <template #title v-if="design_setting.hover_show_variant_description">
                                <span style="z-index: 999">
                                    {{ item.label }}
                                </span>
                            </template>
                            <Radio :value="item.label" style="padding: 0" @click="changeVariant(item.label)"
                                   @touchstart="touchStartEvent($event,item.label)">
                                <div class="pv-outer-border"
                                     :style="{...(outerBorder(item)), padding: `${design_setting.border_spacing}px`,opacity: item.status ? 1 : 0.4}">
                                    <div :style="innerBorder(item)" style="overflow: hidden">
                                        <div v-if="item.option_swatch === 'color'"
                                             style="height: 100%; width: 100%; position: relative">
                                            <div v-if="item.color_code" :style="{background: `${item.color_code}`}"
                                                 style="height: 100%; width: 100%; display: flex !important">
                                            </div>
                                            <img v-if="!item.status" alt="" class="pv-outstock"
                                                 src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png">
                                        </div>
                                        <div v-if="item.option_swatch === 'upload'" style="height: 100%; width: 100%">
                                            <div
                                                style="height: 100%; width: 100%; display: flex !important; position: relative">
                                                <img :src="`https://app.nestscale.com${item.upload_img_url}`"
                                                     alt=""
                                                     @load="trackImage" :style="[getImageStyle(item) ]"
                                                     style="position: absolute">
                                                <img v-if="!item.status" alt="" class="pv-outstock"
                                                     src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png">
                                            </div>
                                        </div>
                                        <div v-if="item.option_swatch === 'add_url'" style="height: 100%; width: 100%">
                                            <div
                                                style="height: 100%; width: 100%; display: flex !important; position: relative">
                                                <img :src="item.swatch_img_url"

                                                     @load="trackImage" alt=""
                                                     :style="[getImageStyle(item) ]"
                                                     style="position: absolute">
                                                <img v-if="!item.status" alt="" class="pv-outstock"
                                                     src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </Radio>
                        </Tooltip>
                        <div v-if="num_of_extra_item !== 0">
                            <div @click="clickExtraItem"
                                 @mouseenter="handleMouseEnter($event, list_variant[list_variant.length - num_of_extra_item])"
                                 @mouseleave="hovered_item = null"
                                 class="pv-outer-border"
                                 :style="{...(outerBorder(list_variant[list_variant.length - num_of_extra_item]))}">
                                <div style="position: relative;overflow: hidden;cursor: pointer;
                                            " :style="combinedStyles">

                                    <div class="pv-plus-variant-hidden"
                                         :style="{color:design_setting.image_overlay ? '#FFFFFF' : ''}">
                                        +{{ num_of_extra_item }}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </RadioGroup>
                </div>
            </div>
        </div>
        <div v-else>
            <div v-if="design_setting.display_style === 'swatch_circle_in_square'">
                <div v-if="design_setting.label_show" :style="{fontSize: `${design_setting.label_size}px`}"
                     style="display: flex">
                    <div style="white-space: nowrap">{{ option_setting.name }}</div>
                    <div style="white-space: nowrap">:&nbsp;{{ labelText }}</div>
                </div>
                <div class="pv-flex-row" :style="[getCollectionPosition]">
                    <RadioGroup v-model:value="select_variant" style="display: flex; flex-wrap: wrap"
                                :style="[ { gap: `${design_setting.swatch_spacing}px` }, getCollectionPosition ]">

                        <Tooltip color="#FFFFFF" v-for="item in getVariantPreviewArray(list_variant)"
                                 :autoAdjustOverflow="true"

                                 @mouseenter="handleMouseEnter($event, item)"
                                 @mouseleave="hovered_item = null">
                            <template #title v-if="design_setting.hover_show_variant_description">
                                <span style="z-index: 999">
                                    {{ item.label }}
                                </span>
                            </template>
                            <Radio :value="item.label" style="padding: 0" @click="changeVariant(item.label)"
                                   @touchstart="touchStartEvent($event,item.label)">
                                <div class="pv-outer-border pv-swatch_circle_in_square"
                                     :style="{...(outerBorder(item)), opacity: item.status ? 1 : 0.4}">
                                    <div :style="innerBorder(item)" style="overflow: hidden">
                                        <img v-if="item.url_image != null" @load="trackImage" :src="item.url_image"
                                             alt=""
                                             style="width: 100%" :style="[getImageStyle(item)]">
                                        <img v-if="!item.status" alt="" class="pv-outstock"
                                             src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png">
                                    </div>
                                </div>
                            </Radio>
                        </Tooltip>
                        <div v-if="num_of_extra_item !== 0">
                            <div @click="clickExtraItem"
                                 @mouseenter="handleMouseEnter($event, list_variant[list_variant.length - num_of_extra_item])"
                                 @mouseleave="hovered_item = null"
                                 class="pv-outer-border pv-swatch_circle_in_square"
                                 :style="{...(outerBorder(list_variant[list_variant.length - num_of_extra_item]))}">
                                <div style="border: none !important;position: relative;cursor: pointer;
                                            " :style="combinedStyles">

                                    <div class="pv-plus-variant-hidden"
                                         :style="{color:design_setting.image_overlay ? '#FFFFFF' : ''}">
                                        +{{ num_of_extra_item }}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </RadioGroup>

                </div>
            </div>
            <div v-if="design_setting.display_style === 'circular_swatch'">
                <div v-if="design_setting.label_show" :style="{fontSize: `${design_setting.label_size}px`}"
                     style="display: flex">
                    <div style="white-space: nowrap">{{ option_setting.name }}</div>
                    <div style="white-space: nowrap">:&nbsp;{{ labelText }}</div>
                </div>
                <div class="pv-flex-row" :style="[getCollectionPosition]">
                    <RadioGroup v-model:value="select_variant" style="display: flex; flex-wrap: wrap"
                                :style="[ { gap: `${design_setting.swatch_spacing}px` }, getCollectionPosition ]">
                        <Tooltip color="#FFFFFF" v-for="item in getVariantPreviewArray(list_variant)"
                                 :autoAdjustOverflow="true"
                                 @mouseenter="handleMouseEnter($event, item)"
                                 @mouseleave="hovered_item = null">
                            <template #title v-if="design_setting.hover_show_variant_description">
                                <span style="z-index: 999">
                                    {{ item.label }}
                                </span>
                            </template>
                            <Radio :value="item.label" style="padding: 0" @click="changeVariant(item.label)"
                                   @touchstart="touchStartEvent($event,item.label)">
                                <div class="pv-outer-border"
                                     :style="{...(outerBorder(item)), opacity: item.status ? 1 : 0.4}"
                                     style="justify-content: center; border-radius: 50% !important; align-items: center; display: flex; background: white">
                                    <div :style="innerBorder(item)"
                                         style="overflow: hidden; position: relative; border-radius: 50% !important">
                                        <img @load="trackImage" :src="item.url_image || default_feature_image"
                                             alt=""
                                             style="position: absolute" :style="[getImageStyle(item)]">
                                        <img v-if="!item.status" alt="" class="pv-outstock"
                                             src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png">
                                    </div>
                                </div>
                            </Radio>
                        </Tooltip>
                        <div v-if="num_of_extra_item !== 0">
                            <div @click="clickExtraItem"
                                 @mouseenter="handleMouseEnter($event, list_variant[list_variant.length - num_of_extra_item])"
                                 @mouseleave="hovered_item = null"
                                 style="justify-content: center; border-radius: 50% !important; align-items: center; display: flex; background: white"
                                 :style="{...(outerBorder(list_variant[list_variant.length - num_of_extra_item]))}">
                                <div
                                    style="overflow: hidden; position: relative; border-radius: 50% !important;cursor: pointer;"
                                    :style="combinedStyles">
                                    <div class="pv-plus-variant-hidden" style="cursor: pointer"
                                         :style="{color:design_setting.image_overlay ? '#FFFFFF' : ''}">+{{
                                            num_of_extra_item
                                        }}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </RadioGroup>
                </div>
            </div>
            <div v-if="design_setting.display_style === 'square_swatch'">
                <div v-if="design_setting.label_show" :style="{fontSize: `${design_setting.label_size}px`}"
                     style="display: flex">
                    <div style="white-space: nowrap">{{ option_setting.name }}</div>
                    <div style="white-space: nowrap">:&nbsp;{{ labelText }}</div>
                </div>
                <div class="pv-flex-row" :style="[getCollectionPosition]">
                    <RadioGroup v-model:value="select_variant" style="display: flex; flex-wrap: wrap;position: relative"
                                :style="[ { gap: `${design_setting.swatch_spacing}px` }, getCollectionPosition ]">
                        <Tooltip color="#FFFFFF" v-for="item in getVariantPreviewArray(list_variant)"
                                 :autoAdjustOverflow="true"
                                 @mouseenter="handleMouseEnter($event, item)"
                                 @mouseleave="hovered_item = null">
                            <template #title v-if="design_setting.hover_show_variant_description">
                                <span style="z-index: 999">
                                    {{ item.label }}
                                </span>
                            </template>
                            <Radio :value="item.label" style="padding: 0" @click="changeVariant(item.label)"
                                   @touchstart="touchStartEvent($event,item.label)">
                                <div class="pv-outer-border"
                                     :style="{...(outerBorder(item)), opacity: item.status ? 1 : 0.4}"
                                     style="justify-content: center; align-items: center; display: flex; background:white">
                                    <div style="overflow: hidden; position: relative" :style="innerBorder(item)">
                                        <img v-if="item.url_image != null" @load="trackImage" :src="item.url_image"
                                             :style="[getImageStyle(item) ]"
                                             alt="" class="pv-img">
                                        <img v-if="!item.status" alt="" class="pv-outstock"
                                             src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png">
                                    </div>
                                </div>
                            </Radio>
                        </Tooltip>
                        <div v-if="num_of_extra_item !== 0">
                            <div @click="clickExtraItem"
                                 @mouseenter="handleMouseEnter($event, list_variant[list_variant.length - num_of_extra_item])"
                                 @mouseleave="hovered_item = null"
                                 style="justify-content: center; align-items: center; display: flex; background:white"
                                 :style="{...(outerBorder(list_variant[list_variant.length - num_of_extra_item]))}">
                                <div style="overflow: hidden; position: relative;" :style="combinedStyles">
                                    <div class="pv-plus-variant-hidden"
                                         :style="{color:design_setting.image_overlay ? '#FFFFFF' : ''}">
                                        +{{ num_of_extra_item }}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </RadioGroup>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import {Radio, RadioGroup, Select, SelectOption, Tooltip} from "ant-design-vue"
import {DownOutlined} from "@ant-design/icons-vue"


export default {
    name: "CardProduct",
    data() {
        return {
            option_setting: {},
            design_setting: {},
            option_setting_color_custom_image: {},
            list_variant: [],
            select_variant: null,
            hovered_item: null,
            option_variant_info: {}, num_of_extra_item: 0,
            product_url: '',
            backgroundLimitedImage: 'https://app.nestscale.com/nestprdvariant/static/images/rainbow.png'
        }
    },
    components: {
        Radio,
        RadioGroup,
        Select,
        SelectOption, Tooltip,
        DownOutlined
    },
    props: {
        variant_option: Object,
        card_product_info: Object,
        variant_list_processed: Array,
        default_feature_image: String,
        object_selected_variant: Object
    },
    watch: {
        variant_list_processed(newone) {
            if (newone) {
                this.processVariantList(newone)
            }
        }
    },
    emits: ['set_list_selected_variant'],
    computed: {
        combinedStyles() {
            const lastVariant = this.list_variant[this.list_variant.length - this.num_of_extra_item];
            return {
                ...this.innerBorder(lastVariant),
                background: this.design_setting.image_overlay ?   `linear-gradient(0deg, rgba(0, 0, 0, 0.20) 0%, rgba(0, 0, 0, 0.20) 100%), url('${this.backgroundLimitedImage}') lightgray 50% / cover no-repeat` : `linear-gradient(0deg, rgba(255, 255, 255, 0.40) 0%, rgba(255, 255, 255, 0.40) 100%), url('${this.backgroundLimitedImage}') lightgray 50% / cover no-repeat`,
            };
        },
        getCollectionPosition() {
            let style = {}
            if (this.design_setting.collection_position === "right") {
                style.justifyContent = 'flex-end'
            } else if (this.design_setting.collection_position === "center") {
                style.justifyContent = 'center'
            }
            return style
        },
        isMobileDevice() {
            const userAgent = navigator.userAgent || navigator.vendor || window.opera;
            return /android|avantgo|bada\/|blackberry|bolt|boost|cricket|docomo|fone|hiptop|mini|mobi|palm|phone|pie|plucker|pocket|psp|symbian|treo|up\.browser|up\.link|webos|wince/i.test(userAgent) ||
                /iemobile|windows phone/i.test(userAgent) ||
                /iphone|ipod|ipad/i.test(userAgent) && !window.MSStream; // Exclude Windows tablets
        },
        labelText() {
            if (this.select_variant !== null && this.select_variant !== undefined) {
                if (this.design_setting.label_case === "uppercase") {
                    return this.select_variant.toUpperCase()
                }
                if (this.design_setting.label_case === "lowercase") {
                    return this.select_variant.toLowerCase()
                }
                if (this.design_setting.label_case === "default") {
                    return this.select_variant
                }
            }

        }
    },
    methods: {
        clickExtraItem() {
            window.open(this.product_url, '_blank')
        },
        touchStartEvent(event, item) {
            event.preventDefault();
            if (this.isMobileDevice) {
                this.select_variant = item
                this.$emit('set_list_selected_variant', this.option_setting.name, item, true)
            }
        },
        handleMouseEnter(event, item) {
            this.hovered_item = {
                item: item,
                event: event
            }
        },
        imageSettings() {
            let imageStyle = {};
            switch (this.design_setting.img_position) {
                case "center":
                    imageStyle = {
                        objectFit: this.design_setting.img_position,
                        top: '50%',
                        left: '50%',
                        transform: 'translate(-50%, -50%)'
                    };
                    break;
                case "top":
                    imageStyle = {
                        objectFit: this.design_setting.img_position,
                        top: '0',
                        left: '0',
                        right: '0',
                    };
                    break;
                case "bottom":
                    imageStyle = {
                        objectFit: this.design_setting.img_position,
                        left: '0',
                        right: '0',
                        bottom: 0
                    };
                    break;
            }
            imageStyle.objectFit = this.design_setting.img_fit === "cover" ? 'cover' : 'contain';
            imageStyle.width = '100%';
            imageStyle.height = this.design_setting.img_fit === "cover" ? 'unset' : '100%';
            imageStyle.backgroundColor = this.design_setting.background_swatch_color
            return imageStyle;
        },
        getVariantPreviewArray(variant_array) {
            if (this.design_setting.maximum_number_of_variations !== undefined) {
                if (variant_array.length > this.design_setting.maximum_number_of_variations) {
                    this.num_of_extra_item = variant_array.length - this.design_setting.maximum_number_of_variations
                    let array = JSON.parse(JSON.stringify(variant_array))
                    array.splice(-this.num_of_extra_item)
                    return array
                }
                this.num_of_extra_item = 0
                return variant_array
            }
        },
        getImageStyle(item) {
            let style = {...this.imageSettings()}
            if (this.hovered_item !== null) {
                if (this.design_setting.hover_zoom_variant_image) {
                    if (this.hovered_item.item.label === item.label) {
                        style = {
                            ...style,
                            transition: 'transform .25s !important'
                        }
                        if (this.hovered_item.event.target.querySelectorAll('img')[0].width >= this.hovered_item.event.target.querySelectorAll('img')[0].height) {
                            style.transform = `translate(-50%, -50%) scale(${this.design_setting.hover_zoom_size})  !important`
                            this.hovered_item.event.target.querySelectorAll('img')[0].classList.add("imgWidthBigger");
                        } else {
                            style.transform = this.design_setting.img_position === 'center' ? `translate(-50%, -50%) scale(${this.design_setting.hover_zoom_size})  !important` : `scale(${this.design_setting.hover_zoom_size}) `
                            this.hovered_item.event.target.querySelectorAll('img')[0].classList.remove("imgWidthBigger");
                        }
                    }
                }
            }
            return style;
        },
        sortValuesByPosition(values) {
            let array = [];
            for (const variant of this.option_variant_info.values) {
                for (const variantElement of values) {
                    if (variant === variantElement.label) {
                        array.push(variantElement)
                        break
                    }
                }
            }
            return array;
        },
        changeVariant(item) {
            this.select_variant = item
            this.$emit('set_list_selected_variant', this.option_setting.name, item, true)
        },
        innerBorder(variant) {
            let borderRadius = ''

            if (this.select_variant === variant.label) {
                if (this.design_setting.display_style === "swatch_circle_in_square" || this.design_setting.display_style === 'circular_swatch') {
                    borderRadius = '50%'
                }
                if (this.design_setting.display_style !== "swatch_circle_in_square" && this.design_setting.display_style !== 'circular_swatch') {
                    borderRadius = this.design_setting.selected_inner_border_radius + 'px'
                }
                if (this.design_setting.display_style === 'square_swatch') {
                    return {
                        border: `${this.design_setting.selected_inner_border} ${this.design_setting.selected_inner_border_thickness}px solid`,
                        borderRadius: borderRadius,
                        maxHeight: this.design_setting.img_height + 'px',
                        maxWidth: this.design_setting.img_width + 'px',
                        height: '100%',
                        width: '100%'
                    }
                }
                let data = {
                    border: `${this.design_setting.selected_inner_border} ${this.design_setting.selected_inner_border_thickness}px solid`,
                    borderRadius: borderRadius,
                    height: this.design_setting.img_height + 'px',
                    width: this.design_setting.img_width + 'px'
                }
                if (this.design_setting.display_style === 'swatch_in_pill') {
                    data.minWidth = this.design_setting.img_width + 'px'
                }
                return data
            } else {
                if (this.design_setting.display_style === "swatch_circle_in_square" || this.design_setting.display_style === 'circular_swatch') {
                    borderRadius = '50%'
                }
                if (this.design_setting.display_style !== "swatch_circle_in_square" && this.design_setting.display_style !== 'circular_swatch') {
                    borderRadius = this.design_setting.unselected_inner_border_radius + 'px'
                }
                if (this.design_setting.display_style === 'square_swatch') {
                    return {
                        border: `${this.design_setting.unselected_inner_border} ${this.design_setting.unselected_inner_border_thickness}px solid`,
                        borderRadius: borderRadius,
                        maxHeight: this.design_setting.img_height + 'px',
                        maxWidth: this.design_setting.img_width + 'px',
                        height: '100%',
                        width: '100%'
                    }
                }
                let data = {
                    border: `${this.design_setting.unselected_inner_border} ${this.design_setting.unselected_inner_border_thickness}px solid`,
                    borderRadius: borderRadius,
                    height: this.design_setting.img_height + 'px',
                    width: this.design_setting.img_width + 'px'
                }
                if (this.design_setting.display_style === 'swatch_in_pill') {
                    data.minWidth = this.design_setting.img_width + 'px'
                }
                return data
            }
        },
        outerBorder(variant) {
            const isSelected = this.select_variant === variant.label;
            let isHovered = false
            if (this.hovered_item !== null) {
                isHovered = this.design_setting.hover_show_shadow && this.hovered_item.item.label === variant.label;
            }
            let borderStyle = isSelected ? this.design_setting.selected_outer_border : this.design_setting.unselected_outer_border;
            let borderWidth = isSelected ? this.design_setting.selected_outer_border_thickness : this.design_setting.unselected_outer_border_thickness;
            let borderRadius = this.design_setting.display_style === 'circular_swatch' ? '50%' : isSelected ? `${this.design_setting.selected_outer_border_radius}px` : `${this.design_setting.unselected_outer_border_radius}px`;

            let styleObject = {
                border: `${borderStyle} ${borderWidth}px solid`,
                borderRadius: borderRadius,
                height: `${this.design_setting.style_height}px`,
                width: `${this.design_setting.style_width}px`,

            };

            if (isHovered) {
                styleObject.boxShadow = `0px 0px ${this.design_setting.hover_shadow_blur}px ${this.design_setting.hover_shadow_thickness}px ${this.design_setting.hover_shadow}`;
            }

            return styleObject;
        },
        trackImage: function (e) {
            if (e.target) {
                if (e.target.width >= e.target.height) {

                    if (!e.target.classList.contains("imgWidthBigger")) {
                        e.target.classList.add("imgWidthBigger");
                    }
                    e.target.setAttribute('data-flag', 'true');
                } else {
                    if (e.target.style.transform !== "") {
                        e.target.style.transform = ""
                    }
                    if (e.target.style.transition !== '') {
                        e.target.style.transition = ""
                    }
                    if (e.target.classList.contains("imgWidthBigger")) {
                        e.target.classList.remove("imgWidthBigger")
                    }
                    e.target.setAttribute('data-flag', 'false');
                    let styles = this.imageSettings()
                    Object.keys(styles).forEach(style => {
                        e.target.style[style] = styles[style];
                    });

                }
            }

        },
        processVariantList(variant_list_processed) {
            if (this.variant_option !== undefined) {
                let card_product_variant_info = this.card_product_info.product.options
                this.option_setting = this.variant_option.option_setting
                this.design_setting = this.variant_option.design_setting
                this.option_variant_info = card_product_variant_info.filter(item => item.name === this.option_setting.name)[0]
                if (this.variant_option.hasOwnProperty('option_setting_color_custom_image')) {
                    this.option_setting_color_custom_image = this.variant_option.option_setting_color_custom_image
                    let variant_of_product_array = this.option_setting_color_custom_image.filter(item => {
                        return item.variant_option_name === this.option_variant_info.name && this.option_variant_info.values.includes(item.variant_option_value);
                    });
                    let option_variant_list = variant_of_product_array.map(item => {
                        let newItem = {
                            label: item.variant_option_value,
                            option_swatch: item.option_swatch,
                            swatch_img_url: item.swatch_img_url,
                            upload_img_url: item.upload_img_url,
                            color_code: item.color_code
                        };
                        return newItem;
                    });
                    this.list_variant = variant_list_processed.filter(item => this.option_setting.name === item.type)
                        .map(item => {
                            const firstItem = option_variant_list.find(fItem => fItem.label === item.label);
                            if (firstItem && firstItem.url_image) {
                                item.url_image = firstItem.url_image;
                            }
                            return {...item, ...firstItem};
                        });
                    this.list_variant = JSON.parse(JSON.stringify(this.sortValuesByPosition(this.list_variant)))
                } else {
                    this.list_variant = variant_list_processed
                        .filter(item => this.option_setting.name === item.type)
                    this.list_variant = JSON.parse(JSON.stringify(this.sortValuesByPosition(this.list_variant)))
                    // .sort((a, b) => {
                    //
                    //     const labelA = a.label;
                    //     const labelB = b.label;
                    //
                    //     const isNumericA = !isNaN(labelA);
                    //     const isNumericB = !isNaN(labelB);
                    //
                    //     if (isNumericA && isNumericB) {
                    //         return Number(labelA) - Number(labelB);
                    //     }
                    //
                    //     return labelA.localeCompare(labelB);
                    // });
                }


            }
        }
    },
    async mounted() {
        this.processVariantList(this.variant_list_processed)
        this.select_variant = this.object_selected_variant[this.option_setting.name]
        if ("url" in this.card_product_info) {
            this.product_url = location.origin + this.card_product_info.product.url
        }
        if ('limited_image' in this.design_setting && 'upload_image' in this.design_setting) {
            if (this.design_setting.limited_image === 'custom') {
                if (this.design_setting.upload_image !== '') {
                    this.backgroundLimitedImage = "https://app.nestscale.com" + this.design_setting.upload_image
                }
            }
        }
    }
}
</script>