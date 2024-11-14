<template>
    <div class="pv-preview" :style="{top: scrollPosition !== 0 ? '7rem':'0'}">
        <div v-if="designItemName === 'Swatch in Dropdown'"
             style="background: white; padding: 20px; border-radius: 8px; overflow: hidden">
            <div class="pv-flex-column">
                <div class="pv-preview-title">Preview</div>
                <div style="display: flex" class="pv-preview-name"
                     :style="{fontSize: `${design_setting.label_size}px`, lineHeight:`${design_setting.label_size}px`}">
                    Color
                    <div v-if="design_setting.label_show">:&nbsp;{{ labelText }}</div>
                </div>
                <div class="pv-design-setting-swatch-in-dropdown-block" style="overflow: hidden; flex-wrap: unset"
                     :style="{
                         border: `${design_setting.dropdown_outer_border_thickness}px ${design_setting.dropdown_outer_border} solid`,
                         borderRadius: `${design_setting.dropdown_outer_border_radius}px`,
                         height: `${design_setting.style_height}px`
                     }">
                    <Select
                        @change="selectSquareInDropdown"
                        style="width: 100%"
                        v-model:value="select_option"
                        :style="{height: `${design_setting.style_height}px !important`}"
                        class="pv-select-swatch- in-box pv-preview-design-setting">

                        <template #default>
                            <SelectOption v-for="option in data_select_option" :value="option.value"
                                          :key="option.value">
                                <div class="pv-select-drop-down" style="width: 95%;"
                                     :style="{padding: `${design_setting.border_spacing}px 0 ${design_setting.border_spacing}px ${design_setting.border_spacing}px`}">
                                    <div
                                        style="display: flex; align-items: center; justify-content: space-between; width: 100%;">
                                        <div
                                            style="position: relative; overflow: hidden; display: flex; align-items: center;"
                                            :style="{
                                                backgroundColor:`${design_setting.background_swatch_color}`,
                                                minHeight:`${design_setting.img_height}px`,
                                                minWidth:`${design_setting.img_width}px`,
                                                height: `${design_setting.img_height}px`,
                                                width: `${design_setting.img_width}px`,
                                                borderRadius: `${design_setting.dropdown_inner_border_radius}px`,
                                                border: `${design_setting.dropdown_inner_border} solid ${design_setting.dropdown_inner_border_thickness}px`
                                            }">
                                            <img
                                                :style="{...(imgPosition), backgroundColor:`${design_setting.background_swatch_color}`}"
                                                :src="option.url_img"
                                                alt=""
                                            >
                                        </div>
                                        <div style="flex: 3; padding-left: 10px;overflow: hidden;text-overflow: ellipsis;">
                                            {{ option.label }}
                                        </div>
                                        <div v-if="design_setting.show_price" class="pv-price-text" style="flex: 1; text-align: right; padding-left: 10px;">
                                            {{ option.price }}
                                        </div>
                                    </div>
                                </div>
                            </SelectOption>
                        </template>
                    </Select>
                </div>
            </div>
        </div>
        <div v-if=" designItemName !== 'Swatch in Dropdown'"
             style="background: white; padding: 20px; border-radius: 8px; overflow: hidden">
            <div class="pv-flex-column">
                <div class="pv-preview-title">Preview</div>
                <div style="display: flex" class="pv-preview-name"
                     :style="{fontSize: `${design_setting.label_size}px`, lineHeight:`${design_setting.label_size}px`}">
                    Color
                    <div v-if="design_setting.label_show">:&nbsp;{{ labelText }}</div>
                </div>
                <div class="pv-design-setting-square_swatch-block" v-if="designItemName === 'Square Swatch'">
                    <div style="display: flex; align-items: center"
                         :style="{gap: `${design_setting.swatch_spacing}px`}">
                        <div v-for="(item, index) in data_select_option" @click="selectSquareSwatch(index)"
                             @mouseenter="hovered_item = index"
                             @mouseleave="hovered_item = null">
                            <Tooltip color="#FFFFFF"
                                     v-if="design_setting.hover_show_variant_description && !design_setting.hover_show_tooltip">
                                <template #title>
                                    <span>{{ item.label }}</span>
                                </template>
                                <div class="pv-design-setting-square_swatch-item"
                                     :style="[selectSquareSwatchIndex === index ? divStyleSelected : divStyleUnselected,getHoverStyle(index)]">
                                    <div class="pv-design-setting-square_swatch-img-block"
                                         :style="{...(selectSquareSwatchIndex === index ? imgStyleSelected : imgStyleUnselected),backgroundColor:`${design_setting.background_swatch_color}`, maxHeight: `${design_setting.img_height}px`, maxWidth: `${design_setting.img_width}px`}">
                                        <img :src="item.url_img" alt="" :style="getImageStyle(index)">
                                    </div>
                                </div>
                            </Tooltip>

                            <Tooltip color="#FFFFFF"
                                     v-else-if="design_setting.hover_show_tooltip">


                                <template #title
                                          v-if="design_setting.hover_show_variant_description">

                                    <div class="pv-swatch_circle_in_square">
                                        <div v-if="design_setting.hover_show_variant_description" style="color: #333"
                                             :style="{ width: `${generateToolTipHeight}px`}"
                                             class="pv-flex-row-center">
                                            {{ item.label }}
                                        </div>
                                        <div
                                            :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`,backgroundColor: `${design_setting.background_swatch_color}`}">
                                            <img :src="item.url_img"
                                                 alt="" style="width: 100%; z-index: 999"
                                                 class="pv-img pv-imgWidthBigger" :style="imgPosition">
                                        </div>
                                    </div>
                                </template>
                                <div class="pv-design-setting-square_swatch-item"
                                     :style="[selectSquareSwatchIndex === index ? divStyleSelected : divStyleUnselected,getHoverStyle(index)]">
                                    <div class="pv-design-setting-square_swatch-img-block"
                                         :style="{...(selectSquareSwatchIndex === index ? imgStyleSelected : imgStyleUnselected),backgroundColor:`${design_setting.background_swatch_color}`, maxHeight: `${design_setting.img_height}px`, maxWidth: `${design_setting.img_width}px`}">
                                        <img :src="item.url_img" alt="" :style="getImageStyle(index)"
                                        >
                                    </div>
                                </div>
                            </Tooltip>


                            <div class="pv-design-setting-square_swatch-item"
                                 :style="[selectSquareSwatchIndex === index ? divStyleSelected : divStyleUnselected,getHoverStyle(index)]"
                                 v-else>
                                <div class="pv-design-setting-square_swatch-img-block"
                                     :style="{...(selectSquareSwatchIndex === index ? imgStyleSelected : imgStyleUnselected),backgroundColor:`${design_setting.background_swatch_color}`, maxHeight: `${design_setting.img_height}px`, maxWidth: `${design_setting.img_width}px`}">
                                    <img :src="item.url_img" alt="" :style="getImageStyle(index)"
                                    >
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="pv-design-setting-square_swatch-block pv-design-setting-swatch-in-box-block"
                     v-if="designItemName === 'Swatch in Box'">
                    <div style="display: flex" :style="{'gap': `${design_setting.swatch_spacing}px`}">
                        <div v-for="(color, index) in list_color_data"
                             @mouseenter="hovered_item = index"
                             @mouseleave="hovered_item = null"
                             @click="selectColor(index)">
                            <Tooltip color="#FFFFFF"
                                     v-if="design_setting.hover_show_variant_description && !design_setting.hover_show_tooltip">
                                <template #title>
                                    <span>{{ color.label }}</span>
                                </template>
                                <div class="pv-flex-column pv-swatch-in-box-item"
                                     :style="[selectColorIndex === index ? divStyleSelected : divStyleUnselected,getHoverStyle(index)]">
                                    <div class="pv-design-setting-swatch-in-box-item"
                                         :style="{...(selectColorIndex === index ? imgStyleSelected : imgStyleUnselected),backgroundColor:`${design_setting.background_swatch_color}`, height: `${design_setting.img_height}px`, width: `${design_setting.img_width}px`}">
                                        <img :src="color.url" alt="" :style="getImageStyle(index)"
                                        >
                                    </div>
                                    <div>{{ color.label }}</div>
                                    <div class="pv-price-text" v-if="design_setting.show_price">
                                        ${{ generateNumber(index) }}
                                    </div>
                                </div>
                            </Tooltip>

                            <Tooltip color="#FFFFFF"
                                     :overlayStyle="{padding:'8px',border:'1px #D9D9D9',}"
                                     v-else-if="design_setting.hover_show_tooltip">
                                <template #title>
                                    <div class="pv-swatch_circle_in_square">
                                        <div v-if="design_setting.hover_show_variant_description" style="color: #333"
                                             :style="{ width: `${generateToolTipHeight}px`}"
                                             class="pv-flex-row-center">
                                            {{ color.label }}
                                        </div>
                                        <div style="overflow: hidden"
                                             :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`,backgroundColor: `${design_setting.background_swatch_color}`}">
                                            <img :src="color.url"
                                                 alt="" style="width: 100%; z-index: 999;position: absolute"
                                                 :style="imgPosition">
                                        </div>
                                    </div>
                                </template>
                                <div class="pv-flex-column pv-swatch-in-box-item"
                                     :style="[selectColorIndex === index ? divStyleSelected : divStyleUnselected,getHoverStyle(index)]">
                                    <div class="pv-design-setting-swatch-in-box-item"
                                         :style="{...(selectColorIndex === index ? imgStyleSelected : imgStyleUnselected),backgroundColor:`${design_setting.background_swatch_color}`, height: `${design_setting.img_height}px`, width: `${design_setting.img_width}px`}">
                                        <img :src="color.url" alt="" :style="getImageStyle(index)"
                                        >
                                    </div>
                                    <div>{{ color.label }}</div>
                                    <div class="pv-price-text" v-if="design_setting.show_price">
                                        ${{ generateNumber(index) }}
                                    </div>
                                </div>
                            </Tooltip>

                            <div class="pv-flex-column pv-swatch-in-box-item" v-else
                                 :style="[selectColorIndex === index ? divStyleSelected : divStyleUnselected,getHoverStyle(index)]">
                                <div class="pv-design-setting-swatch-in-box-item"
                                     :style="{...(selectColorIndex === index ? imgStyleSelected : imgStyleUnselected),backgroundColor:`${design_setting.background_swatch_color}`, height: `${design_setting.img_height}px`, width: `${design_setting.img_width}px`}">
                                    <img :src="color.url" alt="" :style="getImageStyle(index)">
                                </div>
                                <div>{{ color.label }}</div>
                                <div class="pv-price-text" v-if="design_setting.show_price">
                                    ${{ generateNumber(index) }}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="pv-design-setting-circular-swatch-block" v-if="designItemName === 'Circular Swatch'"
                     :style="{gap: `${design_setting.swatch_spacing}px`}">
                    <div v-for="(color, index) in list_color_data" @click="selectColor(index)"
                         @mouseenter="hovered_item = index"
                         @mouseleave="hovered_item = null">

                        <Tooltip color="#FFFFFF"
                                 v-if="design_setting.hover_show_variant_description && !design_setting.hover_show_tooltip">
                            <template #title>
                                <span>{{ color.label }}</span>
                            </template>
                            <div class="pv-circular-swatch-item"
                                 :style="[selectColorIndex === index ? divStyleSelected : divStyleUnselected,getHoverStyle(index)]">
                                <div
                                    :style="{opacity: color.value === list_color_data.length ? 0.5 : 1,backgroundColor:`${design_setting.background_swatch_color}`, height: `${design_setting.img_height}px`, width: `${design_setting.img_width}px`, ...(selectColorIndex === index ? imgStyleSelected : imgStyleUnselected)}"
                                    class="pv-circular-swatch-item-block-img">
                                    <img src="/nestprdvariant/static/images/design_setting/Vector72.png" alt=""
                                         class="pv-design-setting-circular-swatch-img-delete"
                                         :style="{opacity: color.value === list_color_data.length ? 1 : 0}">
                                    <img class="pv-design-setting-circular-swatch-img" :src="color.url"
                                         style="position: relative"
                                         alt="" :style="getImageStyle(index)">
                                </div>
                            </div>
                        </Tooltip>

                        <Tooltip color="#FFFFFF"
                                 :overlayStyle="{padding:'8px',border:'1px #D9D9D9',}"
                                 v-else-if="design_setting.hover_show_tooltip">
                            <template #title>
                                <div class="pv-swatch_circle_in_square">
                                    <div v-if="design_setting.hover_show_variant_description" style="color: #333"
                                         :style="{ width: `${generateToolTipHeight}px`}"
                                         class="pv-flex-row-center">
                                        {{ color.label }}
                                    </div>
                                    <div style="overflow: hidden"
                                         :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`,backgroundColor: `${design_setting.background_swatch_color}`}">
                                        <img :src="color.url"
                                             alt="" style="width: 100%; z-index: 999;position: absolute"
                                             :style="imgPosition">
                                    </div>
                                </div>
                            </template>
                            <div class="pv-circular-swatch-item"
                                 :style="[selectColorIndex === index ? divStyleSelected : divStyleUnselected,getHoverStyle(index)]">
                                <div
                                    :style="{opacity: color.value === list_color_data.length ? 0.5 : 1,backgroundColor:`${design_setting.background_swatch_color}`, height: `${design_setting.img_height}px`, width: `${design_setting.img_width}px`, ...(selectColorIndex === index ? imgStyleSelected : imgStyleUnselected)}"
                                    class="pv-circular-swatch-item-block-img">
                                    <img src="/nestprdvariant/static/images/design_setting/Vector72.png" alt=""
                                         class="pv-design-setting-circular-swatch-img-delete"
                                         :style="{opacity: color.value === list_color_data.length ? 1 : 0}">
                                    <img class="pv-design-setting-circular-swatch-img" :src="color.url"
                                         style="position: relative"
                                         alt="" :style="getImageStyle(index)">
                                </div>
                            </div>
                        </Tooltip>
                        <div class="pv-circular-swatch-item" v-else
                             :style="[selectColorIndex === index ? divStyleSelected : divStyleUnselected,getHoverStyle(index)]">
                            <div
                                :style="{opacity: color.value === list_color_data.length ? 0.5 : 1,backgroundColor:`${design_setting.background_swatch_color}`, height: `${design_setting.img_height}px`, width: `${design_setting.img_width}px`, ...(selectColorIndex === index ? imgStyleSelected : imgStyleUnselected)}"
                                class="pv-circular-swatch-item-block-img">
                                <img src="/nestprdvariant/static/images/design_setting/Vector72.png" alt=""
                                     class="pv-design-setting-circular-swatch-img-delete"
                                     :style="{opacity: color.value === list_color_data.length ? 1 : 0}">
                                <img class="pv-design-setting-circular-swatch-img" :src="color.url"
                                     style="position: relative"
                                     alt="" :style="getImageStyle(index)">
                            </div>
                        </div>
                    </div>
                </div>
                <div class="pv-design-setting-square_swatch-block pv-design-setting-swatch-circle-in-square-block"
                     v-if="designItemName === 'Swatch Circle in Square'">
                    <div style="display: flex; align-items: center" :style="{gap:`${design_setting.swatch_spacing}px`}">
                        <div v-for="(swatch_circle_in_square, index) in data_swatch_circle_in_square"
                             @mouseenter="hovered_item = index"
                             @mouseleave="hovered_item = null"
                             @click="selectSwatchCircleInSquare(index)">
                            <Tooltip color="#FFFFFF"
                                     v-if="design_setting.hover_show_variant_description && !design_setting.hover_show_tooltip">
                                <template #title>
                                    <span>{{ swatch_circle_in_square.color }}</span>
                                </template>
                                <div class="pv-design-setting-swatch-circle-in-square-item"
                                     :style="[selectSwatchCircleInSquareIndex === index ? divStyleSelected : divStyleUnselected,getHoverStyle(index)]">
                                    <div
                                        :style="{height: `${design_setting.img_height}px`,backgroundColor:`${design_setting.background_swatch_color}`, width: `${design_setting.img_width}px`, ...(selectSwatchCircleInSquareIndex === index ? imgStyleSelected : imgStyleUnselected)}"
                                        class="pv-design-setting-swatch-circle-in-square-img-block">
                                        <img :src="swatch_circle_in_square.url" alt="" :style="getImageStyle(index)">
                                    </div>
                                </div>
                            </Tooltip>

                            <Tooltip color="#FFFFFF"
                                     :overlayStyle="{padding:'8px',border:'1px #D9D9D9',}"
                                     v-else-if="design_setting.hover_show_tooltip">
                                <template #title>
                                    <div class="pv-swatch_circle_in_square">
                                        <div v-if="design_setting.hover_show_variant_description" style="color: #333"
                                             :style="{ width: `${generateToolTipHeight}px`}"
                                             class="pv-flex-row-center">
                                            {{ swatch_circle_in_square.color }}
                                        </div>

                                        <div style="overflow: hidden"
                                             :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`,backgroundColor: `${design_setting.background_swatch_color}`}">
                                            <img :src="swatch_circle_in_square.url"
                                                 alt="" style="width: 100%; z-index: 999;position: absolute"
                                                 :style="imgPosition">
                                        </div>
                                    </div>
                                </template>
                                <div class="pv-design-setting-swatch-circle-in-square-item"
                                     :style="[selectSwatchCircleInSquareIndex === index ? divStyleSelected : divStyleUnselected,getHoverStyle(index)]">
                                    <div
                                        :style="{height: `${design_setting.img_height}px`,backgroundColor:`${design_setting.background_swatch_color}`, width: `${design_setting.img_width}px`, ...(selectSwatchCircleInSquareIndex === index ? imgStyleSelected : imgStyleUnselected)}"
                                        class="pv-design-setting-swatch-circle-in-square-img-block">
                                        <img :src="swatch_circle_in_square.url" alt=""
                                             :style="getImageStyle(index)">
                                    </div>
                                </div>
                            </Tooltip>
                            <div v-else class="pv-design-setting-swatch-circle-in-square-item"
                                 :style="[selectSwatchCircleInSquareIndex === index ? divStyleSelected : divStyleUnselected,getHoverStyle(index)]">
                                <div
                                    :style="{height: `${design_setting.img_height}px`,backgroundColor:`${design_setting.background_swatch_color}`, width: `${design_setting.img_width}px`, ...(selectSwatchCircleInSquareIndex === index ? imgStyleSelected : imgStyleUnselected)}"
                                    class="pv-design-setting-swatch-circle-in-square-img-block">
                                    <img :src="swatch_circle_in_square.url" alt=""
                                         :style="getImageStyle(index)">
                                </div>
                            </div>
                        </div>


                    </div>
                </div>
                <div class="pv-design-setting-square_swatch-block pv-design-setting-swatch-in-pill-block"
                     v-if="designItemName === 'Swatch in Pill'">
                    <div style="display: flex; align-items: center"
                         :style="{gap: `${design_setting.swatch_spacing}px`}">
                        <div v-for="(color, index) in list_color_data" @click="selectColor(index)"
                             @mouseenter="hovered_item = index"
                             @mouseleave="hovered_item = null">

                            <Tooltip color="#FFFFFF"
                                     v-if="design_setting.hover_show_variant_description && !design_setting.hover_show_tooltip">
                                <template #title>
                                    <span>{{ color.label }}</span>
                                </template>
                                <div class="pv-design-setting-swatch-in-pill-item"
                                     :style="[selectColorIndex === index ? divStyleSelected : divStyleUnselected,getHoverStyle(index)]">
                                    <div class="pv-design-setting-swatch-in-pill-img-block" style="gap: 5px">
                                        <div style="position: relative; align-items: center; overflow: hidden"
                                             :style="{...(selectColorIndex === index ? imgStyleSelected : imgStyleUnselected),backgroundColor:`${design_setting.background_swatch_color}`, height: `${design_setting.img_height}px`, width: `${design_setting.img_width}px`}">
                                            <img :src="color.url" alt=""
                                                 :style="getImageStyle(index)"
                                                 style="padding: 0 !important; position: absolute; height: 200%; width: 200%; transform: translate(-50%, -50%); top: 50%; left: 50%">
                                        </div>
                                        <div class="pv-img-name"
                                             style="max-width: 90px; display: -webkit-box !important; width: max-content !important">
                                            {{ color.label }}
                                        </div>
                                    </div>
                                </div>
                            </Tooltip>

                            <Tooltip color="#FFFFFF"
                                     :overlayStyle="{padding:'8px',border:'1px #D9D9D9',}"
                                     v-else-if="design_setting.hover_show_tooltip">
                                <template #title>
                                    <div class="pv-swatch_circle_in_square">
                                        <div v-if="design_setting.hover_show_variant_description" style="color: #333"
                                             :style="{ width: `${generateToolTipHeight}px`}"
                                             class="pv-flex-row-center">
                                            {{ color.label }}
                                        </div>
                                        <div style="overflow: hidden"
                                             :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`,backgroundColor: `${design_setting.background_swatch_color}`}">
                                            <img :src="color.url"
                                                 alt="" style="width: 100%; z-index: 999;position: absolute"
                                                 :style="imgPosition">
                                        </div>
                                    </div>
                                </template>
                                <div class="pv-design-setting-swatch-in-pill-item"
                                     :style="[selectColorIndex === index ? divStyleSelected : divStyleUnselected,getHoverStyle(index)]">
                                    <div class="pv-design-setting-swatch-in-pill-img-block" style="gap: 5px">
                                        <div style="position: relative; align-items: center; overflow: hidden"
                                             :style="{...(selectColorIndex === index ? imgStyleSelected : imgStyleUnselected),backgroundColor:`${design_setting.background_swatch_color}`, height: `${design_setting.img_height}px`, width: `${design_setting.img_width}px`}">
                                            <img :src="color.url" alt=""
                                                 :style="getImageStyle(index)"
                                                 style="padding: 0 !important; position: absolute; height: 200%; width: 200%; transform: translate(-50%, -50%); top: 50%; left: 50%">
                                        </div>
                                        <div class="pv-img-name"
                                             style="max-width: 90px; display: -webkit-box !important; width: max-content !important">
                                            {{ color.label }}
                                        </div>
                                    </div>
                                </div>
                            </Tooltip>
                            <div v-else class="pv-design-setting-swatch-in-pill-item"
                                 :style="[selectColorIndex === index ? divStyleSelected : divStyleUnselected,getHoverStyle(index)]">
                                <div class="pv-design-setting-swatch-in-pill-img-block" style="gap: 5px">
                                    <div style="position: relative; align-items: center; overflow: hidden"
                                         :style="{...(selectColorIndex === index ? imgStyleSelected : imgStyleUnselected),backgroundColor:`${design_setting.background_swatch_color}`, height: `${design_setting.img_height}px`, width: `${design_setting.img_width}px`}">
                                        <img :src="color.url" alt=""
                                             :style="getImageStyle(index)"
                                             style="padding: 0 !important; position: absolute; height: 200%; width: 200%; transform: translate(-50%, -50%); top: 50%; left: 50%">
                                    </div>
                                    <div class="pv-img-name"
                                         style="max-width: 90px; display: -webkit-box !important; width: max-content !important">
                                        {{ color.label }}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import {Select, SelectOption, Tooltip} from "ant-design-vue"

export default {
    name: 'PreviewDesignSetting',
    components: {SelectOption, Select, Tooltip},
    data() {
        return {
            price_array: [16, 15, 18, 14, 19, 20],
            select_option: 1,
            selected_option: {
                value: 1,
                label: "Baby Pink Buckled Flatform Sandals",
                url_img: '/nestprdvariant/static/images/design_setting/preview_design_setting/360e319423a9198a82efa471f5487300.png'
            },
            list_color_data: [{
                value: 1,
                label: 'Hot Pink',
                url: '/nestprdvariant/static/images/design_setting/HotPink.png'
            }, {
                value: 2,
                label: 'Purple',
                url: '/nestprdvariant/static/images/design_setting/MediumPurple.png'
            }, {
                value: 3,
                label: 'Olive Drab',
                url: '/nestprdvariant/static/images/design_setting/OliveDrab.png'
            }, {
                value: 4,
                label: 'Salmon',
                url: '/nestprdvariant/static/images/design_setting/LightSalmon.png'
            }, {
                value: 5,
                label: 'Sky Blue',
                url: '/nestprdvariant/static/images/design_setting/SkyBlue.png'
            }, {
                value: 6,
                label: 'Goldenrod ',
                url: '/nestprdvariant/static/images/design_setting/Goldenrod.png'
            }],
            data_select_option: [{
                value: 1,
                price: '$20',
                label: "Baby Pink Buckled Flatform Sandals",
                url_img: '/nestprdvariant/static/images/design_setting/preview_design_setting/360e319423a9198a82efa471f5487300.png'
            }, {
                url_img: '/nestprdvariant/static/images/design_setting/preview_design_setting/b5db6ab0fae1f58595559cc432b10e7f.jpeg',
                price: '$23',
                label: 'Lilac Purple Buckled Flatform Sandals',
                value: 2
            }, {
                value: 3,
                price: '$30',
                label: "Sand Brown Pink Buckled Flatform Sandals",
                url_img: "/nestprdvariant/static/images/design_setting/preview_design_setting/e49abe93ef9e2c16f65cf8969100d9f6.png"
            }, {
                value: 4,
                price: '$18',
                url_img: '/nestprdvariant/static/images/design_setting/preview_design_setting/7c010d272cd9c537ebbddbd637222a62.png',
                label: "Light Green Buckled Flatform Sandals"
            }, {
                value: 5,
                price: '$33',
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
                url: "/nestprdvariant/static/images/design_setting/SwatchCircleInSquare/preview/4849e1de32b87254df2d8bb093004661.png",
                color: 'Hot Pink', value: 1
            }, {
                value: 2, color: "Goldenrod",
                url: '/nestprdvariant/static/images/design_setting/SwatchCircleInSquare/preview/f7d37766d79868705218ac4cc8417451.png'

            }, {
                value: 3, color: 'Sky Blue',
                url: "/nestprdvariant/static/images/design_setting/SwatchCircleInSquare/preview/e0b5513878d6681bba549da756013883.png"
            }, {
                url: '/nestprdvariant/static/images/design_setting/SwatchCircleInSquare/preview/06806a1319de29107fa80de4a25aabf3.png',
                value: 4, color: 'Olive Drab'
            }, {
                url: '/nestprdvariant/static/images/design_setting/SwatchCircleInSquare/preview/c1c9acb854db58fe9fc4f107e0aa9734.png',
                value: 5, color: 'Medium Purple'
            }, {
                url: '/nestprdvariant/static/images/design_setting/SwatchCircleInSquare/preview/a2171f7bb1f88673536c27ae92a23803.png',
                value: 6, color: 'Salmon'
            }],
            selectSwatchCircleInSquareIndex: 0,
            selectedSwatchCircleInSquare: {
                url: "/nestprdvariant/static/images/design_setting/SwatchCircleInSquare/preview/4849e1de32b87254df2d8bb093004661.png",
                color: 'Hot Pink', value: 1
            },
            selectColorIndex: 0,
            selectedColor: {
                value: 1,
                label: 'Hot Pink',
                url: '/nestprdvariant/static/images/design_setting/HotPink.png'
            },
            hovered_item: null,
        }
    },
    props: {
        designItemName: String,
        design_setting: Object,
        scrollPosition: Number
    },
    methods: {
        generateNumber(index) {
            return this.price_array[index];
        },
        getImageStyle(index) {
            const zoomSize = `scale(${this.design_setting.hover_zoom_size})`;
            let style = this.imgPosition
            style = {
                ...style,
                backgroundColor: `${this.design_setting.background_swatch_color}`,
                transition: 'transform .25s'
            }
            if (this.design_setting.hover_zoom_variant_image) {
                if (this.hovered_item === index) {
                    if (this.design_setting.img_position === 'center' && this.design_setting.img_fit === 'cover') {
                        style.transform = `translate(-50%, -50%) ${zoomSize} !important`;
                    } else {
                        style = {
                            ...style,
                            transform: `scale(${this.design_setting.hover_zoom_size})`,
                        }
                    }

                }
            }
            return style
        },
        getHoverStyle(index) {
            if (this.design_setting.hover_show_shadow === true) {
                if (this.hovered_item === index) {
                    return {
                        boxShadow: `0px 0px ${this.design_setting.hover_shadow_blur}px ${this.design_setting.hover_shadow_thickness}px ${this.design_setting.hover_shadow}`
                    };
                }
            }
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
        generateToolTipHeight() {
            return this.design_setting.img_height * (parseInt(this.design_setting.hover_scaling_size) / 100)
        },
        generateToolTipWidth() {
            return this.design_setting.img_width * (parseInt(this.design_setting.hover_scaling_size) / 100)
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
                        top: '0 !important',
                        left: '0 !important',
                        right: '0 !important',
                    };
                    break;
                case "bottom":
                    imageStyle = {
                        objectFit: this.design_setting.img_position,
                        left: '0 !important',
                        right: '0 !important',
                        bottom: 0
                    };
                    break;
            }
            imageStyle.objectFit = this.design_setting.img_fit === "cover" ? 'cover' : 'contain';
            imageStyle.width = '100%';
            imageStyle.height = this.design_setting.img_fit === "cover" ? 'unset !important' : '100% !important';
            imageStyle.backgroundColor = this.design_setting.background_swatch_color
            return imageStyle;
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