<template>
    <div v-if="pv_data && Object.entries(pv_data.list_product).length > 1" style="width: 100%;">
        <div :style="{fontSize: `${design_setting.label_size}px`}" style="display: flex" class="pv-title-heading">
            <div style="white-space: nowrap">{{ name }}</div>

        </div>
        <div v-if="list_product.length > 0 && this.pv_data['option_img'] !== 'variant_image'">
            <div class="pv-flex-row" :style="[getCollectionPosition]"
                 v-if="design_setting.display_style === 'swatch_circle_in_square'">
                <RadioGroup v-model:value="select_product" style="display: flex; flex-wrap: wrap;position: relative"
                            :style="[ { gap: `${design_setting.swatch_spacing}px` }, getCollectionPosition ]">
                    <Tooltip color="#FFFFFF"
                             v-for="(item,index) in getVariantPreviewArray(list_product)">
                        <template #title
                                  v-if="design_setting.hover_show_variant_description || design_setting.hover_show_tooltip">
                            <span
                                v-if="design_setting.hover_show_variant_description && !design_setting.hover_show_tooltip">
                                {{ item.name }}
                            </span>
                            <div v-else-if="design_setting.hover_show_tooltip">
                                <div v-if="design_setting.hover_show_variant_description" style="color: #333"
                                     :style="{ width: `${generateToolTipHeight}px`}"
                                     class="pv-flex-row-center">
                                    {{ item.variant_option_value }}
                                </div>
                                <div
                                    :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`,...innerBorderTipTool(item.variant_option_value)}">
                                    <!--                                    <img :src="item.url"-->
                                    <!--                                         :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`}"-->
                                    <!--                                         style="object-fit: cover">-->
                                    <div v-if="item.option_swatch === 'color'"
                                         style="height: 100%; width: 100%; position: relative">
                                        <div v-if="item.color_code" :style="{background: `${item.color_code}`}"
                                             style="height: 100%; width: 100%; display: flex !important">
                                        </div>

                                    </div>
                                    <div v-if="item.option_swatch === 'upload'" style="height: 100%; width: 100%">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative; background: white">
                                            <img :src="`https://app.nestscale.com${item.upload_img_url}`" alt=""

                                                 @load="trackImage"
                                                 :style="{ ...imageSettings, backgroundColor: design_setting.background_swatch_color }"
                                                 style="position: absolute"
                                                 class="pv-image-custom">
                                        </div>
                                    </div>
                                    <div v-if="item.option_swatch === 'add_url'" style="height: 100%; width: 100%">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative; background: white">
                                            <img :src="item.swatch_img_url" @load="trackImage"
                                                 :style="{ ...imageSettings, backgroundColor: design_setting.background_swatch_color }"
                                                 alt=""
                                                 style="position: absolute" class="pv-image-custom">
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </template>

                        <Radio :value="item.variant_option_value" class="pv-div" style="padding: 0"
                               @touchstart="touchStartEvent(item.variant_option_value,index)"
                               @mouseenter="handleMouseEnter($event, item.variant_option_value)"
                               @mouseleave="hovered_item = null"
                               @click="productGroupClickEvent(item.variant_option_value,index)">
                            <div class="pv-outer-border "
                                 :style="{...(outerBorder(item.variant_option_value))}">
                                <div class="pv-inner-border" :style="innerBorder(item.variant_option_value)"
                                     style="overflow: hidden">
                                    <div v-if="item.option_swatch === 'color'"
                                         style="height: 100%; width: 100%">
                                        <div v-if="item.color_code"
                                             :style="{background: `${item.color_code}`}"
                                             style="height: 100%; width: 100%; display: flex !important">
                                        </div>

                                    </div>
                                    <div v-if="item.option_swatch === 'upload'" style="height: 100%; width: 100%">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative; background: white">
                                            <img :src="`https://app.nestscale.com${item.upload_img_url}`" alt=""
                                                 @load="trackImage" :style="[getImageStyle(index)]"
                                                 style="position: absolute">
                                        </div>
                                    </div>
                                    <div v-if="item.option_swatch === 'add_url'" style="height: 100%; width: 100%">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative; background: white">
                                            <img :src="item.swatch_img_url" @load="trackImage" alt=""
                                                 :style="[getImageStyle(index)]"
                                                 style="position: absolute">
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </Radio>
                    </Tooltip>
                    <div v-if="num_of_extra_item !== 0">
                        <div @click="clickExtraItem"
                             @mouseenter="handleMouseEnter($event, list_product[list_product.length - num_of_extra_item])"
                             @mouseleave="hovered_item = null"
                             style="justify-content: center; align-items: center; display: flex; background:white"
                             :style="{...(outerBorder(list_product[list_product.length - num_of_extra_item]))}">
                            <div style="overflow: hidden; position: relative"
                                 :style="combinedStyles">
                                <div class="pv-plus-variant-hidden"
                                     :style="{color:design_setting.image_overlay ? '#FFFFFF' : ''}">
                                    +{{ num_of_extra_item }}
                                </div>
                            </div>
                        </div>
                    </div>
                </RadioGroup>
            </div>
            <div v-else-if="design_setting.display_style === 'swatch_in_box'">
                <RadioGroup v-model:value="select_product" style="display: flex; flex-wrap: wrap;position: relative"
                            :style="{gap: `${design_setting.swatch_spacing}px`}">

                    <Tooltip color="#FFFFFF"
                             v-for="(item,index) in getVariantPreviewArray(list_product)">
                        <template #title
                                  v-if="design_setting.hover_show_variant_description || design_setting.hover_show_tooltip">
                            <span
                                v-if="design_setting.hover_show_variant_description && !design_setting.hover_show_tooltip">
                                {{ item.name }}
                            </span>
                            <div v-else-if="design_setting.hover_show_tooltip">
                                <div v-if="design_setting.hover_show_variant_description" style="color: #333"
                                     :style="{ width: `${generateToolTipHeight}px`}"
                                     class="pv-flex-row-center">
                                    {{ item.variant_option_value }}
                                </div>
                                <div
                                    :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`,...innerBorderTipTool(item.variant_option_value)}">
                                    <div v-if="item.option_swatch === 'color'"
                                         style="height: 100%; width: 100%; display: flex; flex-direction: column; position: relative">
                                        <div v-if="item.color_code" :style="{background: `${item.color_code}`}"
                                             style="height: 100%; width: 100%; display: flex !important">
                                        </div>
                                    </div>
                                    <div v-if="item.option_swatch === 'upload'"
                                         style="height: 100%; width: 100%; display: flex; flex-direction: column">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative">
                                            <img :src="`https://app.nestscale.com${item.upload_img_url}`" alt=""
                                                 class="pv-image-custom"
                                                 style="position: absolute"
                                                 :style="{ ...imageSettings, backgroundColor: design_setting.background_swatch_color }">

                                        </div>
                                    </div>
                                    <div v-if="item.option_swatch === 'add_url'"
                                         style="height: 100%; width: 100%; display: flex; flex-direction: column">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative">
                                            <img :src="item.swatch_img_url" class="pv-image-custom"
                                                 style="position: absolute"
                                                 alt=""
                                                 :style="{ ...imageSettings, backgroundColor: design_setting.background_swatch_color }">

                                        </div>
                                    </div>
                                </div>
                            </div>
                        </template>


                        <Radio :value="item.variant_option_value" style="padding: 0"
                               @touchstart="touchStartEvent(item.variant_option_value,index)"
                               @mouseenter="handleMouseEnter($event, item.variant_option_value)"
                               @mouseleave="hovered_item = null"
                               @click="productGroupClickEvent(item.variant_option_value,index)" class="pv-div">
                            <div
                                :style="{...(outerBorder(item.variant_option_value)), paddingTop: design_setting.border_spacing + 'px'}"
                                style="flex-direction: column; justify-content: unset; text-align: center"
                                class="pv-outer-border">
                                <div class="pv-inner-border" :style="innerBorder(item.variant_option_value)"
                                     style="overflow: hidden">
                                    <div v-if="item.option_swatch === 'color'"
                                         style="height: 100%; width: 100%; display: flex; flex-direction: column; position: relative">
                                        <div v-if="item.color_code"
                                             :style="{background: `${item.color_code}`}"
                                             style="height: 100%; width: 100%; display: flex !important">
                                        </div>

                                    </div>
                                    <div v-if="item.option_swatch === 'upload'"
                                         style="height: 100%; width: 100%; display: flex; flex-direction: column">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative">
                                            <img :src="`https://app.nestscale.com${item.upload_img_url}`" alt=""
                                                 @load="trackImage" style="position: absolute"
                                                 :style="[getImageStyle(index)]">

                                        </div>
                                    </div>
                                    <div v-if="item.option_swatch === 'add_url'"
                                         style="height: 100%; width: 100%; display: flex; flex-direction: column">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative">
                                            <img :src="item.swatch_img_url" @load="trackImage"
                                                 style="position: absolute"
                                                 alt="" :style="[getImageStyle(index)]">

                                        </div>
                                    </div>
                                </div>
                            </div>
                        </Radio>
                    </Tooltip>
                    <div v-if="num_of_extra_item !== 0">
                        <div @click="clickExtraItem"
                             @mouseenter="handleMouseEnter($event, list_product[list_product.length - num_of_extra_item])"
                             @mouseleave="hovered_item = null"
                             style="justify-content: center; align-items: center; display: flex; background:white"
                             :style="{...(outerBorder(list_product[list_product.length - num_of_extra_item]))}">
                            <div style="overflow: hidden; position: relative; "
                                 :style="combinedStyles">
                                <div class="pv-plus-variant-hidden"
                                     :style="{color:design_setting.image_overlay ? '#FFFFFF' : ''}">
                                    +{{ num_of_extra_item }}
                                </div>
                            </div>
                        </div>
                    </div>
                </RadioGroup>
            </div>


            <div v-else-if="design_setting.display_style === 'swatch_in_dropdown'"
                 :id="'pv-swatch-in-dropdown-' + name">
                <div @click="openDropdownCustom" class="pv-dropdown"
                     :style="{
                                     border: `${design_setting.dropdown_outer_border_thickness}px solid ${design_setting.dropdown_outer_border}`,
                                     borderRadius: `${design_setting.dropdown_outer_border_radius}px`,
                                     paddingLeft:`${design_setting.border_spacing}px`,
                                     height: `${design_setting.style_height}px`
                                 }">
                    <div style="display: flex; align-items: center; gap: 5px" class="pv-dropdown-selected">
                        <div class="pv-inner-border"
                             :style="{...(innerBorder()), }"
                             style="position: relative; overflow: hidden">
                            <div v-if="list_product[0].option_swatch === 'color'"
                                 :style="{background: list_product[0].color_code}"
                                 style="width: 100%; height: 100%; display: block"/>
                            <img
                                :src="`https://app.nestscale.com${list_product[0].upload_img_url}`"
                                alt=""
                                :style="imageSettings"
                                style="position: absolute"
                                v-if="list_product[0].option_swatch === 'upload'"
                                @load="trackImage">
                            <img :src="list_product[0].swatch_img_url" alt=""
                                 :style="imageSettings"
                                 @load="trackImage"
                                 v-if="list_product[0].option_swatch === 'add_url'"
                                 style="position: absolute">

                        </div>
                        <div>
                            {{ list_product[0].name }}
                        </div>
                    </div>
                    <DownOutlined style="padding-right: 10px"/>
                </div>
                <div :id="'pv-open-dropdown-' + name"
                     :class="openDropdown ? 'openDropdown' : 'hideDropdown'" class="pv-custom-dropdown">
                    <RadioGroup v-model:value="select_product"
                                style="overflow-y: auto; max-height: 250px;position: relative"
                                class="pv-dropdown-selection"
                                :style="{borderRadius: `${this.design_setting.dropdown_outer_border_radius}px`}">
                        <Radio :value="item.variant_option_value" style="width: 100%"
                               :style="{paddingLeft: `${design_setting.border_spacing}px`}"
                               v-for="(item,index) in getVariantPreviewArray(list_product)"
                               @touchstart="touchStartEvent(item.variant_option_value,index)"
                               @click="productGroupClickEvent(item.variant_option_value,index);this.openDropdown = !this.openDropdown"
                               class="pv-div pv-dropdown-item">
                            <div class="pv-outer-border" style="justify-content: unset; gap: 5px; background: unset"
                                 :style="outerBorder(item.variant_option_value)">
                                <div class="pv-inner-border" :style="innerBorder(item.variant_option_value)"
                                     style="overflow: hidden">
                                    <div v-if="item.option_swatch === 'color'"
                                         style="height: 100%; width: 100%; display: flex; flex-direction: column; position: relative">
                                        <div v-if="item.color_code" :style="{background: `${item.color_code}`}"
                                             style="height: 100%; width: 100%; display: flex !important">
                                        </div>

                                    </div>
                                    <div v-if="item.option_swatch === 'upload'"
                                         style="height: 100%; width: 100%; display: flex; flex-direction: column">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative; background: white">
                                            <img :src="`https://app.nestscale.com${item.upload_img_url}`" alt=""
                                                 class="pv-image-custom"
                                                 @load="trackImage" style="position: absolute" :style="imageSettings">

                                        </div>
                                    </div>
                                    <div style="height: 100%; width: 100%; display: flex; flex-direction: column"
                                         v-if="item.option_swatch === 'add_url'">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative; background: white">
                                            <img :src="item.swatch_img_url" class="pv-image-custom" @load="trackImage"
                                                 :style="imageSettings"
                                                 style="position: absolute" alt="">
                                        </div>
                                    </div>
                                </div>
                                <div>{{ item.name }}</div>
                            </div>
                        </Radio>
                    </RadioGroup>
                </div>
            </div>


            <div class="pv-flex-row" :style="[getCollectionPosition]"
                 v-else-if="design_setting.display_style === 'circular_swatch'">
                <RadioGroup v-model:value="select_product" style="display: flex; flex-wrap: wrap;position: relative"
                            :style="[ { gap: `${design_setting.swatch_spacing}px` }, getCollectionPosition ]">
                    <Tooltip color="#FFFFFF"
                             v-for="(item,index) in getVariantPreviewArray(list_product)">
                        <template #title
                                  v-if="design_setting.hover_show_variant_description || design_setting.hover_show_tooltip">
                            <span
                                v-if="design_setting.hover_show_variant_description && !design_setting.hover_show_tooltip">
                                {{ item.name }}
                            </span>
                            <div v-else-if="design_setting.hover_show_tooltip">
                                <div v-if="design_setting.hover_show_variant_description" style="color: #333"
                                     :style="{ width: `${generateToolTipHeight}px`}"
                                     class="pv-flex-row-center">
                                    {{ item.variant_option_value }}
                                </div>
                                <div
                                    :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`,...innerBorderTipTool(item.variant_option_value)}">

                                    <div style="height: 100%; width: 100%; position: relative"
                                         v-if="item.option_swatch === 'color'">
                                        <div v-if="item.color_code" :style="{background: `${item.color_code}`}"
                                             style="height: 100%; width: 100%; display: flex !important">
                                        </div>

                                    </div>
                                    <div v-if="item.option_swatch === 'upload'" style="height: 100%; width: 100%">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative">
                                            <img :src="`https://app.nestscale.com${item.upload_img_url}`" alt=""
                                                 class="pv-image-custom"
                                                 @load="trackImage"
                                                 style="position: absolute"
                                                 :style="{ ...imageSettings, backgroundColor: design_setting.background_swatch_color }">

                                        </div>
                                    </div>
                                    <div v-if="item.option_swatch === 'add_url'" style="height: 100%; width: 100%">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative">
                                            <img :src="item.swatch_img_url"
                                                 :style="{ ...imageSettings, backgroundColor: design_setting.background_swatch_color }"
                                                 @load="trackImage"
                                                 class="pv-image-custom"
                                                 alt="" style="position: absolute">

                                        </div>
                                    </div>
                                </div>
                            </div>
                        </template>

                        <Radio :value="item.variant_option_value" style="padding: 0"
                               @mouseenter="handleMouseEnter($event, item.variant_option_value)"
                               @mouseleave="hovered_item = null"
                               @touchstart="touchStartEvent(item.variant_option_value,index)"
                               @click="productGroupClickEvent(item.variant_option_value,index)" class="pv-div">
                            <div :style="outerBorder(item.variant_option_value)" class="pv-outer-border">
                                <div class="pv-inner-border" :style="innerBorder(item.variant_option_value)"
                                     style="overflow: hidden">
                                    <div style="height: 100%; width: 100%; position: relative"
                                         v-if="item.option_swatch === 'color'">
                                        <div v-if="item.color_code"
                                             :style="{background: `${item.color_code}`}"
                                             style="height: 100%; width: 100%; display: flex !important">
                                        </div>

                                    </div>
                                    <div v-if="item.option_swatch === 'upload'" style="height: 100%; width: 100%">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative">
                                            <img :src="`https://app.nestscale.com${item.upload_img_url}`" alt=""

                                                 @load="trackImage" style="position: absolute"
                                                 :style="[getImageStyle(index)]">

                                        </div>
                                    </div>
                                    <div v-if="item.option_swatch === 'add_url'" style="height: 100%; width: 100%">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative">
                                            <img :src="item.swatch_img_url" @load="trackImage"
                                                 :style="[getImageStyle(index)]"
                                                 alt="" style="position: absolute">

                                        </div>
                                    </div>
                                </div>
                            </div>
                        </Radio>
                    </Tooltip>
                    <div v-if="num_of_extra_item !== 0">
                        <div @click="clickExtraItem"
                             @mouseenter="handleMouseEnter($event, list_product[list_product.length - num_of_extra_item])"
                             @mouseleave="hovered_item = null"
                             style="justify-content: center; align-items: center; display: flex; background:white"
                             :style="{...(outerBorder(list_product[list_product.length - num_of_extra_item]))}">
                            <div style="overflow: hidden; position: relative;"
                                 :style="combinedStyles">
                                <div class="pv-plus-variant-hidden"
                                     :style="{color:design_setting.image_overlay ? '#FFFFFF' : ''}">
                                    +{{ num_of_extra_item }}
                                </div>
                            </div>
                        </div>
                    </div>
                </RadioGroup>
            </div>
            <div class="pv-flex-row" :style="[getCollectionPosition]"
                 v-else-if="design_setting.display_style === 'square_swatch'">
                <RadioGroup v-model:value="select_product" style="display: flex; flex-wrap: wrap;position: relative"
                            :style="[ { gap: `${design_setting.swatch_spacing}px` }, getCollectionPosition ]">

                    <Tooltip color="#FFFFFF"
                             v-for="(item,index) in getVariantPreviewArray(list_product)">

                        <template #title
                                  v-if="design_setting.hover_show_variant_description || design_setting.hover_show_tooltip">
                                        <span
                                            v-if="design_setting.hover_show_variant_description && !design_setting.hover_show_tooltip">
                                            {{ item.name }}
                                        </span>
                            <div v-else-if="design_setting.hover_show_tooltip">
                                <div v-if="design_setting.hover_show_variant_description" style="color: #333"
                                     :style="{ width: `${generateToolTipHeight}px`}"
                                     class="pv-flex-row-center">
                                    {{ item.variant_option_value }}
                                </div>
                                <div
                                    :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`,...innerBorderTipTool(item.variant_option_value)}">
                                    <div v-if="item.option_swatch === 'color'"
                                         style="height: 100%; width: 100%; position: relative">
                                        <div v-if="item.color_code" :style="{background: `${item.color_code}`}"
                                             style="height: 100%; width: 100%; display: flex !important">
                                        </div>

                                    </div>
                                    <div v-if="item.option_swatch === 'upload'" style="height: 100%; width: 100%">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative">
                                            <img :src="`https://app.nestscale.com${item.upload_img_url}`" alt=""
                                                 class="pv-image-custom"
                                                 @load="trackImage"
                                                 style="position: absolute"
                                                 :style="{ ...imageSettings, backgroundColor: design_setting.background_swatch_color }">

                                        </div>
                                    </div>
                                    <div v-if="item.option_swatch === 'add_url'" style="height: 100%; width: 100%">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative">
                                            <img :src="item.swatch_img_url"
                                                 :style="{ ...imageSettings, backgroundColor: design_setting.background_swatch_color }"
                                                 @load="trackImage" class="pv-image-custom"
                                                 style="position: absolute" alt="">

                                        </div>
                                    </div>
                                </div>
                            </div>
                        </template>

                        <Radio :value="item.variant_option_value" class="pv-div"
                               @touchstart="touchStartEvent(item.variant_option_value,index)"
                               @mouseenter="handleMouseEnter($event, item.variant_option_value)"
                               @mouseleave="hovered_item = null"
                               style="padding: 0"
                               @click="productGroupClickEvent(item.variant_option_value,index)">
                            <div
                                :style="{...(outerBorder(item.variant_option_value)), padding: `${design_setting.border_spacing}px`}"
                                class="pv-outer-border">
                                <div class="pv-inner-border" :style="innerBorder(item.variant_option_value)"
                                     style="overflow: hidden">
                                    <div v-if="item.option_swatch === 'color'"
                                         style="height: 100%; width: 100%; position: relative">
                                        <div v-if="item.color_code"
                                             :style="{background: `${item.color_code}`}"
                                             style="height: 100%; width: 100%; display: flex !important">
                                        </div>

                                    </div>
                                    <div v-if="item.option_swatch === 'upload'" style="height: 100%; width: 100%">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative">
                                            <img :src="`https://app.nestscale.com${item.upload_img_url}`" alt=""

                                                 @load="trackImage" style="position: absolute"
                                                 :style="[getImageStyle(index)]">

                                        </div>
                                    </div>
                                    <div v-if="item.option_swatch === 'add_url'" style="height: 100%; width: 100%">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative">
                                            <img :src="item.swatch_img_url" @load="trackImage"

                                                 :style="[getImageStyle(index)]"
                                                 style="position: absolute" alt="">

                                        </div>
                                    </div>
                                </div>
                            </div>
                        </Radio>
                    </Tooltip>
                    <div v-if="num_of_extra_item !== 0">
                        <div @click="clickExtraItem"
                             @mouseenter="handleMouseEnter($event, list_product[list_product.length - num_of_extra_item])"
                             @mouseleave="hovered_item = null"
                             style="justify-content: center; align-items: center; display: flex; background:white"
                             :style="{...(outerBorder(list_product[list_product.length - num_of_extra_item]))}">
                            <div style="overflow: hidden; position: relative;"
                                 :style="combinedStyles">
                                <div class="pv-plus-variant-hidden"
                                     :style="{color:design_setting.image_overlay ? '#FFFFFF' : ''}">
                                    +{{ num_of_extra_item }}
                                </div>
                            </div>
                        </div>
                    </div>
                </RadioGroup>
            </div>
            <div v-else-if="design_setting.display_style === 'swatch_in_pill'">
                <RadioGroup v-model:value="select_product" style="display: flex; flex-wrap: wrap;position: relative"
                            :style="{gap: `${design_setting.swatch_spacing}px`}">

                    <Tooltip color="#FFFFFF"
                             v-for="(item,index) in getVariantPreviewArray(list_product)">
                        <template #title
                                  v-if="design_setting.hover_show_variant_description || design_setting.hover_show_tooltip">
                                        <span
                                            v-if="design_setting.hover_show_variant_description && !design_setting.hover_show_tooltip">
                                            {{ item.name }}
                                        </span>
                            <div v-else-if="design_setting.hover_show_tooltip">
                                <div v-if="design_setting.hover_show_variant_description" style="color: #333"
                                     :style="{ width: `${generateToolTipHeight}px`}"
                                     class="pv-flex-row-center">
                                    {{ item.variant_option_value }}
                                </div>
                                <div
                                    :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`,...innerBorderTipTool(item.variant_option_value)}">
                                    <div
                                        style="height: 100%; width: 100%; display: flex; flex-direction: column; position: relative"
                                        v-if="item.option_swatch === 'color'">
                                        <div v-if="item.color_code" :style="{background: `${item.color_code}`}"
                                             style="height: 100%; width: 100%; display: flex !important">
                                        </div>
                                    </div>
                                    <div v-if="item.option_swatch === 'upload'"
                                         style="height: 100%; width: 100%; display: flex; flex-direction: column">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative">
                                            <img :src="`https://app.nestscale.com${item.upload_img_url}`" alt=""
                                                 class="pv-image-custom"
                                                 @load="trackImage"
                                                 style="position: absolute"
                                                 :style="{ ...imageSettings, backgroundColor: design_setting.background_swatch_color }">

                                        </div>
                                    </div>
                                    <div v-if="item.option_swatch === 'add_url'"
                                         style="height: 100%; width: 100%; display: flex; flex-direction: column">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative">
                                            <img :src="item.swatch_img_url"
                                                 :style="{ ...imageSettings, backgroundColor: design_setting.background_swatch_color }"
                                                 alt="" @load="trackImage"
                                                 class="pv-image-custom"
                                                 style="position: absolute">

                                        </div>
                                    </div>
                                </div>
                            </div>
                        </template>

                        <Radio :value="item.variant_option_value"
                               style="padding: 0"
                               @touchstart="touchStartEvent(item.variant_option_value,index)"
                               @mouseenter="handleMouseEnter($event, item.variant_option_value)"
                               @mouseleave="hovered_item = null"
                               @click="productGroupClickEvent(item.variant_option_value,index)">
                            <div
                                :style="{...(outerBorder(item.variant_option_value)), padding: `0 ${design_setting.border_spacing}px`}"
                                class="pv-outer-border" style="justify-content: unset; gap: 5px">
                                <div class="pv-inner-border" :style="innerBorder(item.variant_option_value)"
                                     style="overflow: hidden">
                                    <div
                                        style="height: 100%; width: 100%; display: flex; flex-direction: column; position: relative"
                                        v-if="item.option_swatch === 'color'">
                                        <div v-if="item.color_code"
                                             :style="{background: `${item.color_code}`}"
                                             style="height: 100%; width: 100%; display: flex !important">
                                        </div>

                                    </div>
                                    <div v-if="item.option_swatch === 'upload'"
                                         style="height: 100%; width: 100%; display: flex; flex-direction: column">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative">
                                            <img :src="`https://app.nestscale.com${item.upload_img_url}`" alt=""

                                                 @load="trackImage" style="position: absolute"
                                                 :style="[getImageStyle(index)]">

                                        </div>
                                    </div>
                                    <div v-if="item.option_swatch === 'add_url'"
                                         style="height: 100%; width: 100%; display: flex; flex-direction: column">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative">
                                            <img :src="item.swatch_img_url" @load="trackImage"
                                                 :style="[getImageStyle(index)]"
                                                 alt=""
                                                 style="position: absolute">
                                        </div>
                                    </div>
                                </div>
                                <div class="pv-pill">{{ item.name }}</div>
                            </div>
                        </Radio>
                    </Tooltip>
                    <div v-if="num_of_extra_item !== 0">
                        <div @click="clickExtraItem"
                             @mouseenter="handleMouseEnter($event, list_product[list_product.length - num_of_extra_item])"
                             @mouseleave="hovered_item = null"
                             style="justify-content: center; align-items: center; display: flex; background:white"
                             :style="{...(outerBorder(list_product[list_product.length - num_of_extra_item]))}">
                            <div style="overflow: hidden; position: relative;"
                                 :style="combinedStyles">
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
        <div v-else-if="list_product.length > 0">
            <div class="pv-flex-row" :style="[getCollectionPosition]"
                 v-if="design_setting.display_style === 'swatch_circle_in_square'">
                <RadioGroup v-model:value="select_product" style="display: flex; flex-wrap: wrap;position: relative"
                            :style="[ { gap: `${design_setting.swatch_spacing}px` }, getCollectionPosition ]">
                    <Tooltip color="#FFFFFF"
                             v-for="(item,index) in getVariantPreviewArray(list_product)">
                        <template #title
                                  v-if="design_setting.hover_show_variant_description || design_setting.hover_show_tooltip">
                            <span
                                v-if="design_setting.hover_show_variant_description && !design_setting.hover_show_tooltip">
                                {{ item.name }}
                            </span>
                            <div v-else-if="design_setting.hover_show_tooltip" class="pv-swatch_circle_in_square">
                                <div v-if="design_setting.hover_show_variant_description" style="color: #333"
                                     :style="{ width: `${generateToolTipHeight}px`}"
                                     class="pv-flex-row-center">
                                    {{ item.name }}
                                </div>
                                <div
                                    :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`,...innerBorderTipTool(index)}">
                                    <img :src="item.img_src"
                                         alt="" style="width: 100%; z-index: 999" class="" @load="trackImage"
                                         :style="imageSettings">

                                </div>
                            </div>
                        </template>
                        <Radio
                            @touchstart="touchStartEvent(item.id,index)"
                            @mouseenter="handleMouseEnter($event, item.id)"
                            @mouseleave="hovered_item = null"
                            @click="productGroupClickEvent(item.id,index)"
                            style="padding: 0; margin: 0 !important" class="pv-div"
                            :value="item.id">
                            <div :style="{...(outerBorder(item.id))}"
                                 class="pv-outer-border pv-swatch_circle_in_square">
                                <div class="pv-inner-border" :style="innerBorder(item.id)">
                                    <img @load="trackImage" :src="item.img_src"
                                         alt="" style="width: 100%"
                                         class="pv-shopify-image"
                                         :style="[getImageStyle(index)]">
                                </div>
                            </div>
                        </Radio>
                    </Tooltip>
                    <div v-if="num_of_extra_item !== 0">
                        <div @click="clickExtraItem"
                             @mouseenter="handleMouseEnter($event, list_product[list_product.length - num_of_extra_item])"
                             @mouseleave="hovered_item = null"
                             style="justify-content: center; align-items: center; display: flex; background:white"
                             :style="{...(outerBorder(list_product[list_product.length - num_of_extra_item]))}">
                            <div style="overflow: hidden; position: relative;"
                                 :style="combinedStyles">
                                <div class="pv-plus-variant-hidden"
                                     :style="{color:design_setting.image_overlay ? '#FFFFFF' : ''}">
                                    +{{ num_of_extra_item }}
                                </div>
                            </div>
                        </div>
                    </div>
                </RadioGroup>
            </div>


            <div v-else-if="design_setting.display_style === 'swatch_in_box'">
                <RadioGroup v-model:value="select_product" style="display: flex; flex-wrap: wrap;position: relative"
                            :style="{gap: design_setting.swatch_spacing + 'px'}">
                    <Tooltip color="#FFFFFF"
                             v-for="(item,index) in getVariantPreviewArray(list_product)">
                        <template #title
                                  v-if="design_setting.hover_show_variant_description || design_setting.hover_show_tooltip">
                            <span
                                v-if="design_setting.hover_show_variant_description && !design_setting.hover_show_tooltip">
                                {{ item.name }}
                            </span>
                            <div v-else-if="design_setting.hover_show_tooltip" class="pv-swatch_circle_in_square">
                                <div v-if="design_setting.hover_show_variant_description" style="color: #333"
                                     :style="{ width: `${generateToolTipHeight}px`}"
                                     class="pv-flex-row-center">
                                    {{ item.name }}
                                </div>
                                <div
                                    :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`,...innerBorderTipTool(index)}">
                                    <img :src="item.img_src"
                                         alt="" style="width: 100%;position: absolute; z-index: 999"
                                         @load="trackImage"
                                         :style="imageSettings">
                                </div>
                            </div>
                        </template>

                        <Radio @mouseenter="handleMouseEnter($event, item.id)"
                               @mouseleave="hovered_item = null"
                               @touchstart="touchStartEvent(item.id,index)"
                               @click="productGroupClickEvent(item.id,index)"
                               :value="item.id" class="pv-div">
                            <div :style="{...(outerBorder(item.id)), }"
                                 class="pv-outer-border" style="flex-direction: column; justify-content: unset">
                                <div :style="{paddingTop: design_setting.border_spacing + 'px'}"
                                     style="display: flex; flex-direction: column; align-items: center">
                                    <div class="pv-inner-border" style="overflow: hidden; position: relative"
                                         :style="innerBorder(item.id)">
                                        <img @load="trackImage"
                                             :src="item.img_src"
                                             class="pv-shopify-image"
                                             alt="" style="width: 100%;position: absolute"
                                             :style="[getImageStyle(index)]">
                                    </div>
                                    <div style="text-align: center">{{ item.name }}</div>
                                </div>

                            </div>
                        </Radio>
                    </Tooltip>
                    <div v-if="num_of_extra_item !== 0">
                        <div @click="clickExtraItem"
                             @mouseenter="handleMouseEnter($event, list_product[list_product.length - num_of_extra_item])"
                             @mouseleave="hovered_item = null"
                             style="justify-content: center; align-items: center; display: flex; background:white"
                             :style="{...(outerBorder(list_product[list_product.length - num_of_extra_item]))}">
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


            <div v-else-if="design_setting.display_style === 'swatch_in_dropdown'"
                 :id="'pv-swatch-in-dropdown-' + name">
                <div @click="openDropdownCustom" class="pv-dropdown"
                     :style="{
                                     height: `${design_setting.style_height}px`,
                                     paddingLeft:`${design_setting.border_spacing}px`,
                                     border: `${design_setting.dropdown_outer_border_thickness}px solid ${design_setting.dropdown_outer_border}`,
                                     borderRadius: `${design_setting.dropdown_outer_border_radius}px`
                                 }">
                    <div class="pv-dropdown-selected">
                        <div class="pv-inner-border"
                             :style="{...(innerBorder())}"
                             style="position: relative; overflow: hidden; background: white">
                            <img :src="list_product[0].img_src" alt=""
                                 :style="imageSettings" @load="trackImage"
                                 class="pv-shopify-image"
                                 style="position: absolute;z-index: 1 !important;">

                        </div>
                        <div>
                            {{ list_product[0].name }}
                        </div>
                    </div>
                    <DownOutlined style="padding-right: 10px"/>
                </div>
                <div :id="'pv-open-dropdown-' + name"
                     :class="openDropdown ? 'openDropdown' : 'hideDropdown'">
                    <RadioGroup v-model:value="select_product" class="pv-dropdown-selection"
                                style="overflow-y: auto; max-height: 250px;position: relative"
                                :style="{
                                        borderRadius: `${design_setting.dropdown_outer_border_radius}px`,
                                        maxWidth: max_width + 'px',
                                        minWidth: max_width + 'px'}">
                        <Radio class="pv-radio-dropdown pv-div pv-swatch-dropdown-item"
                               :value="item.id" style="padding: 5px; width: 100%"
                               v-for="(item,index) in getVariantPreviewArray(list_product)"
                               @touchstart="touchStartEvent(item.id,index)"
                               @click="productGroupClickEvent(item.id,index);this.openDropdown = !this.openDropdown"
                               :style="{...(outerBorder(item.id))}">
                            <div class="pv-outer-border" :style="{}"
                                 style="justify-content: unset; width: 100%; gap: 5px; background: unset">
                                <div style="display: flex; align-items: center; gap: 5px">
                                    <div class="pv-inner-border"
                                         style="overflow: hidden; position: relative; background: white"
                                         :style="innerBorder(item.id)">
                                        <img @load="trackImage"
                                             :src="item.img_src"
                                             alt="" style="width: 100%;position: absolute"
                                             class="pv-shopify-image"
                                             :style="imageSettings">
                                    </div>
                                    <div>{{ item.name }}</div>
                                </div>
                            </div>
                        </Radio>
                    </RadioGroup>
                </div>
            </div>

            <div class="pv-flex-row" :style="[getCollectionPosition]"
                 v-else-if="design_setting.display_style === 'circular_swatch'">
                <RadioGroup v-model:value="select_product" style="display: flex; flex-wrap: wrap;position: relative"
                            :style="[ { gap: `${design_setting.swatch_spacing}px` }, getCollectionPosition ]">
                    <Tooltip color="#FFFFFF"
                             v-for="(item,index) in getVariantPreviewArray(list_product)">
                        <template #title
                                  v-if="design_setting.hover_show_variant_description || design_setting.hover_show_tooltip">
                            <span
                                v-if="design_setting.hover_show_variant_description && !design_setting.hover_show_tooltip">
                                {{ item.name }}
                            </span>
                            <div v-else-if="design_setting.hover_show_tooltip" class="pv-swatch_circle_in_square">
                                <div v-if="design_setting.hover_show_variant_description" style="color: #333"
                                     :style="{ width: `${generateToolTipHeight}px`}"
                                     class="pv-flex-row-center">
                                    {{ item.name }}
                                </div>
                                <div
                                    :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`,...innerBorderTipTool(item.id)}">
                                    <img :src="item.img_src"
                                         alt="" style="width: 100%; z-index: 999" @load="trackImage"
                                         :style="imageSettings">
                                </div>
                            </div>
                        </template>

                        <Radio @mouseenter="handleMouseEnter($event, item.id)"
                               @mouseleave="hovered_item = null"
                               @touchstart="touchStartEvent(item.id,index)"
                               @click="productGroupClickEvent(item.id,index)" class="pv-div"
                               :value="item.id">
                            <div :style="{...(outerBorder(item.id))}"
                                 class="pv-outer-border pv-swatch_circle_in_square">
                                <div class="pv-inner-border" :style="innerBorder(item.id)"
                                     style="overflow: hidden; position: relative;">
                                    <img @load="trackImage" :src="item.img_src"
                                         alt="" style="width: 100%;position: absolute"
                                         class="pv-shopify-image"
                                         :style="[getImageStyle(index)]">

                                </div>
                            </div>
                        </Radio>
                    </Tooltip>
                    <div v-if="num_of_extra_item !== 0">
                        <div @click="clickExtraItem"
                             @mouseenter="handleMouseEnter($event, list_product[list_product.length - num_of_extra_item])"
                             @mouseleave="hovered_item = null"
                             style="justify-content: center; align-items: center; display: flex; background:white"
                             :style="{...(outerBorder(list_product[list_product.length - num_of_extra_item]))}">
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
            <div class="pv-flex-row" :style="[getCollectionPosition]"
                 v-else-if="design_setting.display_style === 'square_swatch'">
                <RadioGroup v-model:value="select_product" style="display: flex; flex-wrap: wrap;position: relative"
                            :style="[ { gap: `${design_setting.swatch_spacing}px` }, getCollectionPosition ]">

                    <Tooltip color="#FFFFFF"
                             v-for="(item,index) in getVariantPreviewArray(list_product)">
                        <template #title
                                  v-if="design_setting.hover_show_variant_description || design_setting.hover_show_tooltip">
                            <span
                                v-if="design_setting.hover_show_variant_description && !design_setting.hover_show_tooltip">
                                {{ item.name }}
                            </span>
                            <div v-else-if="design_setting.hover_show_tooltip" class="pv-swatch_circle_in_square">
                                <div v-if="design_setting.hover_show_variant_description" style="color: #333"
                                     :style="{ width: `${generateToolTipHeight}px`}"
                                     class="pv-flex-row-center">
                                    {{ item.name }}
                                </div>
                                <div
                                    :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`,...innerBorderTipTool(index)}">
                                    <img :src="item.img_src" @load="trackImage"
                                         :style="imageSettings"
                                         alt="" style="width: 100%; z-index: 999"
                                         class="pv-img ">
                                </div>
                            </div>
                        </template>

                        <Radio @mouseenter="handleMouseEnter($event, item.id)"
                               @mouseleave="hovered_item = null"
                               @touchstart="touchStartEvent(item.id,index)"
                               @click="productGroupClickEvent(item.id,index)" class="pv-div"
                               :value="item.id">
                            <div :style="{...(outerBorder(item.id))}"
                                 class="pv-outer-border pv-swatch_circle_in_square">
                                <div class="pv-inner-border" :style="innerBorder(item.id)">
                                    <img @load="trackImage" :src="item.img_src"
                                         alt="" style="width: 100%"
                                         :style="[getImageStyle(index)]"
                                         class="pv-img pv-shopify-image">

                                </div>
                            </div>
                        </Radio>
                    </Tooltip>
                    <div v-if="num_of_extra_item !== 0">
                        <div @click="clickExtraItem"
                             @mouseenter="handleMouseEnter($event, list_product[list_product.length - num_of_extra_item])"
                             @mouseleave="hovered_item = null"
                             style="justify-content: center; align-items: center; display: flex; background:white"
                             :style="{...(outerBorder(list_product[list_product.length - num_of_extra_item]))}">
                            <div style="overflow: hidden; position: relative;"
                                 :style="combinedStyles">
                                <div class="pv-plus-variant-hidden"
                                     :style="{color:design_setting.image_overlay ? '#FFFFFF' : ''}">
                                    +{{ num_of_extra_item }}
                                </div>
                            </div>
                        </div>
                    </div>
                </RadioGroup>
            </div>
            <div v-else-if="design_setting.display_style === 'swatch_in_pill'">
                <RadioGroup v-model:value="select_product" style="display: flex; flex-wrap: wrap;position: relative"
                            :style="{gap: `${design_setting.swatch_spacing}px`}">

                    <Tooltip color="#FFFFFF"
                             v-for="(item,index) in getVariantPreviewArray(list_product)">
                        <template #title
                                  v-if="design_setting.hover_show_variant_description || design_setting.hover_show_tooltip">
                            <span
                                v-if="design_setting.hover_show_variant_description && !design_setting.hover_show_tooltip">
                                {{ item.name }}
                            </span>
                            <div v-else-if="design_setting.hover_show_tooltip" class="pv-swatch_circle_in_square">
                                <div v-if="design_setting.hover_show_variant_description" style="color: #333"
                                     :style="{ width: `${generateToolTipHeight}px`}"
                                     class="pv-flex-row-center">
                                    {{ item.name }}
                                </div>
                                <div
                                    :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`,...innerBorderTipTool(index)}">
                                    <img :src="item.img_src"
                                         alt="" style="width: 100%; z-index: 999" class="pv-img" @load="trackImage"
                                         :style="imageSettings">
                                </div>
                            </div>
                        </template>

                        <Radio :value="item.id" class="pv-div"
                               @mouseenter="handleMouseEnter($event, item.id)"
                               @mouseleave="hovered_item = null"
                               @touchstart="touchStartEvent(item.id,index)"
                               @click="productGroupClickEvent(item.id,index)"
                               style="padding: 0">
                            <div
                                :style="{...(outerBorder(item.id)), padding: `0 ${design_setting.border_spacing}px`}"
                                class="pv-outer-border" style="justify-content: unset !important; gap: 5px">
                                <div class="pv-inner-border" :style="innerBorder(item.id)"
                                     style="overflow: hidden; position: relative">
                                    <img @load="trackImage" :src="item.img_src"
                                         alt="" style="width: 100%"
                                         :style="[getImageStyle(index)]"
                                         class="pv-img pv-shopify-image">
                                </div>
                                <div class="pv-pill">
                                    {{ item.name }}
                                </div>
                            </div>
                        </Radio>
                    </Tooltip>
                    <div v-if="num_of_extra_item !== 0">
                        <div @click="clickExtraItem"
                             @mouseenter="handleMouseEnter($event, list_product[list_product.length - num_of_extra_item])"
                             @mouseleave="hovered_item = null"
                             style="justify-content: center; align-items: center; display: flex; background:white"
                             :style="{...(outerBorder(list_product[list_product.length - num_of_extra_item]))}">
                            <div style="overflow: hidden; position: relative;"
                                 :style="combinedStyles">
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
</template>
<script>
import {Radio, RadioGroup, Select, SelectOption, Tooltip} from "ant-design-vue"
import {DownOutlined} from "@ant-design/icons-vue"

export default {
    name: "ProductGroupComponent",
    data() {
        return {
            checkCustomDropdown: true,
            select_product: '',
            design_setting: {},
            selectOptionSquareInDropdown: '',
            openDropdown: false,
            selected_dropdown_value: '',
            hovered_item: null,
            list_product: [],
            num_of_extra_item: 0,
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
        page: String,
        pv_data: Object,
        max_width: Number,
        card_product_info: Object,
        list_option_data_img_product_group: Object,
        product_id: Number,
        name: String,
        group_index: Number
    },
    watch: {
        checkCustomDropdown() {
            let pv_custom_dropdowns = document.querySelectorAll('.pv-dropdown-selection')
            if (pv_custom_dropdowns.length > 0) {
                for (let pv_custom_dropdown of pv_custom_dropdowns) {
                    pv_custom_dropdown.style.width = pv_custom_dropdown.parentElement.parentElement.offsetWidth + 'px'
                }
            }
        },
    },
    emits: ['change_product_group_image'],
    computed: {
        combinedStyles() {
            const lastVariant = this.list_product[this.list_product.length - this.num_of_extra_item];
            return {
                ...this.innerBorder(lastVariant),
                background: this.design_setting.image_overlay ? `linear-gradient(0deg, rgba(0, 0, 0, 0.20) 0%, rgba(0, 0, 0, 0.20) 100%), url('${this.backgroundLimitedImage}') lightgray 50% / cover no-repeat` : `linear-gradient(0deg, rgba(255, 255, 255, 0.40) 0%, rgba(255, 255, 255, 0.40) 100%), url('${this.backgroundLimitedImage}') lightgray 50% / cover no-repeat`,
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
        generateToolTipHeight() {
            return this.design_setting.img_height * (parseInt(this.design_setting.hover_scaling_size) / 100)
        },
        generateToolTipWidth() {
            return this.design_setting.img_width * (parseInt(this.design_setting.hover_scaling_size) / 100)
        },
    },
    methods: {
        getVariantPreviewArray(variant_array) {
            if (this.page === 'collection') {
                if (this.design_setting.maximum_number_of_variations !== undefined) {
                    if (variant_array.length > this.design_setting.maximum_number_of_variations) {
                        this.num_of_extra_item = variant_array.length - this.design_setting.maximum_number_of_variations
                        let array = JSON.parse(JSON.stringify(variant_array))
                        array.splice(-this.num_of_extra_item)
                        if (array.length > 0) {
                            return array
                        }
                    }
                    this.num_of_extra_item = 0
                    return variant_array
                }
            }
            return variant_array
        },
        touchStartEvent(variant, index) {
            if (this.isMobileDevice) {
                if (this.page === 'product') {
                    this.select_product = variant
                    let a = document.createElement('a');
                    a.href = this.list_product[index].product_url;
                    document.body.appendChild(a);
                    a.click();
                } else {
                    this.$emit('change_product_group_image', this.group_index, variant)
                }
            }
        },
        handleMouseEnter(event, product_id) {
            this.hovered_item = {
                value: product_id,
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
                        transform: 'translate(-50%, -50%) '
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
        getImageStyle(item) {
            let style = {...this.imageSettings()}
            if (this.hovered_item !== null) {
                if (this.design_setting.hover_zoom_variant_image) {
                    if (this.hovered_item.value === item) {
                        style = {
                            ...style,
                            transition: 'transform .25s !important'
                        }
                        if (this.hovered_item.event.target.querySelectorAll('img')[0].width >= this.hovered_item.event.target.querySelectorAll('img')[0].height) {
                            style.transform = `translate(-50%, -50%) scale(${this.design_setting.hover_zoom_size})  !important`
                        } else {
                            style.transform = this.design_setting.img_position === 'center' ? `translate(-50%, -50%) scale(${this.design_setting.hover_zoom_size})  !important` : `scale(${this.design_setting.hover_zoom_size}) !important`

                        }
                    }
                }
            }
            return style;
        },

        openDropdownCustom() {
            this.openDropdown = !this.openDropdown
            if (this.checkCustomDropdown) {
                this.checkCustomDropdown = false
            }
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

        outerBorder(variant) {
            if (this.design_setting.display_style !== "swatch_in_dropdown") {
                // let borderRadius = `${this.design_setting.unselected_outer_border_radius}px`
                // let border = `${this.design_setting.unselected_outer_border} ${this.design_setting.unselected_outer_border_thickness}px solid`
                // if (this.select_product == variant) {
                //     borderRadius = `${this.design_setting.selected_outer_border_radius}px`
                //     border = `${this.design_setting.selected_outer_border} ${this.design_setting.selected_outer_border_thickness}px solid`
                // }
                // if (this.design_setting.display_style === 'circular_swatch') {
                //     borderRadius = '50%'
                // }
                // return {
                //     border: border,
                //     borderRadius: borderRadius,
                //     height: this.design_setting.style_height + 'px',
                //     width: this.design_setting.style_width + 'px'
                // }

                const isSelected = this.select_product === variant
                let isHovered = false
                if (this.hovered_item !== null) {
                    if (this.list_product.length > 0) {
                        isHovered = this.design_setting.hover_show_shadow && this.hovered_item.value === variant;
                    } else {
                        isHovered = this.design_setting.hover_show_shadow && this.hovered_item.value === variant;
                    }
                }
                let borderStyle = isSelected ? this.design_setting.selected_outer_border : this.design_setting.unselected_outer_border;
                let borderWidth = isSelected ? this.design_setting.selected_outer_border_thickness : this.design_setting.unselected_outer_border_thickness;
                let borderRadius;
                if (this.design_setting.display_style === 'circular_swatch') {
                    borderRadius = '50%';
                } else {
                    borderRadius = isSelected ? `${this.design_setting.selected_outer_border_radius}px` : `${this.design_setting.unselected_outer_border_radius}px`;
                }
                let styleObject = {
                    border: `${borderStyle} ${borderWidth}px solid`,
                    borderRadius: borderRadius,
                    minHeight: `${this.design_setting.style_height}px`,
                    width: `${this.design_setting.style_width}px`
                };
                if (isHovered) {
                    styleObject.boxShadow = `0px 0px ${this.design_setting.hover_shadow_blur}px ${this.design_setting.hover_shadow_thickness}px ${this.design_setting.hover_shadow}`;
                }
                return styleObject;
            } else {
                if (this.select_product === variant) {
                    return {
                        background: '#e6f7ff',
                        height: `${this.design_setting.img_height + 10}px`
                    }
                }
                return {height: `${this.design_setting.img_height + 10}px`}
            }
        },
        innerBorderTipTool(variant) {

            let borderRadius = this.design_setting.unselected_inner_border_radius + 'px'
            let border = `${this.design_setting.unselected_inner_border} ${this.design_setting.unselected_inner_border_thickness}px solid`
            // if (this.select_product === variant) {
            //     borderRadius = this.design_setting.selected_inner_border_radius + 'px'
            //     border = `${this.design_setting.selected_inner_border} ${this.design_setting.selected_inner_border_thickness}px solid`
            // }
            if (this.design_setting.display_style === "swatch_circle_in_square" || this.design_setting.display_style === 'circular_swatch') {
                borderRadius = '50%'
            }
            let data = {
                border: border,
                borderRadius: borderRadius,
                overflow: "hidden"
            }

            return data
        },
        innerBorder(variant) {
            if (this.design_setting.display_style === "swatch_in_dropdown") {
                return {
                    height: `${this.design_setting.img_height}px`,
                    width: `${this.design_setting.img_width}px`,
                    border: `${this.design_setting.dropdown_inner_border} solid ${this.design_setting.dropdown_inner_border_thickness}px`,
                    borderRadius: `${this.design_setting.dropdown_inner_border_radius}px`
                }
            }
            let borderRadius = this.design_setting.unselected_inner_border_radius + 'px'
            let border = `${this.design_setting.unselected_inner_border} ${this.design_setting.unselected_inner_border_thickness}px solid`
            if (this.select_product === variant) {
                borderRadius = this.design_setting.selected_inner_border_radius + 'px'
                border = `${this.design_setting.selected_inner_border} ${this.design_setting.selected_inner_border_thickness}px solid`
            }
            if (this.design_setting.display_style === "swatch_circle_in_square" || this.design_setting.display_style === 'circular_swatch') {
                borderRadius = '50%'
            }
            let data = {
                border: border,
                borderRadius: borderRadius,
                height: this.design_setting.img_height + 'px',
                width: this.design_setting.img_width + 'px'
            }
            if (this.design_setting.display_style === 'square_swatch') {
                data.maxHeight = this.design_setting.img_height + 'px'
                data.maxWidth = this.design_setting.img_width + 'px'
            }
            if (this.design_setting.display_style === 'swatch_in_pill') {
                data.minWidth = this.design_setting.img_width + 'px'
            }
            return data
        },
        clickExtraItem() {
            window.open(this.product_url, '_blank')
        },
        productGroupClickEvent(variant, index) {
            if (!this.isMobileDevice) {
                if (this.page === 'product') {
                    this.select_product = variant
                    let a = document.createElement('a');
                    a.href = this.list_product[index].product_url;
                    document.body.appendChild(a);
                    a.click();
                } else {
                    this.$emit('change_product_group_image', this.group_index, variant)
                }
            }
        }
    },
    async mounted() {
        if (this.page === 'product') {
            this.design_setting = this.pv_data.design_setting
        } else {
            this.design_setting = this.pv_data.design_setting_collection_page

            if ('limited_image' in this.design_setting && 'upload_image' in this.design_setting) {
                if (this.design_setting.limited_image === 'custom') {
                    if (this.design_setting.upload_image !== '') {
                        this.backgroundLimitedImage = "https://app.nestscale.com" + this.design_setting.upload_image
                    }
                }
            }
        }

        if (this.pv_data['option_img'] !== 'variant_image') {
            Object.entries(this.list_option_data_img_product_group).forEach(([key, value]) => {
                if (key in this.pv_data['list_product'] && parseInt(key) !== this.product_id) {
                    this.list_product.push(value)
                }
            });
        } else {
            this.list_product = Object.entries(this.pv_data.list_product).filter(([key, value]) => parseInt(key) !== this.product_id).map(([key, value]) => value)
        }
        if ("url" in this.card_product_info) {
            this.product_url = location.origin + this.card_product_info.product.url
        }
        if (this.design_setting.display_style === 'swatch_in_dropdown') {
            this.selected_dropdown_value = this
        }
    }
}
</script>