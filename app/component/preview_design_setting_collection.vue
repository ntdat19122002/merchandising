<template>
    <div class="pv-preview" :style="{top: scrollPosition !== 0 ? '7rem':'0'}">

        <div style="background: white; padding: 20px; border-radius: 8px; overflow: hidden">
            <div class="pv-flex-column">
                <div class="pv-preview-title">Preview</div>
                <div class="pv-preview-main-container">
                    <div class="pv-variant-image-container">

                        <img v-if="designItemName === 'Swatch Circle in Square'"
                             :src="this.data_swatch_circle_in_square[selectSwatchCircleInSquareIndex].url_image"
                             class="pv-variant-image-selected">
                        <img v-else-if="designItemName === 'Circular Swatch'"
                             :src="this.data_swatch_circle_in_square[selectColorIndex].url_image"
                             class="pv-variant-image-selected">
                        <img v-else-if="designItemName === 'Square Swatch'"
                             :src="this.data_select_option[selectSquareSwatchIndex].url_img"
                             class="pv-variant-image-selected">

                    </div>
                    <div style="display: flex" class="pv-preview-name" v-if="design_setting.label_show"
                         :style="{fontSize: `${design_setting.label_size}px`, lineHeight:`${design_setting.label_size}px`}">
                        Color
                        <div>:&nbsp;{{ labelText }}</div>
                    </div>
                    <div class="pv-design-setting-square_swatch-block" style="width: 100%;"
                         v-if="designItemName === 'Square Swatch'">
                        <div style="display: flex; align-items: center"
                             :style="[{gap:`${design_setting.swatch_spacing}px`},getCollectionPosition]">
                            <div v-for="(item, index) in getVariantPreviewArray(data_select_option)"
                                 @click="selectSquareSwatch(index)"
                                 @mouseenter="hovered_item = index"
                                 @mouseleave="hovered_item = null">


                                <Tooltip color="#FFFFFF" placement="top"
                                         v-if="design_setting.hover_show_variant_description">
                                    <template #title>
                                        <span>{{ item.label }}</span>
                                    </template>
                                    <div class="pv-design-setting-square_swatch-item" :style="getStyle(index)">
                                        <div class="pv-design-setting-square_swatch-img-block"
                                             :style="{...(selectSquareSwatchIndex === index ? imgStyleSelected : imgStyleUnselected),backgroundColor:`${design_setting.background_swatch_color}`, maxHeight: `${design_setting.img_height}px`, maxWidth: `${design_setting.img_width}px`}">
                                            <img :src="item.url_img" alt=""
                                                 :style="[imgPosition,getImageStyle(index)]">
                                        </div>
                                    </div>
                                </Tooltip>


                                <div class="pv-design-setting-square_swatch-item" :style="getStyle(index)" v-else>
                                    <div class="pv-design-setting-square_swatch-img-block"
                                         :style="{...(selectSquareSwatchIndex === index ? imgStyleSelected : imgStyleUnselected),backgroundColor:`${design_setting.background_swatch_color}`, maxHeight: `${design_setting.img_height}px`, maxWidth: `${design_setting.img_width}px`}">
                                        <img :src="item.url_img" alt="" :style="[imgPosition,getImageStyle(index)]">
                                    </div>
                                </div>
                            </div>
                            <div v-if="num_of_extra_item !== 0">
                                <div @mouseenter="hovered_item = data_select_option.length - num_of_extra_item"
                                     @mouseleave="hovered_item = null"
                                     class="pv-design-setting-square_swatch-item"
                                     :style="getStyle(data_select_option.length - num_of_extra_item)">
                                    <div class="pv-design-setting-square_swatch-img-block"
                                         style="border: none !important;position: relative">
                                        <div
                                            :style="{
                                              ...(selectSquareSwatchIndex === data_select_option.length - num_of_extra_item ? imgStyleSelected : imgStyleUnselected),
                                              backgroundColor: design_setting.background_swatch_color,
                                              height: `${design_setting.img_height}px`,
                                              width: `${design_setting.img_width}px`,
                                              background: design_setting.image_overlay ?  `linear-gradient(0deg, rgba(0, 0, 0, 0.20) 0%, rgba(0, 0, 0, 0.20) 100%), url('${backgroundLimitedImage}') lightgray 50% / cover no-repeat` :  `linear-gradient(0deg, rgba(255, 255, 255, 0.40) 0%, rgba(255, 255, 255, 0.40) 100%), url('${backgroundLimitedImage}') lightgray 50% / cover no-repeat`
                                            }">
                                        </div>
                                        <div class="pv-plus-variant-hidden" :style="{color:design_setting.image_overlay ? '#FFFFFF' : ''}">+{{ num_of_extra_item }}</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="pv-design-setting-circular-swatch-block" v-if="designItemName === 'Circular Swatch'"
                         style="width: 100%"
                         :style="[{gap:`${design_setting.swatch_spacing}px`},getCollectionPosition]">
                        <div v-for="(color, index) in getVariantPreviewArray(list_color_data)"
                             @click="selectColor(index)"
                             @mouseenter="hovered_item = index"
                             @mouseleave="hovered_item = null">

                            <Tooltip color="#FFFFFF" placement="top"
                                     v-if="design_setting.hover_show_variant_description">
                                <template #title>
                                    <span>{{ color.label }}</span>
                                </template>
                                <div class="pv-circular-swatch-item"
                                     :style="getStyle(index)">
                                    <div
                                        :style="{opacity: color.value === list_color_data.length ? 0.5 : 1,backgroundColor:`${design_setting.background_swatch_color}`, height: `${design_setting.img_height}px`, width: `${design_setting.img_width}px`, ...(selectColorIndex === index ? imgStyleSelected : imgStyleUnselected)}"
                                        class="pv-circular-swatch-item-block-img">
                                        <img src="/nestprdvariant/static/images/design_setting/Vector72.png" alt=""
                                             class="pv-design-setting-circular-swatch-img-delete"
                                             :style="{opacity: color.value === list_color_data.length ? 1 : 0}">
                                        <img class="pv-design-setting-circular-swatch-img pv-preview-image"
                                             :src="color.url_image"
                                             alt="" :style="[getImageStyle(index), imgPosition]">
                                    </div>
                                </div>
                            </Tooltip>

                            <div class="pv-circular-swatch-item" v-else
                                 :style="getStyle(index)">
                                <div
                                    :style="{opacity: color.value === list_color_data.length ? 0.5 : 1,backgroundColor:`${design_setting.background_swatch_color}`, height: `${design_setting.img_height}px`, width: `${design_setting.img_width}px`, ...(selectColorIndex === index ? imgStyleSelected : imgStyleUnselected)}"
                                    class="pv-circular-swatch-item-block-img">
                                    <img src="/nestprdvariant/static/images/design_setting/Vector72.png" alt=""
                                         class="pv-design-setting-circular-swatch-img-delete"
                                         :style="{opacity: color.value === list_color_data.length ? 1 : 0}">
                                    <img class="pv-design-setting-circular-swatch-img pv-preview-image"
                                         :src="color.url_image"
                                         alt="" :style="[getImageStyle(index), imgPosition]">
                                </div>
                            </div>
                        </div>
                        <div v-if="num_of_extra_item !== 0">
                            <div @mouseenter="hovered_item = list_color_data.length - num_of_extra_item"
                                 @mouseleave="hovered_item = null"
                                 class="pv-design-setting-square_swatch-item"
                                 :style="getStyle(list_color_data.length - num_of_extra_item)">
                                <div class="pv-circular-swatch-item-block-img"
                                     style="border: none !important;position: relative">
                                    <div class="pv-design-setting-circular-swatch-img pv-preview-image"
                                         :style="{...(selectSquareSwatchIndex === data_select_option.length - num_of_extra_item ? imgStyleSelected : imgStyleUnselected),backgroundColor:`${design_setting.background_swatch_color}`, height: `${design_setting.img_height}px`, width: `${design_setting.img_width}px`,
                                         background: design_setting.image_overlay ?  `linear-gradient(0deg, rgba(0, 0, 0, 0.20) 0%, rgba(0, 0, 0, 0.20) 100%), url('${backgroundLimitedImage}') lightgray 50% / cover no-repeat` :  `linear-gradient(0deg, rgba(255, 255, 255, 0.40) 0%, rgba(255, 255, 255, 0.40) 100%), url('${backgroundLimitedImage}') lightgray 50% / cover no-repeat`}"></div>
                                    <div class="pv-plus-variant-hidden" :style="{color:design_setting.image_overlay ? '#FFFFFF' : ''}">+{{ num_of_extra_item }}</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="pv-design-setting-square_swatch-block pv-design-setting-swatch-circle-in-square-block"
                         style="width: 100%;"
                         v-if="designItemName === 'Swatch Circle in Square'">
                        <div style="display: flex; align-items: center"
                             :style="[{gap:`${design_setting.swatch_spacing}px`},getCollectionPosition]">
                            <div
                                v-for="(swatch_circle_in_square, index) in getVariantPreviewArray(data_swatch_circle_in_square)"
                                @mouseenter="hovered_item = index"
                                @mouseleave="hovered_item = null"
                                @click="selectSwatchCircleInSquare(index)">
                                <Tooltip color="#FFFFFF" placement="top"
                                         v-if="design_setting.hover_show_variant_description">
                                    <template #title>
                                        <span>{{ swatch_circle_in_square.color }}</span>
                                    </template>
                                    <div class="pv-design-setting-swatch-circle-in-square-item"
                                         :style="getStyle(index)">
                                        <div
                                            :style="{height: `${design_setting.img_height}px`,backgroundColor:`${design_setting.background_swatch_color}`, width: `${design_setting.img_width}px`, ...(selectSwatchCircleInSquareIndex === index ? imgStyleSelected : imgStyleUnselected)}"
                                            class="pv-design-setting-swatch-circle-in-square-img-block">
                                            <img :src="swatch_circle_in_square.url_image" alt=""
                                                 :style="[getImageStyle(index), imgPosition]">
                                        </div>
                                    </div>
                                </Tooltip>
                                <div v-else class="pv-design-setting-swatch-circle-in-square-item"
                                     :style="getStyle(index)">
                                    <div
                                        :style="{height: `${design_setting.img_height}px`,backgroundColor:`${design_setting.background_swatch_color}`, width: `${design_setting.img_width}px`, ...(selectSwatchCircleInSquareIndex === index ? imgStyleSelected : imgStyleUnselected)}"
                                        class="pv-design-setting-swatch-circle-in-square-img-block">
                                        <img :src="swatch_circle_in_square.url_image" alt=""
                                             :style="[getImageStyle(index), imgPosition]">
                                    </div>
                                </div>
                            </div>
                            <div v-if="num_of_extra_item !== 0">
                                <div
                                    @mouseenter="hovered_item = data_swatch_circle_in_square.length - num_of_extra_item"
                                    @mouseleave="hovered_item = null"
                                    class="pv-design-setting-square_swatch-item"
                                    :style="getStyle(data_swatch_circle_in_square.length - num_of_extra_item)">
                                    <div class="pv-design-setting-swatch-circle-in-square-img-block"
                                         style="border: none !important;position: relative">
                                        <div
                                            :style="{...(selectSquareSwatchIndex === data_select_option.length - num_of_extra_item ? imgStyleSelected : imgStyleUnselected),backgroundColor:`${design_setting.background_swatch_color}`, height: `${design_setting.img_height}px`, width: `${design_setting.img_width}px`
                                            ,background: design_setting.image_overlay ?  `linear-gradient(0deg, rgba(0, 0, 0, 0.20) 0%, rgba(0, 0, 0, 0.20) 100%), url('${backgroundLimitedImage}') lightgray 50% / cover no-repeat` :  `linear-gradient(0deg, rgba(255, 255, 255, 0.40) 0%, rgba(255, 255, 255, 0.40) 100%), url('${backgroundLimitedImage}') lightgray 50% / cover no-repeat`}">
                                        </div>
                                        <div class="pv-plus-variant-hidden" :style="{color:design_setting.image_overlay ? '#FFFFFF' : ''}">+{{
                                                num_of_extra_item
                                            }}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="pv-preview-money">$10.00 SGD</div>
                </div>


            </div>
        </div>
    </div>
