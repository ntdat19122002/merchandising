<template>
    <div v-if="pv_data">
        <OptionTitle
            :label_size="design_setting.label_size"
            :label_show="design_setting.label_show"
            :label_case="design_setting.label_case"
            :name="option_information.name"
            :label_value="labelValue"
        />
        <div v-if="option_setting_color_custom_image.length > 0">
            <div v-if="design_setting.display_style === 'swatch_circle_in_square'">
                <RadioGroup v-model:value="select_variant_template_id" style="display: flex; flex-wrap: wrap"
                            :style="{gap: `${design_setting.swatch_spacing}px`}">
                    <Tooltip color="#FFFFFF"
                             v-for="(item,index) in option_setting_color_custom_image">
                        <template #title
                                  v-if="design_setting.hover_show_variant_description || design_setting.hover_show_tooltip">
                            <span
                                v-if="design_setting.hover_show_variant_description && !design_setting.hover_show_tooltip">
                                {{ item.variant_option_value }}
                            </span>
                            <div v-else-if="design_setting.hover_show_tooltip">
                                <div v-if="design_setting.hover_show_variant_description" style="color: #333"
                                     :style="{ width: `${generateToolTipHeight}px`}"
                                     class="pv-flex-row-center">
                                    {{ item.variant_option_value }}
                                </div>
                                <div
                                    :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`,...innerBorderTipTool(item.variant_template_id)}">
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

                        <Radio :value="item.variant_template_id" class="pv-div" style="padding: 0"
                               @mouseenter="handleMouseEnter($event, item.variant_template_id)"
                               @touchstart="handleTouchStart"
                               @touchend="handleTouchEnd($event, item.variant_template_id, index)"
                               @mouseleave="hovered_item = null"
                               @click="changeVariant(item.variant_template_id,index)">
                            <div
                                :style="{...(outerBorder(item.variant_template_id)), opacity: list_img[index].available ? 1 : 0.4}"
                                class="pv-outer-border">
                                <div class="pv-inner-border" :style="innerBorder(item.variant_template_id)"
                                     style="overflow: hidden">
                                    <div v-if="item.option_swatch === 'color'"
                                         style="height: 100%; width: 100%; position: relative">
                                        <div v-if="item.color_code"
                                             :style="{background: `${item.color_code}`}"
                                             style="height: 100%; width: 100%; display: flex !important">
                                        </div>


                                        <img v-if="!list_img[index].available" alt="" class="pv-outstock"
                                             src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png">
                                    </div>
                                    <div v-if="item.option_swatch === 'upload'" style="height: 100%; width: 100%">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative; background: white">
                                            <img :src="`https://app.nestscale.com${item.upload_img_url}`" alt=""
                                                 @load="trackImage" :style="[getImageStyle(index)]"
                                                 style="position: absolute">
                                            <img v-if="!list_img[index].available" alt="" class="pv-outstock"
                                                 src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png">
                                        </div>
                                    </div>
                                    <div v-if="item.option_swatch === 'add_url'" style="height: 100%; width: 100%">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative; background: white">
                                            <img :src="item.swatch_img_url" @load="trackImage"
                                                 :style="[getImageStyle(index)]"
                                                 style="position: absolute">
                                            <img v-if="!list_img[index].available" alt="" class="pv-outstock"
                                                 src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png">
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </Radio>
                    </Tooltip>
                </RadioGroup>
            </div>
            <div v-else-if="design_setting.display_style === 'swatch_in_box'">
                <RadioGroup v-model:value="select_variant_template_id" style="display: flex; flex-wrap: wrap"
                            :style="{gap: `${design_setting.swatch_spacing}px`}">

                    <Tooltip color="#FFFFFF"
                             v-for="(item,index) in option_setting_color_custom_image">
                        <template #title
                                  v-if="design_setting.hover_show_variant_description || design_setting.hover_show_tooltip">
                            <span
                                v-if="design_setting.hover_show_variant_description && !design_setting.hover_show_tooltip">
                                {{ item.variant_option_value }}
                            </span>
                            <div v-else-if="design_setting.hover_show_tooltip">
                                <div v-if="design_setting.hover_show_variant_description" style="color: #333"
                                     :style="{ width: `${generateToolTipHeight}px`}"
                                     class="pv-flex-row-center">
                                    {{ item.variant_option_value }}
                                </div>
                                <div
                                    :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`,...innerBorderTipTool(item.variant_template_id)}">
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


                        <Radio :value="item.variant_template_id" style="padding: 0"
                               @touchstart="handleTouchStart"
                               @touchend="handleTouchEnd($event, item.variant_template_id, index)"
                               @mouseenter="handleMouseEnter($event, item.variant_template_id)"
                               @mouseleave="hovered_item = null"
                               @click="changeVariant(item.variant_template_id,index)" class="pv-div">
                            <div
                                :style="{...(outerBorder(item.variant_template_id)), paddingTop: design_setting.border_spacing + 'px', opacity: list_img[index].available ? 1 : 0.4}"
                                style="flex-direction: column; justify-content: unset; text-align: center"
                                class="pv-outer-border">
                                <div class="pv-inner-border" :style="innerBorder(item.variant_template_id)"
                                     style="overflow: hidden">
                                    <div v-if="item.option_swatch === 'color'"
                                         style="height: 100%; width: 100%; display: flex; flex-direction: column; position: relative">
                                        <div v-if="item.color_code"
                                             :style="{background: `${item.color_code}`}"
                                             style="height: 100%; width: 100%; display: flex !important">
                                        </div>
                                        <img v-if="!list_img[index].available" alt="" class="pv-outstock"
                                             src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png">
                                    </div>
                                    <div v-if="item.option_swatch === 'upload'"
                                         style="height: 100%; width: 100%; display: flex; flex-direction: column">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative">
                                            <img :src="`https://app.nestscale.com${item.upload_img_url}`" alt=""
                                                 @load="trackImage" style="position: absolute"
                                                 :style="[getImageStyle(index)]">
                                            <img v-if="!list_img[index].available" alt="" class="pv-outstock"
                                                 src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png">
                                        </div>
                                    </div>
                                    <div v-if="item.option_swatch === 'add_url'"
                                         style="height: 100%; width: 100%; display: flex; flex-direction: column">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative">
                                            <img :src="item.swatch_img_url" @load="trackImage"
                                                 style="position: absolute"
                                                 alt="" :style="[getImageStyle(index)]">
                                            <img v-if="!list_img[index].available" alt="" class="pv-outstock"
                                                 src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png">
                                        </div>
                                    </div>
                                </div>
                                <div>{{ swatch_value }}</div>
                                <div v-if="design_setting.show_price">{{ getPrice(list_img[index].price) }}</div>
                            </div>
                        </Radio>
                    </Tooltip>
                </RadioGroup>
            </div>
            <div v-else-if="design_setting.display_style === 'swatch_in_dropdown'"
                 :id="'pv-swatch-in-dropdown-' + variant_template_ids.index_of_fieldset">
                <div @click="openDropdownCustom" class="pv-dropdown"
                     :style="{
                         border: `${design_setting.dropdown_outer_border_thickness}px solid ${design_setting.dropdown_outer_border}`,
                         borderRadius: `${design_setting.dropdown_outer_border_radius}px`,
                         paddingLeft:`${design_setting.border_spacing}px`,
                         height: `${design_setting.style_height}px`
                     }">
                    <div class="pv-dropdown-selected pv-space-between" style="width: 100%">
                        <div class="pv-dropdown-selected" style="gap: 8px">
                            <div class="pv-inner-border"
                                 :style="{...(innerBorder()), opacity: list_img[index_of_option_variant].available ? 1 : 0.4}"
                                 style="position: relative; overflow: hidden">
                                <div v-if="option_setting_color_custom_image_choosen.option_swatch === 'color'"
                                     :style="{background: option_setting_color_custom_image_choosen.color_code}"
                                     style="width: 100%; height: 100%; display: block"/>
                                <img
                                    :src="`https://app.nestscale.com${option_setting_color_custom_image_choosen.upload_img_url}`"
                                    alt=""
                                    :style="imageSettings" :id="list_img[index_of_option_variant].src"
                                    style="position: absolute"
                                    v-if="option_setting_color_custom_image_choosen.option_swatch === 'upload'"
                                    @load="trackImage">
                                <img :src="option_setting_color_custom_image_choosen.swatch_img_url" alt=""
                                     :style="imageSettings"
                                     :id="list_img[index_of_option_variant].src"
                                     @load="trackImage"
                                     v-if="option_setting_color_custom_image_choosen.option_swatch === 'add_url'"
                                     style="position: absolute">
                                <img v-if="!list_img[index_of_option_variant].available" alt="" class="pv-outstock"
                                     src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png">
                            </div>
                            <div :style="{opacity: list_img[index_of_option_variant].available ? 1 : 0.4}">
                                {{ selectedVariant }}
                            </div>
                        </div>
                        <div class="pv-price-text" v-if="design_setting.show_price">
                            {{ getPrice(list_img[index_of_option_variant].price) }}
                        </div>
                    </div>
                    <DownOutlined style="padding-right: 10px"/>
                </div>
                <div :id="'pv-open-dropdown-' + variant_template_ids.index_of_fieldset"
                     :class="openDropdown ? 'openDropdown' : 'hideDropdown'" class="pv-custom-dropdown">
                    <RadioGroup v-model:value="select_variant_template_id"
                                style="overflow-y: auto; max-height: 250px;z-index: 4" class="pv-dropdown-selection"
                                :style="{borderRadius: `${this.design_setting.dropdown_outer_border_radius}px`}">
                        <Radio :value="item.variant_template_id" style="width: 100%"
                               :style="{paddingLeft: `${design_setting.border_spacing}px`, opacity: list_img[index].available ? 1: 0.4}"
                               v-for="(item,index) in option_setting_color_custom_image"
                               @click="changeVariant(item.variant_template_id,index);this.openDropdown = !this.openDropdown"
                               class="pv-div pv-dropdown-item">
                            <div class="pv-outer-border"
                                 style="justify-content: space-between; gap: 5px; background: unset"
                                 :style="outerBorder(item.variant_template_id)">
                                <div style="display: flex; align-items: center; gap: 8px">
                                    <div class="pv-inner-border" :style="innerBorder(item.variant_template_id)"
                                         style="overflow: hidden">
                                        <div v-if="item.option_swatch === 'color'"
                                             style="height: 100%; width: 100%; display: flex; flex-direction: column; position: relative">
                                            <div v-if="item.color_code" :style="{background: `${item.color_code}`}"
                                                 style="height: 100%; width: 100%; display: flex !important">
                                            </div>
                                            <img
                                                src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png"
                                                v-if="!list_img[index].available" alt="" class="pv-outstock">
                                        </div>
                                        <div v-if="item.option_swatch === 'upload'"
                                             style="height: 100%; width: 100%; display: flex; flex-direction: column">
                                            <div
                                                style="height: 100%; width: 100%; display: flex !important; position: relative; background: white">
                                                <img :src="`https://app.nestscale.com${item.upload_img_url}`" alt=""
                                                     class="pv-image-custom"
                                                     @load="trackImage" style="position: absolute"
                                                     :style="imageSettings">
                                                <img
                                                    src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png"
                                                    v-if="!list_img[index].available" alt="" class="pv-outstock">
                                            </div>
                                        </div>
                                        <div style="height: 100%; width: 100%; display: flex; flex-direction: column"
                                             v-if="item.option_swatch === 'add_url'">
                                            <div
                                                style="height: 100%; width: 100%; display: flex !important; position: relative; background: white">
                                                <img :src="item.swatch_img_url" class="pv-image-custom"
                                                     @load="trackImage"
                                                     :style="imageSettings"
                                                     style="position: absolute" alt="">
                                                <img
                                                    src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png"
                                                    v-if="!list_img[index].available" alt="" class="pv-outstock">
                                            </div>
                                        </div>
                                    </div>
                                    <div>{{ swatch_value }}</div>
                                </div>


                                <div class="pv-price-text" v-if="design_setting.show_price">
                                    {{ getPrice(list_img[index_of_option_variant].price) }}
                                </div>
                            </div>
                        </Radio>
                    </RadioGroup>
                </div>
            </div>
            <div v-else-if="design_setting.display_style === 'circular_swatch'">
                <RadioGroup v-model:value="select_variant_template_id" style="display: flex; flex-wrap: wrap"
                            :style="{gap: `${design_setting.swatch_spacing}px`}">

                    <Tooltip color="#FFFFFF"
                             v-for="(item,index) in option_setting_color_custom_image">
                        <template #title
                                  v-if="design_setting.hover_show_variant_description || design_setting.hover_show_tooltip">
                            <span
                                v-if="design_setting.hover_show_variant_description && !design_setting.hover_show_tooltip">
                                {{ item.variant_option_value }}
                            </span>
                            <div v-else-if="design_setting.hover_show_tooltip">
                                <div v-if="design_setting.hover_show_variant_description" style="color: #333"
                                     :style="{ width: `${generateToolTipHeight}px`}"
                                     class="pv-flex-row-center">
                                    {{ item.variant_option_value }}
                                </div>
                                <div
                                    :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`,...innerBorderTipTool(item.variant_template_id)}">

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

                        <Radio :value="item.variant_template_id" style="padding: 0"
                               :style="{opacity: list_img[index].available ? 1 : 0.4}"
                               @touchstart="handleTouchStart"
                               @touchend="handleTouchEnd($event, item.variant_template_id, index)"
                               @mouseenter="handleMouseEnter($event, item.variant_template_id)"
                               @mouseleave="hovered_item = null"
                               @click="changeVariant(item.variant_template_id,index)" class="pv-div">
                            <div :style="outerBorder(item.variant_template_id)" class="pv-outer-border">
                                <div class="pv-inner-border" :style="innerBorder(item.variant_template_id)"
                                     style="overflow: hidden">
                                    <div style="height: 100%; width: 100%; position: relative"
                                         v-if="item.option_swatch === 'color'">
                                        <div v-if="item.color_code"
                                             :style="{background: `${item.color_code}`}"
                                             style="height: 100%; width: 100%; display: flex !important">
                                        </div>
                                        <img
                                            src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png"
                                            v-if="!list_img[index].available" alt="" class="pv-outstock">
                                    </div>
                                    <div v-if="item.option_swatch === 'upload'" style="height: 100%; width: 100%">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative">
                                            <img :src="`https://app.nestscale.com${item.upload_img_url}`" alt=""

                                                 @load="trackImage" style="position: absolute"
                                                 :style="[getImageStyle(index)]">
                                            <img
                                                src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png"
                                                v-if="!list_img[index].available" alt="" class="pv-outstock">
                                        </div>
                                    </div>
                                    <div v-if="item.option_swatch === 'add_url'" style="height: 100%; width: 100%">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative">
                                            <img :src="item.swatch_img_url" @load="trackImage"
                                                 :style="[getImageStyle(index)]"
                                                 alt="" style="position: absolute">
                                            <img
                                                src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png"
                                                v-if="!list_img[index].available" alt="" class="pv-outstock">
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </Radio>
                    </Tooltip>
                </RadioGroup>
            </div>
            <div v-else-if="design_setting.display_style === 'square_swatch'">
                <RadioGroup v-model:value="select_variant_template_id" style="display: flex; flex-wrap: wrap"
                            :style="{gap: `${design_setting.swatch_spacing}px`}">

                    <Tooltip color="#FFFFFF"
                             v-for="(item,index) in option_setting_color_custom_image">

                        <template #title
                                  v-if="design_setting.hover_show_variant_description || design_setting.hover_show_tooltip">
                            <span
                                v-if="design_setting.hover_show_variant_description && !design_setting.hover_show_tooltip">
                                {{ item.variant_option_value }}
                            </span>
                            <div v-else-if="design_setting.hover_show_tooltip">
                                <div v-if="design_setting.hover_show_variant_description" style="color: #333"
                                     :style="{ width: `${generateToolTipHeight}px`}"
                                     class="pv-flex-row-center">
                                    {{ item.variant_option_value }}
                                </div>
                                <div
                                    :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`,...innerBorderTipTool(item.variant_template_id)}">
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

                        <Radio :value="item.variant_template_id" class="pv-div"
                               @touchstart="handleTouchStart"
                               @touchend="handleTouchEnd($event, item.variant_template_id, index)"
                               @mouseenter="handleMouseEnter($event, item.variant_template_id)"
                               @mouseleave="hovered_item = null"
                               style="padding: 0" :style="{opacity: list_img[index].available ? 1 : 0.4}"
                               @click="changeVariant(item.variant_template_id,index)">
                            <div
                                :style="{...(outerBorder(item.variant_template_id)), padding: `${design_setting.border_spacing}px`}"
                                class="pv-outer-border">
                                <div class="pv-inner-border" :style="innerBorder(item.variant_template_id)"
                                     style="overflow: hidden">
                                    <div v-if="item.option_swatch === 'color'"
                                         style="height: 100%; width: 100%; position: relative">
                                        <div v-if="item.color_code"
                                             :style="{background: `${item.color_code}`}"
                                             style="height: 100%; width: 100%; display: flex !important">
                                        </div>
                                        <img
                                            src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png"
                                            v-if="!list_img[index].available" alt="" class="pv-outstock">
                                    </div>
                                    <div v-if="item.option_swatch === 'upload'" style="height: 100%; width: 100%">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative">
                                            <img :src="`https://app.nestscale.com${item.upload_img_url}`" alt=""

                                                 @load="trackImage" style="position: absolute"
                                                 :style="[getImageStyle(index)]">
                                            <img
                                                src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png"
                                                v-if="!list_img[index].available" alt="" class="pv-outstock">
                                        </div>
                                    </div>
                                    <div v-if="item.option_swatch === 'add_url'" style="height: 100%; width: 100%">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative">
                                            <img :src="item.swatch_img_url" @load="trackImage"

                                                 :style="[getImageStyle(index)]"
                                                 style="position: absolute" alt="">
                                            <img
                                                src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png"
                                                v-if="!list_img[index].available" alt="" class="pv-outstock">
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </Radio>
                    </Tooltip>
                </RadioGroup>
            </div>
            <div v-else-if="design_setting.display_style === 'swatch_in_pill'">
                <RadioGroup v-model:value="select_variant_template_id" style="display: flex; flex-wrap: wrap"
                            :style="{gap: `${design_setting.swatch_spacing}px`}">

                    <Tooltip color="#FFFFFF"
                             v-for="(item,index) in option_setting_color_custom_image">
                        <template #title
                                  v-if="design_setting.hover_show_variant_description || design_setting.hover_show_tooltip">
                            <span
                                v-if="design_setting.hover_show_variant_description && !design_setting.hover_show_tooltip">
                                {{ item.variant_option_value }}
                            </span>
                            <div v-else-if="design_setting.hover_show_tooltip">
                                <div v-if="design_setting.hover_show_variant_description" style="color: #333"
                                     :style="{ width: `${generateToolTipHeight}px`}"
                                     class="pv-flex-row-center">
                                    {{ item.variant_option_value }}
                                </div>
                                <div
                                    :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`,...innerBorderTipTool(item.variant_template_id)}">
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

                        <Radio :value="item.variant_template_id"
                               :style="{opacity: list_img[index].available ? 1 : 0.4}" style="padding: 0"
                               @touchstart="handleTouchStart"
                               @touchend="handleTouchEnd($event, item.variant_template_id, index)"
                               @mouseenter="handleMouseEnter($event, item.variant_template_id)"
                               @mouseleave="hovered_item = null"
                               @click="changeVariant(item.variant_template_id,index)">
                            <div
                                :style="{...(outerBorder(item.variant_template_id)), padding: `0 ${design_setting.border_spacing}px`}"
                                class="pv-outer-border" style="justify-content: unset; gap: 5px">
                                <div class="pv-inner-border" :style="innerBorder(item.variant_template_id)"
                                     style="overflow: hidden">
                                    <div
                                        style="height: 100%; width: 100%; display: flex; flex-direction: column; position: relative"
                                        v-if="item.option_swatch === 'color'">
                                        <div v-if="item.color_code"
                                             :style="{background: `${item.color_code}`}"
                                             style="height: 100%; width: 100%; display: flex !important">
                                        </div>
                                        <img
                                            src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png"
                                            v-if="!list_img[index].available" alt="" class="pv-outstock">
                                    </div>
                                    <div v-if="item.option_swatch === 'upload'"
                                         style="height: 100%; width: 100%; display: flex; flex-direction: column">
                                        <div
                                            style="height: 100%; width: 100%; display: flex !important; position: relative">
                                            <img :src="`https://app.nestscale.com${item.upload_img_url}`" alt=""

                                                 @load="trackImage" style="position: absolute"
                                                 :style="[getImageStyle(index)]">
                                            <img
                                                src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png"
                                                v-if="!list_img[index].available" alt="" class="pv-outstock">
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
                                            <img
                                                src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png"
                                                v-if="!list_img[index].available" alt="" class="pv-outstock">
                                        </div>
                                    </div>
                                </div>
                                <div class="pv-pill">{{ swatch_value }}</div>
                            </div>
                        </Radio>
                    </Tooltip>
                </RadioGroup>
            </div>
        </div>
        <div v-else>
            <div v-if="design_setting.display_style === 'swatch_circle_in_square'">
                <RadioGroup v-model:value="select_variant_template_id" style="display: flex; flex-wrap: wrap"
                            :style="{gap: design_setting.swatch_spacing + 'px'}">
                    <Tooltip color="#FFFFFF"
                             v-for="(variant,index) in variant_template_ids">
                        <template #title
                                  v-if="design_setting.hover_show_variant_description || design_setting.hover_show_tooltip">
                            <span
                                v-if="design_setting.hover_show_variant_description && !design_setting.hover_show_tooltip">
                                {{ swatch_value }}
                            </span>
                            <div v-else-if="design_setting.hover_show_tooltip" class="pv-swatch_circle_in_square">
                                <div v-if="design_setting.hover_show_variant_description" style="color: #333"
                                     :style="{ width: `${generateToolTipHeight}px`}"
                                     class="pv-flex-row-center">
                                    {{ swatch_value }}
                                </div>
                                <div
                                    :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`,...innerBorderTipTool(index)}">
                                    <img :src="list_img[index].src || default_url_img"
                                         alt="" style="width: 100%; z-index: 999" class="" @load="trackImage"
                                         :style="imageSettings">

                                </div>
                            </div>
                        </template>
                        <Radio
                            @mouseenter="handleMouseEnter($event, index)"
                            @touchstart="handleTouchStart"
                            @touchend="handleTouchEnd($event,variant,index)"
                            @mouseleave="hovered_item = null"
                            @click="changeVariant(variant,index)"
                            style="padding: 0; margin: 0 !important" class="pv-div"
                            :value="variant">
                            <div :style="{...(outerBorder(variant)), opacity: list_img[index].available ? 1 : 0.4}"
                                 class="pv-outer-border pv-swatch_circle_in_square">
                                <div class="pv-inner-border" :style="innerBorder(variant)">
                                    <img @load="trackImage" :src="list_img[index].src || default_url_img"
                                         alt="" style="width: 100%"
                                         class="pv-shopify-image"
                                         :style="[getImageStyle(index)]">
                                    <img v-if="!list_img[index].available" alt="" class="pv-outstock"
                                         src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png">
                                </div>
                            </div>
                        </Radio>
                    </Tooltip>
                </RadioGroup>
            </div>
            <div v-else-if="design_setting.display_style === 'swatch_in_box'">
                <RadioGroup v-model:value="select_variant_template_id" style="display: flex; flex-wrap: wrap"
                            :style="{gap: design_setting.swatch_spacing + 'px'}">
                    <Tooltip color="#FFFFFF"
                             v-for="(variant,index) in variant_template_ids">
                        <template #title
                                  v-if="design_setting.hover_show_variant_description || design_setting.hover_show_tooltip">
                            <span
                                v-if="design_setting.hover_show_variant_description && !design_setting.hover_show_tooltip">
                                {{ swatch_value }}
                            </span>
                            <div v-else-if="design_setting.hover_show_tooltip" class="pv-swatch_circle_in_square">
                                <div v-if="design_setting.hover_show_variant_description" style="color: #333"
                                     :style="{ width: `${generateToolTipHeight}px`}"
                                     class="pv-flex-row-center">
                                    {{ swatch_value }}
                                </div>
                                <div
                                    :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`,...innerBorderTipTool(index)}">
                                    <img :src="list_img[index].src || default_url_img"
                                         alt="" style="width: 100%;position: absolute; z-index: 999"
                                         @load="trackImage"
                                         :style="imageSettings">
                                </div>
                            </div>
                        </template>

                        <Radio @mouseenter="handleMouseEnter($event, index)"
                               @touchstart="handleTouchStart"
                               @touchend="handleTouchEnd($event,variant,index)"
                               @mouseleave="hovered_item = null"
                               @click="changeVariant(variant,index)"
                               :value="variant" class="pv-div">
                            <div :style="{...(outerBorder(variant)), opacity: list_img[index].available ? 1 : 0.4}"
                                 class="pv-outer-border" style="flex-direction: column; justify-content: unset">
                                <div :style="{paddingTop: design_setting.border_spacing + 'px'}"
                                     style="display: flex; flex-direction: column; align-items: center">
                                    <div class="pv-inner-border" style="overflow: hidden; position: relative"
                                         :style="innerBorder(variant)">
                                        <img @load="trackImage"
                                             :src="list_img[index].src || default_url_img"
                                             class="pv-shopify-image"
                                             alt="" style="width: 100%;position: absolute"
                                             :style="[getImageStyle(index)]">
                                        <img v-if="!list_img[index].available" alt="" class="pv-outstock"
                                             src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png">
                                    </div>
                                    <div style="text-align: center">{{ variant.value }}</div>
                                </div>
                                <div class="pv-pill">
                                    {{ swatch_value }}
                                </div>
                                <div v-if="design_setting.show_price">{{ getPrice(list_img[index].price) }}</div>
                            </div>
                        </Radio>
                    </Tooltip>
                </RadioGroup>
            </div>
            <div v-else-if="design_setting.display_style === 'swatch_in_dropdown'"
                 :id="'pv-swatch-in-dropdown-' + variant_template_ids.index_of_fieldset">
                <div @click="openDropdown = !openDropdown" class="pv-dropdown"
                     :style="{
                         height: `${design_setting.style_height}px`,
                         paddingLeft:`${design_setting.border_spacing}px`,
                         border: `${design_setting.dropdown_outer_border_thickness}px solid ${design_setting.dropdown_outer_border}`,
                         borderRadius: `${design_setting.dropdown_outer_border_radius}px`
                     }">
                    <div class="pv-dropdown-selected pv-space-between" style="width: 100%">
                        <div class="pv-dropdown-selected" style="gap: 8px">
                            <div class="pv-inner-border"
                                 :style="{...(innerBorder()), opacity: list_img[index_of_option_variant].available ? 1 : 0.4}"
                                 style="position: relative; overflow: hidden; background: white">
                                <img :src="list_img[index_of_option_variant].src || default_url_img" alt=""
                                     :style="imageSettings" @load="trackImage"
                                     class="pv-shopify-image"
                                     style="position: absolute;z-index: 1 !important;">
                                <img
                                    src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png"
                                    alt="" class="pv-outstock" v-if="!list_img[index_of_option_variant].available">
                            </div>
                            <div :style="{opacity: list_img[index_of_option_variant].available ? 1 : 0.4}">
                                {{ selectedVariant }}
                            </div>
                        </div>
                        <div class="pv-price-text" v-if="design_setting.show_price">
                            {{ getPrice(list_img[index_of_option_variant].price) }}
                        </div>
                    </div>
                    <DownOutlined style="padding-right: 10px"/>
                </div>
                <div :id="'pv-open-dropdown-' + variant_template_ids.index_of_fieldset"
                     :class="openDropdown ? 'openDropdown' : 'hideDropdown'">
                    <RadioGroup v-model:value="select_variant_template_id" class="pv-dropdown-selection"
                                style="overflow-y: auto; max-height: 250px; z-index: 4"
                                :style="{
                                    borderRadius: `${design_setting.dropdown_outer_border_radius}px`,
                                    maxWidth: max_width + 'px',
                                    minWidth: max_width + 'px'
                                }">
                        <Radio class="pv-radio-dropdown pv-div pv-swatch-dropdown-item"
                               :value="variant" style="padding: 5px; width: 100%"
                               v-for="(variant,index) in variant_template_ids"
                               @click="changeVariant(variant,index);this.openDropdown = !this.openDropdown"
                               :style="{...(outerBorder(variant))}">
                            <div class="pv-outer-border" :style="{opacity: list_img[index].available ? 1 : 0.4}"
                                 style="justify-content: space-between; width: 100%; gap: 5px; background: unset">
                                <div style="display: flex; align-items: center; gap: 8px">
                                    <div class="pv-inner-border"
                                         style="overflow: hidden; position: relative; background: white"
                                         :style="innerBorder(variant)">
                                        <img @load="trackImage"
                                             :src="list_img[index].src || default_url_img"
                                             alt="" style="width: 100%;position: absolute"
                                             class="pv-shopify-image"
                                             :style="imageSettings">
                                        <img
                                            src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png"
                                            v-if="!list_img[index].available" alt="" class="pv-outstock">
                                    </div>
                                    <div>{{ swatch_value }}</div>
                                </div>
                                <div class="pv-price-text" v-if="design_setting.show_price">
                                    {{ getPrice(list_img[index_of_option_variant].price) }}
                                </div>
                            </div>
                        </Radio>
                    </RadioGroup>
                </div>
            </div>
            <div v-else-if="design_setting.display_style === 'circular_swatch'">
                <RadioGroup v-model:value="select_variant_template_id" style="display: flex; flex-wrap: wrap"
                            :style="{gap: design_setting.swatch_spacing + 'px'}">

                    <Tooltip color="#FFFFFF"
                             v-for="(variant,index) in variant_template_ids">
                        <template #title
                                  v-if="design_setting.hover_show_variant_description || design_setting.hover_show_tooltip">
                            <span
                                v-if="design_setting.hover_show_variant_description && !design_setting.hover_show_tooltip">
                                {{ swatch_value }}
                            </span>
                            <div v-else-if="design_setting.hover_show_tooltip" class="pv-swatch_circle_in_square">
                                <div v-if="design_setting.hover_show_variant_description" style="color: #333"
                                     :style="{ width: `${generateToolTipHeight}px`}"
                                     class="pv-flex-row-center">
                                    {{ swatch_value }}
                                </div>
                                <div
                                    :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`,...innerBorderTipTool(index)}">
                                    <img :src="list_img[index].src || default_url_img"
                                         alt="" style="width: 100%; z-index: 999" @load="trackImage"
                                         :style="imageSettings">
                                </div>
                            </div>
                        </template>


                        <Radio @mouseenter="handleMouseEnter($event, index)"
                               @touchstart="handleTouchStart"
                               @touchend="handleTouchEnd($event,variant,index)"
                               @mouseleave="hovered_item = null"
                               @click="changeVariant(variant,index)" class="pv-div"
                               :value="variant">
                            <div :style="{...(outerBorder(variant)), opacity: list_img[index].available ? 1 : 0.4}"
                                 class="pv-outer-border pv-swatch_circle_in_square">
                                <div class="pv-inner-border" :style="innerBorder(variant)"
                                     style="overflow: hidden; position: relative;">
                                    <img @load="trackImage" :src="list_img[index].src || default_url_img"
                                         alt="" style="width: 100%;position: absolute"
                                         class="pv-shopify-image"
                                         :style="[getImageStyle(index)]">
                                    <img v-if="!list_img[index].available" alt="" class="pv-outstock"
                                         src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png">
                                </div>
                            </div>
                        </Radio>
                    </Tooltip>
                </RadioGroup>
            </div>
            <div v-else-if="design_setting.display_style === 'square_swatch'">
                <RadioGroup v-model:value="select_variant_template_id" style="display: flex; flex-wrap: wrap"
                            :style="{gap: design_setting.swatch_spacing + 'px'}">

                    <Tooltip color="#FFFFFF"
                             v-for="(variant,index) in variant_template_ids">
                        <template #title
                                  v-if="design_setting.hover_show_variant_description || design_setting.hover_show_tooltip">
                            <span
                                v-if="design_setting.hover_show_variant_description && !design_setting.hover_show_tooltip">
                                {{ swatch_value }}
                            </span>
                            <div v-else-if="design_setting.hover_show_tooltip" class="pv-swatch_circle_in_square">
                                <div v-if="design_setting.hover_show_variant_description" style="color: #333"
                                     :style="{ width: `${generateToolTipHeight}px`}"
                                     class="pv-flex-row-center">
                                    {{ swatch_value }}
                                </div>
                                <div
                                    :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`,...innerBorderTipTool(index)}">
                                    <img :src="list_img[index].src || default_url_img" @load="trackImage"
                                         :style="imageSettings"
                                         alt="" style="width: 100%; z-index: 999"
                                         class="pv-img ">
                                </div>
                            </div>
                        </template>

                        <Radio @mouseenter="handleMouseEnter($event, index)"
                               @touchstart="handleTouchStart"
                               @touchend="handleTouchEnd($event,variant,index)"
                               @mouseleave="hovered_item = null"
                               @click="changeVariant(variant,index)" class="pv-div"
                               :value="variant">
                            <div :style="{...(outerBorder(variant)), opacity: list_img[index].available ? 1 : 0.4}"
                                 class="pv-outer-border pv-swatch_circle_in_square">
                                <div class="pv-inner-border" :style="innerBorder(variant)">
                                    <img @load="trackImage" :src="list_img[index].src || default_url_img"
                                         alt="" style="width: 100%"
                                         :style="[getImageStyle(index)]"
                                         class="pv-img pv-shopify-image">
                                    <img v-if="!list_img[index].available" alt="" class="pv-outstock"
                                         src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png">
                                </div>
                            </div>
                        </Radio>
                    </Tooltip>
                </RadioGroup>
            </div>
            <div v-else-if="design_setting.display_style === 'swatch_in_pill'">
                <RadioGroup v-model:value="select_variant_template_id" style="display: flex; flex-wrap: wrap"
                            :style="{gap: `${design_setting.swatch_spacing}px`}">

                    <Tooltip color="#FFFFFF"
                             v-for="(variant,index) in variant_template_ids">
                        <template #title
                                  v-if="design_setting.hover_show_variant_description || design_setting.hover_show_tooltip">
                            <span
                                v-if="design_setting.hover_show_variant_description && !design_setting.hover_show_tooltip">
                                {{ swatch_value(index) }}
                            </span>
                            <div v-else-if="design_setting.hover_show_tooltip" class="pv-swatch_circle_in_square">
                                <div v-if="design_setting.hover_show_variant_description" style="color: #333"
                                     :style="{ width: `${generateToolTipHeight}px`}"
                                     class="pv-flex-row-center">
                                    {{ swatch_value(index) }}
                                </div>
                                <div
                                    :style="{height: `${generateToolTipHeight}px`, width: `${generateToolTipHeight}px`,...innerBorderTipTool(index)}">
                                    <img :src="list_img[index].src || default_url_img"
                                         alt="" style="width: 100%; z-index: 999" class="pv-img" @load="trackImage"
                                         :style="imageSettings">
                                </div>
                            </div>
                        </template>

                        <Radio :value="variant" class="pv-div"
                               @touchstart="handleTouchStart"
                               @touchend="handleTouchEnd($event,variant,index)"
                               @mouseenter="handleMouseEnter($event, index)"
                               @mouseleave="hovered_item = null"
                               @click="changeVariant(variant,index)"
                               style="padding: 0">
                            <div
                                :style="{...(outerBorder(variant)), opacity: list_img[index].available ? 1 : 0.4, padding: `0 ${design_setting.border_spacing}px`}"
                                class="pv-outer-border" style="justify-content: unset !important; gap: 5px">
                                <div class="pv-inner-border" :style="innerBorder(variant)"
                                     style="overflow: hidden; position: relative">
                                    <img @load="trackImage" :src="list_img[index].src || default_url_img"
                                         alt="" style="width: 100%"
                                         :style="[getImageStyle(index)]"
                                         class="pv-img pv-shopify-image">
                                    <img v-if="!list_img[index].available" alt="" class="pv-outstock"
                                         src="https://app.nestscale.com/nestprdvariant/static/images/design_setting/Vector72.png">
                                </div>
                                <div class="pv-pill">
                                    {{ swatch_value(index) }}
                                </div>
                            </div>
                        </Radio>
                    </Tooltip>
                </RadioGroup>
            </div>
        </div>
    </div>
