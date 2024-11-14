<template>
    <div class="pv-block pv-block-option" :id="`pv-block-options-setting-item-${options_setting_item_index}`">
        <div class="pv-flex-column" style="gap: 24px">

            <div class="pv-center-align" style="justify-content: space-between">
                <div>
                    <div v-if="mode === 'option_setting'" class="pv-value-of-variant-option">{{ option.name }}</div>
                    <div v-else class="pv-value-of-variant-option">{{ `${option.group_name} (${option.name})` }}</div>
                </div>
                <Dropdown :trigger="['click']" v-if="mode === 'product_group'">
                    <template #overlay>
                        <Menu>
                            <MenuItem @click="this.$emit('openProductManagement',option,options_setting_item_index)">
                                <div style="gap: 8px" class="pv-center-align">
                                    <svg width="16" height="16" viewBox="0 0 16 16" fill="none"
                                         xmlns="http://www.w3.org/2000/svg">
                                        <path fill-rule="evenodd" clip-rule="evenodd"
                                              d="M10.5316 2.0426C11.4777 1.09648 13.0116 1.09648 13.9577 2.0426C14.9039 2.98872 14.9039 4.52268 13.9577 5.4688L6.95476 12.4718C6.94672 12.4798 6.93879 12.4877 6.93096 12.4956C6.787 12.6396 6.67541 12.7513 6.54921 12.8492C6.43772 12.9357 6.31918 13.0128 6.19485 13.0795C6.05409 13.1551 5.90674 13.2117 5.71663 13.2847C5.7063 13.2887 5.69583 13.2927 5.68523 13.2968L5.62377 13.3204C5.60921 13.3261 5.5948 13.3316 5.58063 13.3371C5.57443 13.3394 5.56828 13.3418 5.56218 13.3441L2.23999 14.6219C1.99409 14.7165 1.71556 14.6574 1.52927 14.4711C1.34297 14.2848 1.28386 14.0063 1.37844 13.7604L2.65622 10.4382C2.65856 10.4321 2.66093 10.4259 2.66331 10.4197L2.70353 10.3151C2.70761 10.3045 2.71163 10.294 2.71561 10.2837C2.78866 10.0936 2.84529 9.94624 2.92084 9.80549C2.98758 9.68115 3.06462 9.56262 3.15113 9.45113C3.24906 9.32493 3.36071 9.21334 3.50476 9.06938C3.5126 9.06155 3.52053 9.05361 3.52857 9.04558L10.5316 2.0426ZM3.80677 11.1609L3.16137 12.839L4.8394 12.1936L3.80677 11.1609ZM6.03612 11.5048C6.01754 11.4861 5.99911 11.4676 5.98117 11.4497C5.97647 11.445 5.9718 11.4404 5.96718 11.4357L4.56463 10.0332C4.56001 10.0286 4.55535 10.0239 4.55065 10.0192C4.53272 10.0013 4.51428 9.98281 4.49554 9.96422L11.4744 2.9854C11.8998 2.55999 12.5895 2.55999 13.0149 2.98541C13.4404 3.41083 13.4404 4.10057 13.0149 4.52599L6.03612 11.5048ZM8.334 13.9997C8.334 13.6315 8.63248 13.333 9.00067 13.333H13.9674C14.3356 13.333 14.6341 13.6315 14.6341 13.9997C14.6341 14.3679 14.3356 14.6663 13.9674 14.6663H9.00067C8.63248 14.6663 8.334 14.3679 8.334 13.9997Z"
                                              fill="#666666"/>
                                    </svg>
                                    <span>Product management</span>
                                </div>
                            </MenuItem>
                            <MenuItem @click="openConfirmDelete">
                                <div style="gap: 8px" class="pv-center-align">
                                    <svg width="16" height="16" viewBox="0 0 16 16" fill="none"
                                         xmlns="http://www.w3.org/2000/svg">
                                        <path
                                            d="M14.0007 3.33366H11.334C11.334 2.59366 11.3207 2.16033 11.114 1.75366C10.9207 1.38033 10.6073 1.07363 10.2473 0.886963C9.82065 0.666963 9.36065 0.666992 8.53398 0.666992H7.46732C6.64065 0.666992 6.18732 0.666963 5.76065 0.886963C5.39398 1.07363 5.08065 1.38034 4.88732 1.76034C4.68065 2.167 4.66732 2.59366 4.66732 3.33366H2.00065C1.63398 3.33366 1.33398 3.63366 1.33398 4.00033C1.33398 4.36699 1.63398 4.66699 2.00065 4.66699H2.66732V11.467C2.66732 12.6936 2.66732 13.3069 2.95398 13.8736C3.20732 14.3803 3.62732 14.7936 4.12065 15.0403C4.69398 15.3336 5.34732 15.3337 6.53398 15.3337H9.46732C10.654 15.3337 11.3073 15.3336 11.874 15.047C12.374 14.8003 12.794 14.3803 13.0473 13.8803C13.3407 13.3136 13.3407 12.6936 13.3407 11.4736V4.67367H14.0073C14.374 4.67367 14.674 4.37367 14.674 4.007C14.674 3.64033 14.374 3.34033 14.0073 3.34033L14.0007 3.33366ZM6.07398 2.36694C6.14065 2.24028 6.24065 2.13365 6.36732 2.07365C6.50732 2.00032 6.89398 2.00033 7.46732 2.00033H8.53398C9.11398 2.00033 9.49398 2.00032 9.64065 2.07365C9.76065 2.13365 9.86732 2.24027 9.92732 2.36027C9.99399 2.4936 10.0007 2.82699 10.0007 3.33366H6.00065C6.00065 2.82699 6.00065 2.49361 6.07398 2.36694ZM12.0007 11.467C12.0007 12.447 12.0007 12.9869 11.854 13.2736C11.7273 13.5269 11.5207 13.7269 11.2673 13.8536C10.9807 14.0003 10.4407 14.0003 9.46065 14.0003H6.52732C5.54732 14.0003 5.00732 14.0003 4.71398 13.847C4.46732 13.727 4.26732 13.5203 4.13398 13.267C3.98732 12.9803 3.98732 12.447 3.98732 11.467V4.66699H11.9873V11.467H12.0007Z"
                                            fill="#666666"/>
                                    </svg>
                                    <span>Delete</span>
                                </div>
                            </MenuItem>
                        </Menu>
                    </template>
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M12 14C13.1 14 14 13.1 14 12C14 10.9 13.1 10 12 10C10.9 10 10 10.9 10 12C10 13.1 10.9 14 12 14Z"
                            fill="#666666"/>
                        <path d="M12 7C13.1 7 14 6.1 14 5C14 3.9 13.1 3 12 3C10.9 3 10 3.9 10 5C10 6.1 10.9 7 12 7Z"
                              fill="#666666"/>
                        <path
                            d="M12 21C13.1 21 14 20.1 14 19C14 17.9 13.1 17 12 17C10.9 17 10 17.9 10 19C10 20.1 10.9 21 12 21Z"
                            fill="#666666"/>
                    </svg>
                </Dropdown>
            </div>


            <div style="margin-top: 4px; gap: 8px" class="pv-option pv-flex-column">
                <div class="pv-design-item-component">
                    <div class="pv-option-label">Display style in Product page</div>


                    <div class="pv-flex-row-center" style="gap: 8px">
                        <div v-if="option.status" class="pv-option-label" style="color:#1677FF !important;">Active</div>
                        <div v-else class="pv-option-label">Inactive</div>
                        <Switch v-model:checked="option.status"/>
                    </div>

                </div>
                <Select v-model:value="display_style" class="pv-select-variant-option"
                        @change="selectDisplayStyle(option)">
                    <SelectOption value="swatch_circle_in_square">Swatch circle in square</SelectOption>
                    <SelectOption value="swatch_in_box">Swatch in box</SelectOption>
                    <SelectOption value="swatch_in_dropdown">Swatch in dropdown</SelectOption>
                    <SelectOption value="circular_swatch">Circular swatch</SelectOption>
                    <SelectOption value="square_swatch">Square swatch</SelectOption>
                    <SelectOption value="swatch_in_pill">Swatch in pill</SelectOption>
                </Select>
            </div>
            <div style="margin-top: 4px; gap: 8px" class="pv-option pv-flex-column">
                <div class="pv-design-item-component" v-if="mode !== 'product_group'">
                    <div class="pv-option-label">Display style in Collection page</div>
                    <div class="pv-flex-row-center" style="gap: 8px">
                        <div v-if="option.status_collection_page && is_has_plan" class="pv-option-label"
                             style="color:#1677FF !important;">Active
                        </div>
                        <div v-else class="pv-option-label">Inactive</div>
                        <Switch v-if="is_has_plan " v-model:checked="option.status_collection_page"/>
                        <Switch v-else disabled="true"/>
                    </div>
                </div>
                <div v-else class="pv-design-item-component">
                    <div class="pv-option-label">Display style in Collection page</div>
                    <div class="pv-flex-row-center" style="gap: 8px">
                        <div v-if="option.status_collection_page" class="pv-option-label"
                             style="color:#1677FF !important;">Active
                        </div>
                        <div v-else class="pv-option-label">Inactive</div>
                        <Switch v-model:checked="option.status_collection_page"/>
                    </div>
                </div>
                <Select v-model:value="display_type_collection_page" class="pv-select-variant-option"
                        :disabled="!is_has_plan && mode !== 'product_group'"
                        @change="selectDisplayStyleCollectionPage(option)">
                    <SelectOption value="swatch_circle_in_square">Swatch circle in square</SelectOption>

                    <SelectOption value="circular_swatch">Circular swatch</SelectOption>
                    <SelectOption value="square_swatch">Square swatch</SelectOption>
                </Select>
                <div class="pv-small-font" v-if="!is_has_plan">Use this feature with Growth version.<span
                    @click="$emit('changePage','plans_billing')"
                    style="color: #1890FF;cursor: pointer">Upgrade now</span></div>
            </div>
            <div style="gap: 8px" class="pv-option pv-flex-column">
                <div class="pv-option-label">Option Images</div>
                <Select v-model:value="option_img" class="pv-select-variant-option"
                        @change="selectOptionImages(option)">
                    <SelectOption value="variant_image">Variant image</SelectOption>
                    <SelectOption value="color_custom_image">Color/Custom Image</SelectOption>
                </Select>


                <div v-if="option_img === 'color_custom_image'" @click="openModalInputColorCustomImage(option)"
                     class="pv-flex-row pv-center-align" style="gap: 8px">
                    <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd"
                              d="M9.21487 1.78788C10.0427 0.960028 11.3849 0.96003 12.2128 1.78788C13.0406 2.61574 13.0406 3.95795 12.2128 4.78581L6.08517 10.9134C6.07814 10.9204 6.0712 10.9274 6.06434 10.9342C5.93838 11.0603 5.84074 11.158 5.73031 11.2437C5.63276 11.3194 5.52904 11.3868 5.42025 11.4452C5.29709 11.5113 5.16815 11.5608 5.00181 11.6248C4.99276 11.6282 4.98361 11.6318 4.97434 11.6353L4.92055 11.656C4.90781 11.6609 4.89521 11.6658 4.88281 11.6705C4.87738 11.6726 4.872 11.6747 4.86667 11.6767L1.95975 12.7948C1.74459 12.8775 1.50087 12.8258 1.33786 12.6628C1.17486 12.4998 1.12314 12.2561 1.20589 12.0409L2.32395 9.13401C2.326 9.12867 2.32807 9.12329 2.33015 9.11786L2.36535 9.02633C2.36891 9.01706 2.37243 9.0079 2.37591 8.99885C2.43983 8.83251 2.48938 8.70357 2.55549 8.58042C2.61389 8.47162 2.68129 8.3679 2.75699 8.27035C2.84269 8.15992 2.94038 8.06228 3.06642 7.93632C3.07328 7.92946 3.08022 7.92252 3.08725 7.91549L9.21487 1.78788ZM3.33068 9.76643L2.76595 11.2347L4.23423 10.67L3.33068 9.76643ZM5.28136 10.0673C5.26511 10.0509 5.24897 10.0348 5.23328 10.0191C5.22917 10.015 5.22508 10.0109 5.22103 10.0069L3.9938 8.77965C3.98976 8.7756 3.98569 8.77152 3.98158 8.76741C3.96589 8.75171 3.94976 8.73557 3.93335 8.71931L10.0398 2.61284C10.4121 2.2406 11.0156 2.2406 11.3878 2.61284C11.7601 2.98508 11.7601 3.58861 11.3878 3.96085L5.28136 10.0673Z"
                              fill="#1677FF"/>
                    </svg>
                    <div style="color: #1890FF;cursor: pointer" class="pv-option-label">Edit swatch</div>
                </div>
            </div>

        </div>
    </div>
    <Modal v-model:visible="modalOpenConfirmDelete" centered
           :closable="false"
           class="pv-modal pv-product-select pv-delete-confirm"
           style="max-width: 295px; border-radius: 6px">
        <template #footer style="display: flex">
            <div class="pv-flex-row pv-center-align pv-justify-center" style="gap: 8px;width: 100%">
                <div @click="modalOpenConfirmDelete = false" class="pv-confirm-modal-delete-button"
                     style="color: #333;background: #FFFFFF;border: 1px solid #D9D9D9;">
                    Cancel
                </div>
                <div @click="deleteProductGroup"
                     class="pv-confirm-modal-delete-button"
                     style="color: #FFFFFF;background: #F5222D;border: 1px solid #D9D9D9;">Confirm
                </div>
            </div>
        </template>
        <div class="pv-flex-column pv-center-align" style="gap: 16px">
            <svg width="57" height="56" viewBox="0 0 57 56" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path
                    d="M19.844 36.6563C20.754 37.5663 22.224 37.5663 23.134 36.6563L28.4773 31.3129L33.8207 36.6563C34.2873 37.123 34.8707 37.3331 35.4773 37.3331C36.084 37.3331 36.6673 37.0996 37.134 36.6563C38.044 35.7463 38.044 34.2762 37.134 33.3662L31.7907 28.0231L37.134 22.6797C38.044 21.7697 38.044 20.2996 37.134 19.3896C36.224 18.4796 34.754 18.4796 33.844 19.3896L28.5007 24.733L23.1573 19.3896C22.2473 18.4796 20.7773 18.4796 19.8673 19.3896C18.9573 20.2996 18.9573 21.7697 19.8673 22.6797L25.2107 28.0231L19.8673 33.3662C18.9573 34.2762 18.9573 35.7463 19.8673 36.6563H19.844Z"
                    fill="#F5222D"/>
                <path
                    d="M28.5007 53.6663C42.664 53.6663 54.1673 42.163 54.1673 27.9997C54.1673 13.8363 42.664 2.33301 28.5007 2.33301C14.3373 2.33301 2.83398 13.8597 2.83398 27.9997C2.83398 42.1397 14.3373 53.6663 28.5007 53.6663ZM28.5007 6.99967C40.074 6.99967 49.5007 16.4263 49.5007 27.9997C49.5007 39.573 40.074 48.9997 28.5007 48.9997C16.9273 48.9997 7.50065 39.573 7.50065 27.9997C7.50065 16.4263 16.9273 6.99967 28.5007 6.99967Z"
                    fill="#F5222D"/>
            </svg>
            <div class="pv-flex-column pv-center-align">
                <span style="color:#1A1A1A;font-size: 20px;font-weight: 600;line-height: 28px;">
                    Delete {{ option.group_name }}
                </span>
                <span style="color: #666;font-size: 14px;font-weight: 400;line-height: 22px;">
                    This action cannot be undone.
                </span>
            </div>
        </div>
    </Modal>