</template>
<script>
import {Select, SelectOption, Tooltip} from "ant-design-vue"

export default {
    name: 'PreviewDesignSettingCollection',
    components: {SelectOption, Select, Tooltip},
    data() {
        return {
            select_option: 1,
            selected_option: {
                value: 1,
                label: "Baby Pink Buckled Flatform Sandals",
                url_img: '/nestprdvariant/static/images/design_setting/preview_design_setting/360e319423a9198a82efa471f5487300.png'
            },
            list_color_data: [{
                value: 1,
                label: 'Hot Pink',
                url_image: '/nestprdvariant/static/images/design_setting/HotPink.png'
            }, {
                value: 2,
                label: 'Goldenrod ',
                url_image: '/nestprdvariant/static/images/design_setting/Goldenrod.png'
            }, {
                value: 3,
                label: 'Sky Blue',
                url_image: '/nestprdvariant/static/images/design_setting/SkyBlue.png'
            }, {
                value: 4,
                label: 'Olive Drab',
                url_image: '/nestprdvariant/static/images/design_setting/OliveDrab.png'
            }, {
                value: 5,
                label: 'Medium Purple',
                url_image: '/nestprdvariant/static/images/design_setting/MediumPurple.png'
            }, {
                value: 6,
                label: 'Light Salmon',
                url_image: '/nestprdvariant/static/images/design_setting/LightSalmon.png'
            },],
            data_select_option: [{
                value: 1,
                label: "Baby Pink Buckled Flatform Sandals",
                url_img: '/nestprdvariant/static/images/design_setting/preview_design_setting/360e319423a9198a82efa471f5487300.png'
            }, {
                url_img: '/nestprdvariant/static/images/design_setting/preview_design_setting/b5db6ab0fae1f58595559cc432b10e7f.jpeg',
                label: 'Lilac Purple Buckled Flatform Sandals',
                value: 2
            }, {
                value: 3,
                label: "Sand Brown Pink Buckled Flatform Sandals",
                url_img: "/nestprdvariant/static/images/design_setting/preview_design_setting/e49abe93ef9e2c16f65cf8969100d9f6.png"
            }, {
                value: 4,
                url_img: '/nestprdvariant/static/images/design_setting/preview_design_setting/7c010d272cd9c537ebbddbd637222a62.png',
                label: "Light Green Buckled Flatform Sandals"
            }, {
                value: 5,
                url_img: '/nestprdvariant/static/images/design_setting/preview_design_setting/ec8406eafffaabdba2d3b1514fcf82df.jpeg',
                label: "Sky Blue Buckled Flatform Sandals"
            }],
            selectSquareSwatchIndex: 0,
            selectedSquareSwatch: {
                value: 1,
                label: "Baby Pink Buckled Flatform Sandals",
                url_img: '/nestprdvariant/static/images/design_setting/preview_design_setting/360e319423a9198a82efa471f5487300.png'
            },
            data_swatch_circle_in_square: [{
                url_image: "/nestprdvariant/static/images/design_setting/SwatchCircleInSquare/preview/4849e1de32b87254df2d8bb093004661.png",
                color: 'Hot Pink', value: 1
            }, {
                value: 2, color: "Goldenrod",
                url_image: '/nestprdvariant/static/images/design_setting/SwatchCircleInSquare/preview/f7d37766d79868705218ac4cc8417451.png'

            }, {
                value: 3, color: 'Sky Blue',
                url_image: "/nestprdvariant/static/images/design_setting/SwatchCircleInSquare/preview/e0b5513878d6681bba549da756013883.png"
            }, {
                url_image: '/nestprdvariant/static/images/design_setting/SwatchCircleInSquare/preview/06806a1319de29107fa80de4a25aabf3.png',
                value: 4, color: 'Olive Drab'
            }, {
                url_image: '/nestprdvariant/static/images/design_setting/SwatchCircleInSquare/preview/c1c9acb854db58fe9fc4f107e0aa9734.png',
                value: 5, color: 'Medium Purple'
            }, {
                url_image: '/nestprdvariant/static/images/design_setting/SwatchCircleInSquare/preview/a2171f7bb1f88673536c27ae92a23803.png',
                value: 6, color: 'Salmon'
            }],
            selectSwatchCircleInSquareIndex: 0,
            selectedSwatchCircleInSquare: {
                url_image: "/nestprdvariant/static/images/design_setting/SwatchCircleInSquare/preview/4849e1de32b87254df2d8bb093004661.png",
                color: 'Hot Pink', value: 1
            },
            selectColorIndex: 0,
            selectedColor: {
                value: 1,
                label: 'Hot Pink',
                url_image: '/nestprdvariant/static/images/design_setting/HotPink.png'
            },
            hovered_item: null,
            num_of_extra_item: 0,

        }
    },
    props: {
        temp_data: Object,
        designItemName: String,
        design_setting: Object,
        scrollPosition: Number
    },
    watch: {
        'design_setting.upload_image'() {

        },
    },
    methods: {
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
        getImageStyle(index) {
            let style = {
                backgroundColor: this.design_setting.background_swatch_color,
                transition: 'transform .25s'
            };
            if (this.design_setting.hover_zoom_variant_image && this.hovered_item === index) {
                const zoomSize = `scale(${this.design_setting.hover_zoom_size})`;
                if (this.design_setting.img_fit === 'cover') {
                    switch (this.design_setting.img_position) {
                        case 'center':
                            if (this.designItemName === 'Square Swatch') {
                                style.transform = `translate(-50%, -50%) ${zoomSize} !important`;
                            } else {
                                style.width = `${parseFloat(this.design_setting.hover_zoom_size) * 100}%`;
                                style.transition = "all 0.25s ease";
                            }
                            break;
                        case 'top':
                        case 'bottom':
                            style.transform = zoomSize;
                            break;
                    }
                } else {
                    style.transform = zoomSize;
                }
            }
            return style;
        },

        getStyle(index) {
            let style = null
            if (this.designItemName === 'Swatch Circle in Square') {
                if (this.selectSwatchCircleInSquareIndex === index) {
                    style = this.divStyleSelected;
                } else {
                    style = this.divStyleUnselected;
                }
            } else if (this.designItemName === 'Swatch in Box') {
                style = {
                    height: `${this.design_setting.style_height}px`,
                    width: `${this.design_setting.style_width}px`, ...(this.selectColorIndex === index ? this.divStyleSelected : this.divStyleUnselected)
                }
            } else if (this.designItemName === 'Circular Swatch') {
                if (this.selectColorIndex === index) {
                    style = this.divStyleSelected;
                } else {
                    style = this.divStyleUnselected;
                }
            } else if (this.designItemName === 'Square Swatch') {
                if (this.selectSquareSwatchIndex === index) {
                    style = this.divStyleSelected;
                } else {
                    style = this.divStyleUnselected;
                }
            } else if (this.designItemName === 'Swatch in Pill') {
                style = {
                    ...(this.selectColorIndex === index ? this.divStyleSelected : this.divStyleUnselected),
                    padding: `0 ${this.design_setting.border_spacing}px`
                }
            }
            if (this.design_setting.hover_show_shadow === true) {
                if (this.hovered_item === index) {
                    style = {
                        ...style,
                        boxShadow: `0px 0px ${this.design_setting.hover_shadow_blur}px ${this.design_setting.hover_shadow_thickness}px ${this.design_setting.hover_shadow}`
                    };
                }
            }

            return style;
        },
        selectSwatchCircleInSquare(index) {
            this.selectSwatchCircleInSquareIndex = index
            for (let item of this.data_swatch_circle_in_square) {
                if (index + 1 == item.value) {
                    this.selectedSwatchCircleInSquare = item
                }
            }
        },
        selectSquareInDropdown() {
            for (let option of this.data_select_option) {
                if (option.value === this.select_option) {
                    this.selected_option = JSON.parse(JSON.stringify(option))
                }
            }
        },
        selectSquareSwatch(index) {
            this.selectSquareSwatchIndex = index
            for (let item of this.data_select_option) {
                if (item.value == index + 1) {
                    this.selectedSquareSwatch = item
                }
            }
        },
        selectColor(index) {
            this.selectColorIndex = index
            for (let color of this.list_color_data) {
                if (color.value == index + 1) {
                    this.selectedColor = color
                }
            }
        }
    },
    computed: {
        backgroundLimitedImage() {
            if (this.design_setting.limited_image === 'custom') {
                if (Object.keys(this.temp_data).length !== 0) {
                    return this.temp_data.imgData
                } else if (this.design_setting.upload_image !== '') {
                    return this.design_setting.upload_image
                }
            }
            return 'https://app.nestscale.com/nestprdvariant/static/images/rainbow.png'
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
        generateToolTipHeight() {
            return this.design_setting.img_height * 2 * (parseInt(this.design_setting.hover_scaling_size) / 100)
        },
        generateToolTipWidth() {
            return this.design_setting.img_width * 2 * (parseInt(this.design_setting.hover_scaling_size) / 100)
        },
        divStyleSelected() {
            let data = {
                border: `${this.design_setting.selected_outer_border} ${this.design_setting.selected_outer_border_thickness}px solid !important`,
                borderRadius: `${this.design_setting.selected_outer_border_radius}px !important`,
                height: `${this.design_setting.style_height}px !important`,
                width: `${this.design_setting.style_width}px !important`,
                padding: `${this.design_setting.border_spacing}px`,
                transition: 'border 0.1s ease-in-out'
            }
            if (this.designItemName === 'Circular Swatch') {
                data.borderRadius = '50% !important'
            }
            if (this.designItemName === 'Swatch in Box') {
                data.padding = 'unset'
                data.paddingTop = `${this.design_setting.border_spacing}px`
            }
            return data
        },
        divStyleUnselected() {
            let data = {
                border: `${this.design_setting.unselected_outer_border} ${this.design_setting.unselected_outer_border_thickness}px solid !important`,
                borderRadius: `${this.design_setting.unselected_outer_border_radius}px !important`,
                height: `${this.design_setting.style_height}px !important`,
                width: `${this.design_setting.style_width}px !important`,
                padding: `${this.design_setting.border_spacing}px`,
                transition: 'border 0.1s ease-in-out'
            }
            if (this.designItemName === 'Circular Swatch') {
                data.borderRadius = '50% !important'
            }
            if (this.designItemName === 'Swatch in Box') {
                data.padding = 'unset'
                data.paddingTop = `${this.design_setting.border_spacing}px`
            }
            return data
        },
        imgStyleSelected() {
            if (this.designItemName === 'Circular Swatch' || this.designItemName === 'Swatch Circle in Square') {
                return {
                    border: `${this.design_setting.selected_inner_border} ${this.design_setting.selected_inner_border_thickness}px solid !important`,
                    borderRadius: '50% !important'
                }
            }
            return {
                border: `${this.design_setting.selected_inner_border} ${this.design_setting.selected_inner_border_thickness}px solid !important`,
                borderRadius: `${this.design_setting.selected_inner_border_radius}px !important`
            }
        },
        imgStyleUnselected() {
            if (this.designItemName === 'Circular Swatch' || this.designItemName === 'Swatch Circle in Square') {
                return {
                    border: `${this.design_setting.unselected_inner_border} ${this.design_setting.unselected_inner_border_thickness}px solid !important`,
                    borderRadius: '50% !important'
                }
            }
            return {
                border: `${this.design_setting.unselected_inner_border} ${this.design_setting.unselected_inner_border_thickness}px solid !important`,
                borderRadius: `${this.design_setting.unselected_inner_border_radius}px !important`
            }
        },
        imgPosition() {
            let height = 'unset !important'
            if (this.design_setting.img_fit === "cover") {
                if (this.design_setting.img_position === "center") {
                    return {
                        'top': '50%',
                        'left': '50%',
                        'transform': this.designItemName === "Circular Swatch" ? 'none !important' : 'translate(-50%, -50%)',
                        'objectFit': 'cover',
                        'height': height
                    }
                }
                if (this.design_setting.img_position === 'bottom') {
                    return {
                        'bottom': 0,
                        'objectFit': 'cover',
                        'height': height
                    }
                }
                if (this.design_setting.img_position === 'top') {
                    return {
                        'top': 0,
                        'height': height,
                        'objectFit': 'cover'
                    }
                }
            } else {
                height = '100% !important'
                return {
                    'height': height,
                    'objectFit': 'contain'
                }
            }
        },
        labelText() {
            let label = ''
            if (this.designItemName === "Square Swatch") {
                label = this.selectedSquareSwatch.label
            }
            if (this.designItemName === 'Swatch in Dropdown') {
                label = this.selected_option.label
            }
            if (this.designItemName === 'Swatch Circle in Square') {
                label = this.selectedSwatchCircleInSquare.color
            }
            if (this.designItemName === 'Swatch in Box' || this.designItemName === "Swatch in Pill" || this.designItemName === "Circular Swatch") {
                label = this.selectedColor.label
            }

            if (this.design_setting.label_case === "uppercase") {
                return label.toUpperCase()
            }
            if (this.design_setting.label_case === "lowercase") {
                return label.toLowerCase()
            }
            if (this.design_setting.label_case === "default") {
                return label
            }
        }
    }
}
</script>