</template>
<script>
import {Radio, RadioGroup, Select, SelectOption, Tooltip} from "ant-design-vue"
import {DownOutlined} from "@ant-design/icons-vue"
import axios from "axios";
import OptionTitle from "./ProductPage/OptionTitle.vue";

export default {
    name: "ProductVariant",
    data() {
        return {
            max_width: 500,
            checkCustomDropdown: true,
            select_variant_template_id: '',
            design_setting: {},
            option_setting_color_custom_image: [],
            selectOptionSquareInDropdown: '',
            openDropdown: false,
            selected_dropdown_value: '',
            hovered_item: null,
            observer_position: null,
            touchStartY: 0,
            touchStartX: 0,
            money_format: ''
        }
    },
    components: {
        OptionTitle,
        Radio,
        RadioGroup,
        Select,
        SelectOption, Tooltip,
        DownOutlined
    },
    props: {
        list_img: Array,
        list_option: Array,
        list_checked_option: Array,
        input_type: String,
        position: Number,
        default_url_img: String,
        list_variants: Array,
        isConflictTheme: Boolean,
        pv_data: [Object, Boolean],
        variant_template_ids: Object,
        block_element_selector: String,
        option_block_selector: String,
        themeData: Object,
        option_information: Object
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
        select_variant_template_id() {
            for (let variant of this.variant_template_ids) {
                if (variant === this.select_variant_template_id) {
                    this.selected_dropdown_value = variant.value
                }
            }
        }
    },
    computed: {
        isMobileDevice() {
            const userAgent = navigator.userAgent || navigator.vendor || window.opera;
            return /android|avantgo|bada\/|blackberry|bolt|boost|cricket|docomo|fone|hiptop|mini|mobi|palm|phone|pie|plucker|pocket|psp|symbian|treo|up\.browser|up\.link|webos|wince/i.test(userAgent) ||
                /iemobile|windows phone/i.test(userAgent) ||
                /iphone|ipod|ipad/i.test(userAgent) && !window.MSStream;
        },
        generateToolTipHeight() {
            return this.design_setting.img_height * (parseInt(this.design_setting.hover_scaling_size) / 100)
        },
        generateToolTipWidth() {
            return this.design_setting.img_width * (parseInt(this.design_setting.hover_scaling_size) / 100)
        },
        option_setting_color_custom_image_choosen() {
            return this.option_setting_color_custom_image[this.index_of_option_variant]
        },
        index_of_option_variant() {
            return this.list_checked_option[this.position]
        },
        labelValue() {
            return this.option_information.values[this.list_checked_option[this.position]]
        },
        swatch_value(index = 0) {
            return this.option_information.values[index]
        }
    },
    methods: {
        handleTouchStart(event) {
            this.touchStartY = event.touches[0].clientY;
            this.touchStartX = event.touches[0].clientX;
        },
        handleTouchEnd(event, variantTemplateId, index) {
            const touchEndY = event.changedTouches[0].clientY;
            const touchEndX = event.changedTouches[0].clientX;

            const deltaY = Math.abs(touchEndY - this.touchStartY);
            const deltaX = Math.abs(touchEndX - this.touchStartX);

            // Threshold for detecting scroll vs touch (can be adjusted)
            const threshold = 10;

            if (deltaY < threshold && deltaX < threshold) {
                this.changeVariant(variantTemplateId, index);
            }
        },
        handleMouseEnter(event, index) {
            this.hovered_item = {
                index: index,
                event: event
            }
        },
        imageSettings() {
            let imageStyle = {};
            switch (this.design_setting.img_position) {
                case "center":
                    imageStyle = {
                        top: '50%',
                        left: '50%',
                        transform: 'translate(-50%, -50%) '
                    };
                    break;
                case "top":
                    imageStyle = {
                        top: '0',
                        left: '0',
                        right: '0',
                    };
                    break;
                case "bottom":
                    imageStyle = {
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
                    if (this.hovered_item.index === item) {
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
                    e.target.style.transform = ""
                    e.target.style.transition = ""
                    e.target.classList.remove("imgWidthBigger")
                    e.target.setAttribute('data-flag', 'false');
                    let styles = this.imageSettings()
                    Object.keys(styles).forEach(style => {
                        e.target.style[style] = styles[style];
                    });

                }
            }

        },
        trackClickOutsideBlock: function (parentElement, block_id, state) {
            document.addEventListener('click', event => {
                const parent_element = document.getElementById(parentElement)
                const clickedElement = event.target
                if (parent_element !== null) {
                    if (!parent_element.contains(clickedElement)) {
                        const targetBlock = document.getElementById(block_id)
                        if (targetBlock) {
                            if (!targetBlock.contains(clickedElement)) {
                                if (this[state] === true) {
                                    this[state] = false
                                }
                            }
                        }
                    }
                }
            })
        },
        outerBorder(variant) {
            const isSelected = this.select_variant_template_id === variant
            let isHovered = false
            if (this.hovered_item !== null) {
                isHovered = this.design_setting.hover_show_shadow && this.hovered_item.index === variant;
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
                height: `${this.design_setting.style_height}px`,
                width: `${this.design_setting.style_width}px`
            };
            if (isHovered) {
                styleObject.boxShadow = `0px 0px ${this.design_setting.hover_shadow_blur}px ${this.design_setting.hover_shadow_thickness}px ${this.design_setting.hover_shadow}`;
            }
            return styleObject;
        },
        outerBorderDropdown(variant) {
            if (this.select_variant_template_id == variant) {
                return {
                    background: '#e6f7ff',
                    height: `${this.design_setting.img_height + 10}px`
                }
            }
            return {height: `${this.design_setting.img_height + 10}px`}
        },
        innerBorderTipTool(variant) {
            let borderRadius = this.design_setting.unselected_inner_border_radius + 'px'
            let border = `${this.design_setting.unselected_inner_border} ${this.design_setting.unselected_inner_border_thickness}px solid`
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
        innerBorderDropdown(variant) {
            return {
                height: `${this.design_setting.img_height}px`,
                width: `${this.design_setting.img_width}px`,
                border: `${this.design_setting.dropdown_inner_border} solid ${this.design_setting.dropdown_inner_border_thickness}px`,
                borderRadius: `${this.design_setting.dropdown_inner_border_radius}px`
            }
        },
        innerBorder(variant) {
            let borderRadius = this.design_setting.unselected_inner_border_radius + 'px'
            let border = `${this.design_setting.unselected_inner_border} ${this.design_setting.unselected_inner_border_thickness}px solid`
            if (this.select_variant_template_id == variant) {
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
        changeVariantTouch(event, variant, index) {
            // event.preventDefault();
            if (this.isMobileDevice) {
                this.select_variant_template_id = variant
            }
            this.changeVariant(variant, index)
        },
        changeVariant(variant, index) {
            switch (this.input_type){
                case 'checkbox':{
                    this.changeCheckboxTypeVariant(index)
                    break;
                }
                case 'select': {
                    this.changeSelectTypeVariant(index)
                    break
                }
                case 'button': {
                    this.changeButtonTypeVariant(index)
                    break
                }
                default: {
                    this.changeDataSwatchItemVariant(index)
                }
            }
            this.observer_position = this.position
        },
        changeCheckboxTypeVariant(index) {
            this.list_checked_option[this.position] = index
            let option = document.querySelector(this.block_element_selector).querySelectorAll(this.option_block_selector)[this.position]
                .querySelectorAll("input:not([type='hidden'])")[index]
            option.click()
        },
        changeSelectTypeVariant(index) {
            this.list_checked_option[this.position] = index
            let select = document.querySelector(this.block_element_selector).querySelectorAll(this.option_block_selector)[this.position].querySelector('select')
            let option = document.querySelector(this.block_element_selector).querySelectorAll(this.option_block_selector)[this.position]
                .querySelector('select').querySelectorAll('option:not([disabled])')[index]
            option.selected = true
            option.dispatchEvent(new Event("change", {
                bubbles: true
            }));
            select.value = option.value;
            let event = new Event('change', {
                bubbles: true,
            });
            select.dispatchEvent(event);
        },
        changeButtonTypeVariant(index) {
            this.list_checked_option[this.position] = index
            let option = document.querySelector(this.block_element_selector).querySelectorAll(this.option_block_selector)[this.position]
                .querySelectorAll('button')[index]
            option.click()
            option.dispatchEvent(new Event("change", {
                bubbles: !0
            }));
        },
        changeDataSwatchItemVariant(index) {
            this.list_checked_option[this.position] = index
            let option = document.querySelector(this.block_element_selector).querySelectorAll(this.option_block_selector)[this.position]
                .querySelectorAll('div[data-swatch-item]')[index]
            option.click()
            option.dispatchEvent(new Event("change", {
                bubbles: !0
            }));
        },
        getPrice(amount) {

            let money_format_currency = this.money_format
            let money_number_type_currency = this.extractContentBrace(money_format_currency)
            let money_replace_currency = this.formatNumber(amount / 100, money_number_type_currency)
            return money_format_currency.replace(/\{\{.*?\}\}/g, money_replace_currency);
        },
        extractContentBrace(str) {
            let matches = str.match(/\{\{([^}]+)\}\}/);
            return matches ? matches[1].trim() : '';
        },
        formatNumber(amount, formatType) {
            switch (formatType) {
                case 'amount':
                    return amount.toFixed(2);
                case 'amount_no_decimals':
                    return Math.round(amount);
                case 'amount_with_comma_separator':
                    return amount.toFixed(2).replace('.', ',');
                case 'amount_no_decimals_with_comma_separator':
                    return Math.round(amount).toString().replace('.', ',');
                case 'amount_with_apostrophe_separator':
                    return amount.toFixed(2).replace('.', '\'');
                default:
                    return amount.toString();
            }
        },
        detectMaxwidth() {
            let form = document.querySelector("form[action='/cart/add']")
            this.max_width = form?.offsetWidth === 0 ? this.max_width : form?.offsetWidth
        },
        setConflictTheme() {
            const observer = new PerformanceObserver((list) => {
                for (const entry of list.getEntries()) {
                    if (entry.initiatorType === "fetch") {
                        let list = ["/products", "/variant"]
                        if (list.some(element => {
                            return entry.name.includes(element)
                        })) {
                            if (this.observer_position !== null) {
                                let option_blocks
                                if (this.isConflictTheme) {
                                    let block_element = document.querySelector(this.themeData.parent_type_value)
                                    option_blocks = block_element.querySelectorAll(this.themeData.option_type_value)
                                } else {
                                    let block_element = document.querySelector(this.block_element_selector)
                                    option_blocks = block_element.querySelectorAll(this.option_block_selector)
                                }
                                option_blocks[this.observer_position].style.display = 'none'
                            }

                        }
                    }
                }
            })
            observer.observe({
                entryTypes: ["resource"]
            })
        },
        addEventListenerOption(option_blocks) {
            option_blocks[this.position].style.display = 'block'
            document.getElementById('pv-frontend-block-' + this.position).style.display = 'none'
            this.observer_position = null
            switch (this.input_type === 'select') {
                case 'select': {
                    this.addEventListenerOptionSelect(option_blocks)
                    break;
                }
                case 'checkbox': {
                    this.addEventListenerOptionCheckbox(option_blocks)
                    break;
                }
                default: {
                    this.addEventListenerOptionButton(option_blocks)
                }
            }
        },
        addEventListenerOptionSelect(option_blocks) {
            let inputs_default_list = option_blocks[this.position].querySelector("select")
            let option_list = inputs_default_list.querySelectorAll("option:not([disabled])")
            if (option_list.length != this.variant_template_ids.length) {
                option_list = inputs_default_list.querySelectorAll('option')
            }
            inputs_default_list.addEventListener('change', () => {
                for (let j = 0; j < option_list.length; j++) {
                    if (option_list[j].selected) {
                        this.list_checked_option[this.position] = j
                    }
                }
            })
        },
        addEventListenerOptionCheckbox(option_blocks) {
            let inputs_default_list = option_blocks[this.position].querySelectorAll("input:not([type='hidden'])")
            for (let i = 0; i < inputs_default_list.length; i++) {
                inputs_default_list[i].addEventListener('change', () => {
                    this.list_checked_option[this.position] = i
                })
            }
        },
        addEventListenerOptionButton(option_blocks) {
            let inputs_default_list = option_blocks[this.position].querySelectorAll('button')
            for (let i = 0; i < inputs_default_list.length; i++) {
                inputs_default_list[i].addEventListener('change', () => {
                    this.list_checked_option[this.position] = i
                })
            }
        },
        getBlockElement() {
            if (this.isConflictTheme) {
                return document.querySelector(this.themeData.parent_type_value)
            } else {
                return document.querySelector(this.block_element_selector)
            }
        }
        ,
        getOptionBlocks(block_element) {
            if (this.isConflictTheme) {
                return block_element.querySelectorAll(this.themeData.option_type_value)
            } else {
                return block_element.querySelectorAll(this.option_block_selector)
            }
        }
    },
    async mounted() {
        this.detectMaxwidth()
        if (nestvariant_currency_symbol !== undefined) {
            this.money_format = nestvariant_currency_symbol
        }
        this.observer_position = this.position
        this.select_variant_template_id = this.variant_template_ids[this.list_checked_option[this.position]]

        let block_element = this.getBlockElement()
        let option_blocks = this.getOptionBlocks(block_element)

        this.trackClickOutsideBlock('pv-swatch-in-dropdown-' + this.position, "pv-open-dropdown-" + this.position, 'openDropdown')
        if (!this.pv_data) {
            option_blocks[this.position].style.display = 'block'
            this.observer_position = null
        } else {
            if (!this.pv_data.option_setting.status) {
                this.addEventListenerOption(option_blocks)
            }
            this.design_setting = this.pv_data.design_setting
            if ('option_setting_color_custom_image' in this.pv_data) {
                for (let i = 0; i < this.option_information.values.length; i++) {
                    let index = this.pv_data.option_setting_color_custom_image
                        .findIndex(setting => setting.variant_option_value === this.swatch_value(i))
                    this.option_setting_color_custom_image.push({
                        ...this.pv_data.option_setting_color_custom_image[index],
                        variant_template_id: this.variant_template_ids[i]
                    })
                }
            }
        }
        this.setConflictTheme()
    }
}
</script>