</template>
<script>
import {Button, Dropdown, Input, Menu, MenuItem, Modal, Select, SelectOption, Switch} from "ant-design-vue"

export default {
    name: "OptionsSettingItem",
    data() {
        return {
            display_style: 'swatch_circle_in_square',
            option_img: "variant_image",
            imageSelection: 'first_image',
            isShow: false,

            display_type_collection_page: 'swatch_circle_in_square',
            modalOpenConfirmDelete: false,
        }
    },
    components: {
        Modal,
        Menu, MenuItem, Button, Dropdown,
        Input,
        Select, Switch,
        SelectOption
    },
    props: {
        option: {
            type: Object,
            default: {},
        },
        mode: String,
        options_setting_item_index: Number,
        is_has_plan: Boolean
    },
    emits: ['selectDisplayStyle', "openModalUploadSwatch", 'selectOptionImages', 'selectDisplayStyleCollectionPage'],
    methods: {
        deleteProductGroup() {
            this.$emit('openDeleteProduct', this.option);
            this.modalOpenConfirmDelete = false
        },
        openConfirmDelete() {
            this.modalOpenConfirmDelete = true
        },
        selectDisplayStyle(option) {
            this.$emit('selectDisplayStyle', option, this.display_style)
        },
        selectDisplayStyleCollectionPage(option) {
            this.$emit('selectDisplayStyleCollectionPage', option, this.display_type_collection_page)
        },
        selectOptionImages(option) {
            this.$emit('selectOptionImages', option, this.option_img)
        },
        openModalInputColorCustomImage(option) {
            this.$emit("openModalUploadSwatch", true, option, this.options_setting_item_index)
        },
        trackClickOutsideBlock: function (parentElement, block_id, state) {
            document.addEventListener('click', (event) => {
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
        }
    },
    mounted() {
        this.trackClickOutsideBlock(
            `pv-block-options-setting-item-${this.options_setting_item_index}`,
            `pv-affect-popup-${this.options_setting_item_index}`,
            'isShow'
        )
        this.display_style = this.option.display_style
        this.display_type_collection_page = this.option.display_type_collection_page
        this.option_img = this.option.option_img
    }
}
</script>