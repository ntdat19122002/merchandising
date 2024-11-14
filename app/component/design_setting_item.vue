<template>
    <div class="pv-flex-column">
        <div style="position: sticky;top: 0;z-index: 999;"
             :class=" scrollPosition !== 0 ? 'pv-sticky-menu':'pv-not-sticky-menu'">
            <div class="pv-design-setting-back-to-previous-page" @click="backToPreviousPage">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                    <path d="M15 18L9 12L15 6" stroke="black" stroke-width="2" stroke-linecap="round"
                          stroke-linejoin="round"/>
                </svg>
                <div class="pv-back-to-previous-page">Back to previous page</div>
            </div>
            <div style="display: flex; justify-content: space-between; height: 36px">
                <div class="pv-design-item-name">{{ designItemName }}</div>
                <div class="pv-flex-row-center" style="gap: 8px">
                    <div style="gap: 16px; display: flex" v-if="design_is_change">
                        <div class="pv-btn-secondary pv-flex-row-center" @click="cancelDesignSetting">
                            <svg width="14" height="14" viewBox="0 0 14 14" fill="none"
                                 xmlns="http://www.w3.org/2000/svg">
                                <path
                                    d="M11.2542 1.92085C11.3681 1.80698 11.5173 1.75003 11.6666 1.75C11.8159 1.74997 11.9652 1.80693 12.0791 1.92085C12.307 2.14866 12.307 2.51801 12.0791 2.74581L7.82486 7L12.079 11.2542C12.3069 11.482 12.3069 11.8513 12.079 12.0791C11.9651 12.193 11.8159 12.25 11.6666 12.25C11.5173 12.25 11.368 12.193 11.2541 12.0791L6.9999 7.82496L2.74638 12.0791C2.63234 12.1932 2.48281 12.2501 2.33333 12.25C2.18424 12.2499 2.03518 12.1929 1.92143 12.0791C1.69362 11.8513 1.69362 11.482 1.92143 11.2542L6.17494 7L1.92085 2.74581C1.69305 2.51801 1.69305 2.14866 1.92085 1.92085C2.03473 1.80698 2.18398 1.75003 2.33323 1.75C2.48255 1.74997 2.63188 1.80693 2.74581 1.92085L6.9999 6.17504L11.2542 1.92085Z"
                                    fill="#F5222D"/>
                            </svg>
                            <span class="pv-button-style" style="color: #F5222D">Cancel</span>
                        </div>
                        <div class="pv-btn-primary" @click="saveDesignSetting">
                            <svg width="14" height="14" viewBox="0 0 14 14" fill="none"
                                 xmlns="http://www.w3.org/2000/svg">
                                <path
                                    d="M12.5823 4.23533C12.4773 4.06616 12.3607 3.94364 12.1215 3.70448L10.354 1.9428C10.354 1.9428 10.3248 1.91366 10.3132 1.902L10.3015 1.89032C10.0857 1.66865 9.9515 1.54035 9.75317 1.41202C9.57234 1.31285 9.40317 1.24281 9.27484 1.21947C9.07067 1.16697 8.87817 1.16699 8.569 1.16699H4.55567C4.39817 1.16699 4.25817 1.16699 4.11817 1.16699C4.09484 1.16699 4.0715 1.16699 4.04817 1.16699C3.319 1.17283 2.85817 1.20786 2.44984 1.41786C2.01234 1.63369 1.64484 2.00119 1.42317 2.43869C1.1665 2.94036 1.1665 3.47702 1.1665 4.55035V9.4503C1.1665 10.5236 1.1665 11.0604 1.41734 11.5562C1.639 11.9995 2.0065 12.3612 2.43817 12.577C2.85234 12.787 3.31317 12.8278 4.04234 12.8337C4.054 12.8337 4.0715 12.8337 4.08317 12.8337C4.229 12.8337 4.38067 12.8337 4.54984 12.8337H9.44984C9.619 12.8337 9.76484 12.8337 9.9165 12.8337C9.92817 12.8337 9.94567 12.8337 9.95734 12.8337C10.6865 12.8278 11.1473 12.7928 11.5557 12.5828C11.9932 12.367 12.3607 11.9995 12.5823 11.562C12.839 11.0661 12.839 10.5236 12.839 9.45614V5.44864C12.839 5.13947 12.839 4.947 12.7923 4.74283C12.7457 4.56783 12.6757 4.39284 12.5823 4.24117V4.23533ZM4.67234 2.33366H8.56317C8.78484 2.33366 8.919 2.33368 9.01234 2.35701C9.0415 2.35701 9.08817 2.38033 9.1465 2.40949C9.19317 2.43866 9.24567 2.48535 9.339 2.57868V3.73367C9.339 3.89701 9.339 4.06031 9.36817 4.07198C9.3215 4.08365 9.15234 4.08366 8.989 4.08366H5.02234C4.859 4.08366 4.69567 4.08368 4.684 4.10701C4.67234 4.06035 4.67234 3.89117 4.67234 3.72783V2.32782V2.33366ZM9.339 11.667H4.67234V8.51698C4.67234 8.35364 4.67234 8.19034 4.64317 8.17867C4.68984 8.167 4.859 8.16699 5.02234 8.16699H8.989C9.15234 8.16699 9.3215 8.16697 9.32734 8.14364C9.339 8.1903 9.339 8.35948 9.339 8.51698V11.667ZM11.6723 9.4503C11.6723 10.3078 11.6723 10.7803 11.544 11.0312C11.4332 11.2528 11.2523 11.4278 11.0307 11.5387C10.914 11.6028 10.739 11.632 10.4998 11.6495V8.51698C10.4998 8.13781 10.4998 7.88698 10.3715 7.64198C10.2548 7.41448 10.074 7.22781 9.85817 7.12864C9.60734 7.00031 9.3565 7.00033 8.97734 7.00033H5.01067C4.6315 7.00033 4.38067 7.0003 4.1415 7.1228C3.91984 7.2278 3.73317 7.41447 3.62234 7.63614C3.494 7.88697 3.494 8.13781 3.494 8.51698V11.6495C3.25484 11.632 3.07984 11.6028 2.95734 11.5387C2.7415 11.4337 2.5665 11.2528 2.44984 11.0312C2.3215 10.7803 2.3215 10.3136 2.3215 9.45614V4.55619C2.3215 3.69869 2.3215 3.22614 2.44984 2.97531C2.56067 2.75364 2.7415 2.57865 2.96317 2.46781C3.07984 2.40365 3.25484 2.37451 3.494 2.35701V3.73951C3.494 4.11868 3.494 4.37535 3.62234 4.61451C3.739 4.84201 3.92567 5.02868 4.12984 5.12785C4.38067 5.25618 4.6315 5.25616 5.01067 5.25616H8.97734C9.3565 5.25616 9.60734 5.25619 9.8465 5.13369C10.0682 5.02869 10.2548 4.84202 10.3657 4.62035C10.494 4.37535 10.494 4.12452 10.494 3.74535L11.3165 4.5678C11.4565 4.7078 11.544 4.79536 11.5732 4.84786C11.6023 4.90036 11.6315 4.95864 11.6432 5.01698C11.6607 5.08698 11.6607 5.22114 11.6607 5.44864V9.45614L11.6723 9.4503Z"
                                    fill="#BFBFBF"/>
                            </svg>
                            <span class="pv-button-style" style="color: #FFFFFF">Save</span>
                        </div>
                    </div>
                    <Dropdown :trigger="['click']">
                        <template #overlay>
                            <Menu>
                                <MenuItem @click="applyDesignFromProduct" v-if="currentPage === 'collection_page'">
                                    <div style="gap: 8px" class="pv-center-align">
                                        <svg width="16" height="16" viewBox="0 0 16 16" fill="none"
                                             xmlns="http://www.w3.org/2000/svg">
                                            <g clip-path="url(#clip0_369_17479)">
                                                <path fill-rule="evenodd" clip-rule="evenodd"
                                                      d="M5.83913 0.666992H10.1609C10.6975 0.666984 11.1404 0.666977 11.5012 0.696455C11.8759 0.727072 12.2204 0.792782 12.544 0.957642C13.0457 1.2133 13.4537 1.62125 13.7094 2.12302C13.8742 2.44658 13.9399 2.79104 13.9705 3.16578C14 3.52657 14 3.96947 14 4.50611V8.33366C14 8.70185 13.7015 9.00033 13.3333 9.00033C12.9651 9.00033 12.6667 8.70185 12.6667 8.33366V4.53366C12.6667 3.96261 12.6661 3.57441 12.6416 3.27435C12.6178 2.98207 12.5745 2.83261 12.5213 2.72834C12.3935 2.47746 12.1895 2.27348 11.9387 2.14565C11.8344 2.09252 11.6849 2.04924 11.3926 2.02536C11.0926 2.00084 10.7044 2.00033 10.1333 2.00033H5.86667C5.29561 2.00033 4.90742 2.00084 4.60736 2.02536C4.31508 2.04924 4.16561 2.09252 4.06135 2.14565C3.81046 2.27348 3.60649 2.47746 3.47866 2.72834C3.42553 2.83261 3.38225 2.98207 3.35837 3.27435C3.33385 3.57441 3.33333 3.96261 3.33333 4.53366V11.467C3.33333 12.038 3.33385 12.4262 3.35837 12.7263C3.38225 13.0186 3.42553 13.168 3.47866 13.2723C3.60649 13.5232 3.81046 13.7272 4.06135 13.855C4.16561 13.9081 4.31508 13.9514 4.60736 13.9753C4.90742 13.9998 5.29561 14.0003 5.86667 14.0003H8C8.36819 14.0003 8.66667 14.2988 8.66667 14.667C8.66667 15.0352 8.36819 15.3337 8 15.3337H5.83912C5.30248 15.3337 4.85958 15.3337 4.49878 15.3042C4.12405 15.2736 3.77958 15.2079 3.45603 15.043C2.95426 14.7873 2.54631 14.3794 2.29065 13.8776C2.12579 13.5541 2.06008 13.2096 2.02946 12.8349C1.99998 12.4741 1.99999 12.0312 2 11.4945V4.50613C1.99999 3.96948 1.99998 3.52657 2.02946 3.16578C2.06008 2.79104 2.12579 2.44658 2.29065 2.12302C2.54631 1.62125 2.95426 1.2133 3.45603 0.957642C3.77958 0.792782 4.12405 0.727072 4.49878 0.696455C4.85958 0.666977 5.30249 0.666984 5.83913 0.666992ZM4.66667 4.66699C4.66667 4.2988 4.96514 4.00033 5.33333 4.00033H10.6667C11.0349 4.00033 11.3333 4.2988 11.3333 4.66699C11.3333 5.03518 11.0349 5.33366 10.6667 5.33366H5.33333C4.96514 5.33366 4.66667 5.03518 4.66667 4.66699ZM4.66667 7.33366C4.66667 6.96547 4.96514 6.66699 5.33333 6.66699H9.33333C9.70152 6.66699 10 6.96547 10 7.33366C10 7.70185 9.70152 8.00033 9.33333 8.00033H5.33333C4.96514 8.00033 4.66667 7.70185 4.66667 7.33366ZM4.66667 10.0003C4.66667 9.63214 4.96514 9.33366 5.33333 9.33366H6.66667C7.03486 9.33366 7.33333 9.63214 7.33333 10.0003C7.33333 10.3685 7.03486 10.667 6.66667 10.667H5.33333C4.96514 10.667 4.66667 10.3685 4.66667 10.0003ZM14.4714 10.5289C14.7318 10.7893 14.7318 11.2114 14.4714 11.4717L11.4714 14.4717C11.2111 14.7321 10.7889 14.7321 10.5286 14.4717L9.19526 13.1384C8.93491 12.878 8.93491 12.4559 9.19526 12.1956C9.45561 11.9352 9.87772 11.9352 10.1381 12.1956L11 13.0575L13.5286 10.5289C13.7889 10.2686 14.2111 10.2686 14.4714 10.5289Z"
                                                      fill="#666666"/>
                                            </g>
                                            <defs>
                                                <clipPath id="clip0_369_17479">
                                                    <rect width="16" height="16" fill="white"/>
                                                </clipPath>
                                            </defs>
                                        </svg>
                                        <span>Apply design from product page</span>
                                    </div>
                                </MenuItem>
                                <MenuItem @click="resetToDefault">
                                    <div style="gap: 8px" class="pv-center-align">
                                        <svg width="16" height="16" viewBox="0 0 16 16" fill="none"
                                             xmlns="http://www.w3.org/2000/svg">
                                            <g clip-path="url(#clip0_369_4712)">
                                                <path fill-rule="evenodd" clip-rule="evenodd"
                                                      d="M8.00008 2.66634C6.52647 2.66634 5.19352 3.2631 4.22754 4.22975C3.72239 4.73524 3.14876 5.42053 2.68727 5.99967H5.33342C5.7016 5.99967 6.00008 6.29815 6.00008 6.66634C6.00008 7.03453 5.7016 7.33301 5.33342 7.33301H1.33341C0.965225 7.33301 0.666748 7.03453 0.666748 6.66634V2.66634C0.666748 2.29815 0.965225 1.99967 1.33341 1.99967C1.7016 1.99967 2.00008 2.29815 2.00008 2.66634V4.7293C2.40134 4.24133 2.85798 3.71398 3.2844 3.28726C4.49023 2.0806 6.15848 1.33301 8.00008 1.33301C11.682 1.33301 14.6667 4.31778 14.6667 7.99967C14.6667 11.6816 11.682 14.6663 8.00008 14.6663C4.95978 14.6663 2.39642 12.6317 1.59406 9.85118C1.49198 9.49742 1.696 9.12789 2.04976 9.02581C2.40352 8.92373 2.77304 9.12775 2.87512 9.48151C3.51722 11.7067 5.56959 13.333 8.00008 13.333C10.9456 13.333 13.3334 10.9452 13.3334 7.99967C13.3334 5.05416 10.9456 2.66634 8.00008 2.66634Z"
                                                      fill="#666666"/>
                                            </g>
                                            <defs>
                                                <clipPath id="clip0_369_4712">
                                                    <rect width="16" height="16" fill="white"/>
                                                </clipPath>
                                            </defs>
                                        </svg>
                                        <span>Reset settings to default</span>
                                    </div>
                                </MenuItem>
                            </Menu>
                        </template>
                        <Button class="pv-showmore-button">
                            <svg width="14" height="14" viewBox="0 0 14 14" fill="none"
                                 xmlns="http://www.w3.org/2000/svg">
                                <path
                                    d="M6.99992 8.16667C7.64159 8.16667 8.16659 7.64167 8.16659 7C8.16659 6.35833 7.64159 5.83333 6.99992 5.83333C6.35825 5.83333 5.83325 6.35833 5.83325 7C5.83325 7.64167 6.35825 8.16667 6.99992 8.16667Z"
                                    fill="#333333"/>
                                <path
                                    d="M6.99992 4.08333C7.64159 4.08333 8.16659 3.55833 8.16659 2.91667C8.16659 2.275 7.64159 1.75 6.99992 1.75C6.35825 1.75 5.83325 2.275 5.83325 2.91667C5.83325 3.55833 6.35825 4.08333 6.99992 4.08333Z"
                                    fill="#333333"/>
                                <path
                                    d="M6.99992 12.25C7.64159 12.25 8.16659 11.725 8.16659 11.0833C8.16659 10.4417 7.64159 9.91667 6.99992 9.91667C6.35825 9.91667 5.83325 10.4417 5.83325 11.0833C5.83325 11.725 6.35825 12.25 6.99992 12.25Z"
                                    fill="#333333"/>
                            </svg>
                        </Button>
                    </Dropdown>
                </div>
            </div>
        </div>
        <div style="padding: 32px 40px 26px 40px">
            <div class="pv-loading-tag-product" v-if="isLoading">
                <LoadingOutlined/>
                <span>Processing</span>
            </div>
            <Row :gutter="14" v-else>
                <Col :xs="{ span: 24, order: 2 }" :lg="{ span: 16, order: 1 }" class="pv-flex-column" style="gap: 24px">
                    <div class="pv-flex-column pv-design-item-block pv-limited-swatch"
                         v-if="currentPage === 'collection_page'">
                        <div class="pv-design-item-title">Limited swatch display</div>
                        <div class="pv-grid-2-column">
                            <div class="flex-column-gap8">
                                <div class="pv-design-item-value-name">Limited image</div>
                                <div class="pv-grid-2-column pv-center-align">
                                    <RadioGroup v-model:value="design_setting.limited_image" name="radioGroup"
                                                class="pv-flex-row" style="gap: 24px">
                                        <Radio value="no_image">No image</Radio>
                                        <Radio value="custom">Custom</Radio>
                                    </RadioGroup>
                                    <div class="pv-upload-image-limited-swatch"
                                         style="min-width: 220px"
                                         :class="!('imgData' in temp_data) && !design_setting.upload_image &&  !isNotLimitedImage ? 'pv-input-error' : ''"
                                         :style="[inputFileStyle]">

                                        <input @change="handleFileChange($event)" type="file"
                                               style="display: none"
                                               id="uploadFileSwatchId"
                                               accept="image/*">
                                        <label
                                            :style="[inputFileStyle]"
                                            :for="isNotLimitedImage ? '':'uploadFileSwatchId'"
                                            style="overflow: hidden" class="pv-label-limited-swatch"
                                            v-if="'imgData' in temp_data">
                                            <img :src="temp_data.imgData" alt="">
                                            <div class="pv-img-name">{{ temp_data.imgName }}</div>
                                            <DeleteOutlined class="pv-delete-img" @click="deleteImage()"/>
                                        </label>
                                        <label
                                            :style="[inputFileStyle]"
                                            :for="isNotLimitedImage ? '':'uploadFileSwatchId'"
                                            style="overflow: hidden"
                                            class="pv-center-align pv-label-limited-swatch"
                                            v-else-if="design_setting.upload_image && !('imgData' in temp_data)">
                                            <img :src="design_setting.upload_image" alt="">
                                            <div class="pv-img-name">
                                                {{
                                                    design_setting.upload_image.split('/')[design_setting.upload_image.split('/').length - 1]
                                                }}
                                            </div>
                                            <DeleteOutlined class="pv-delete-img" @click="deleteImage()"/>
                                        </label>
                                        <label :style="[inputFileStyle]"
                                               v-else-if="!( 'imgData' in temp_data) && !design_setting.upload_image"
                                               :for="isNotLimitedImage ? '':'uploadFileSwatchId'"
                                               class="pv-label-limited-swatch">
                                            <svg width="19" height="18" viewBox="0 0 19 18" fill="none"
                                                 xmlns="http://www.w3.org/2000/svg">
                                                <path
                                                    d="M16.0835 11.25V12.15C16.0835 13.4101 16.0835 14.0402 15.8383 14.5215C15.6225 14.9448 15.2783 15.289 14.855 15.5048C14.3737 15.75 13.7436 15.75 12.4835 15.75H6.1835C4.92338 15.75 4.29332 15.75 3.81202 15.5048C3.38865 15.289 3.04445 14.9448 2.82873 14.5215C2.5835 14.0402 2.5835 13.4101 2.5835 12.15V11.25M13.0835 6L9.3335 2.25M9.3335 2.25L5.5835 6M9.3335 2.25V11.25"
                                                    stroke="#3A3A3C" stroke-width="1.8" stroke-linecap="round"
                                                    stroke-linejoin="round"/>
                                            </svg>
                                            Click to upload image
                                        </label>

                                        <!--                                        <div v-if="'imgData' in temp_data || design_setting.upload_image"-->
                                        <!--                                             :style="[inputFileStyle]"-->
                                        <!--                                             class="pv-upload-block">-->
                                        <!--                                            <label-->
                                        <!--                                                :for="isNotLimitedImage ? '':'uploadFileSwatchId'"-->
                                        <!--                                                style="overflow: hidden" class="btn-upload-file-swatch pv-input-mini"-->
                                        <!--                                                v-if="'imgData' in temp_data">-->
                                        <!--                                                <img :src="temp_data.imgData" alt="">-->
                                        <!--                                                <div class="pv-img-name">{{ temp_data.imgName }}</div>-->
                                        <!--                                            </label>-->
                                        <!--                                            <label-->
                                        <!--                                                :for="isNotLimitedImage ? '':'uploadFileSwatchId'"-->
                                        <!--                                                style="overflow: hidden"-->
                                        <!--                                                class="btn-upload-file-swatch pv-input-mini"-->
                                        <!--                                                v-else-if="design_setting.upload_image && !('imgData' in temp_data)">-->
                                        <!--                                                <img :src="design_setting.upload_image" alt="">-->
                                        <!--                                                <div class="pv-img-name">-->
                                        <!--                                                    {{-->
                                        <!--                                                        temp_data.upload_image.split('/')[temp_data.upload_image.split('/').length - 1]-->
                                        <!--                                                    }}-->
                                        <!--                                                </div>-->
                                        <!--                                            </label>-->
                                        <!--                                            <DeleteOutlined class="pv-delete-img" @click="deleteImage()"/>-->
                                        <!--                                        </div>-->
                                        <!--                                        <label :style="[inputFileStyle]" v-else-if="!('imgData' in temp_data)"-->
                                        <!--                                               :for="isNotLimitedImage ? '':'uploadFileSwatchId'"-->
                                        <!--                                               class="pv-center-align">-->
                                        <!--                                            <svg width="19" height="18" viewBox="0 0 19 18" fill="none"-->
                                        <!--                                                 xmlns="http://www.w3.org/2000/svg">-->
                                        <!--                                                <path-->
                                        <!--                                                    d="M16.0835 11.25V12.15C16.0835 13.4101 16.0835 14.0402 15.8383 14.5215C15.6225 14.9448 15.2783 15.289 14.855 15.5048C14.3737 15.75 13.7436 15.75 12.4835 15.75H6.1835C4.92338 15.75 4.29332 15.75 3.81202 15.5048C3.38865 15.289 3.04445 14.9448 2.82873 14.5215C2.5835 14.0402 2.5835 13.4101 2.5835 12.15V11.25M13.0835 6L9.3335 2.25M9.3335 2.25L5.5835 6M9.3335 2.25V11.25"-->
                                        <!--                                                    stroke="#3A3A3C" stroke-width="1.8" stroke-linecap="round"-->
                                        <!--                                                    stroke-linejoin="round"/>-->
                                        <!--                                            </svg>-->
                                        <!--                                            Click to upload image-->
                                        <!--                                        </label>-->
                                    </div>
                                </div>
                            </div>
                            <div class="flex-column-gap8">
                                <div class="pv-design-item-value-name">Maximum number of variations</div>
                                <div>
                                    <InputNumber v-model:value="design_setting.maximum_number_of_variations"
                                                 min="1" max="8"
                                                 class="pv-design-item-input-number"/>
                                </div>
                            </div>
                        </div>
                        <div class="pv-flex-row" style="gap: 8px">
                            <Switch v-model:checked="design_setting.image_overlay"/>
                            <div>Image with overlay</div>
                        </div>
                    </div>
                    <div class="pv-flex-column pv-design-item-block">
                        <div class="pv-design-item-title">Label settings</div>
                        <div class="pv-grid-2-column">
                            <div class="flex-column-gap8" style="flex: 4">
                                <div class="pv-design-item-value-name">Size</div>
                                <InputNumber v-model:value="design_setting.label_size" min="1" max="30"

                                             :formatter="value => `${value}px`" class="pv-design-item-input-number"
                                             :parser="value => value.replace('px', '')"/>
                            </div>
                            <div class="flex-column-gap8" style="flex: 6">
                                <div class="pv-design-item-value-name">Case</div>

                                <!--                                    <RadioGroup v-model:value="design_setting.label_case" name="radioGroup"-->
                                <!--                                                class="pv-design-item-radio-group">-->
                                <!--                                        <Radio value="default">Default</Radio>-->
                                <!--                                        <Radio value="uppercase">Uppercase</Radio>-->
                                <!--                                        <Radio value="lowercase">Lowercase</Radio>-->
                                <!--                                    </RadioGroup>-->
                                <Select v-model:value="design_setting.label_case" name="radioGroup"
                                        class="pv-select-variant-option">
                                    <SelectOption value="default">Default
                                    </SelectOption>
                                    <SelectOption value="uppercase">Uppercase
                                    </SelectOption>
                                    <SelectOption value="lowercase">Lowercase
                                    </SelectOption>
                                </Select>

                            </div>
                        </div>
                        <Checkbox v-model:checked="design_setting.label_show" style="width: max-content">
                            Show selected option name with label
                        </Checkbox>
                    </div>
                    <div class="pv-flex-column pv-design-item-block">
                        <div class="pv-design-item-title">Image settings</div>
                        <div class="pv-grid-2-column" v-if="currentPage === 'collection_page'">
                            <div class="flex-column-gap8">
                                <div class="pv-design-item-value-name">Display position</div>
                                <div style="margin-top: 7px">
                                    <RadioGroup v-model:value="design_setting.collection_position" name="radioGroup"
                                                style="">
                                        <Radio value="left" style="margin-right: 24px">Left</Radio>
                                        <Radio value="center" style="margin-right: 24px">Center</Radio>
                                        <Radio value="right" style="margin-right: 24px">Right</Radio>
                                    </RadioGroup>
                                </div>
                            </div>
                        </div>
                        <div class="pv-grid-2-column">
                            <div class="flex-column-gap8">
                                <div class="pv-design-item-value-name">Image align</div>
                                <div style="margin-top: 7px">
                                    <RadioGroup v-model:value="design_setting.img_position" name="radioGroup"
                                                style="">
                                        <Radio value="top" style="margin-right: 24px">Top</Radio>
                                        <Radio value="center" style="margin-right: 24px">Center</Radio>
                                        <Radio value="bottom" style="margin-right: 24px">Bottom</Radio>
                                    </RadioGroup>
                                </div>
                            </div>


                            <div class="flex-column-gap8" id="pv-image-size-fit">
                                <div class="pv-design-item-value-name"
                                     style="white-space: nowrap; align-items: center; display: flex">
                                    Image size fit
                                </div>
                                <Select v-model:value="design_setting.img_fit" class="pv-select-variant-option"
                                        style="height: 40px">
                                    <SelectOption value="cover">Cover (Zoom in to fill the swatch)</SelectOption>
                                    <SelectOption value="contain">Container (Zoom out to fill the swatch)</SelectOption>
                                </Select>
                            </div>
                        </div>

                        <div class="pv-grid-2-column">
                            <div class="flex-column-gap8">
                                <div class="pv-design-item-value-name">Background swatch color</div>
                                <div class="option-block">
                                    <div class="wrap-input-color">
                                        <input v-model="design_setting.background_swatch_color"
                                               style="width: 60px !important"
                                               class="pv-input-large pv-input-color" type="color">
                                    </div>
                                    <input v-model="design_setting.background_swatch_color" style="height: 38px"
                                           class="pv-input-mini pv-input-bundle-name" type="text" disabled>
                                </div>
                            </div>

                            <div class="pv-display-flex-1-gap-16">
                                <div class="flex-column-gap8" style="flex: 1">
                                    <div class="pv-design-item-value-name" style="display: flex">Height
                                        <div
                                            v-if="designItemName === 'Swatch Circle in Square' || designItemName === 'Circular Swatch'">
                                            , width size

                                        </div>

                                    </div>
                                    <InputNumber v-model:value="design_setting.img_height" min="10" max="150"
                                                 :formatter="value => `${value}px`"
                                                 class="pv-design-item-input-number pv-style-settings"
                                                 :parser="value => value.replace('px', '')"/>
                                </div>
                                <div class="flex-column-gap8" style="flex: 1"
                                     v-if="designItemName !== 'Swatch Circle in Square' && designItemName !== 'Circular Swatch'">
                                    <div class="pv-design-item-value-name">Width</div>
                                    <InputNumber v-model:value="design_setting.img_width"
                                                 :formatter="value => `${value}px`"
                                                 class="pv-design-item-input-number pv-style-settings" min="10"
                                                 max="150" :parser="value => value.replace('px', '')"/>
                                </div>
                            </div>
                        </div>
                        <div class="pv-flex-row" style="gap: 8px" v-if="designItemName === 'Swatch in Box' || designItemName === 'Swatch in Dropdown'">
                            <Switch v-model:checked="design_setting.show_price"/>
                            <div>Show price</div>
                        </div>
                    </div>
                    <div class="pv-flex-column pv-design-item-block">
                        <div class="pv-design-item-title">Spacing settings</div>
                        <div class="pv-grid-2-column">
                            <div class="flex-column-gap8" style="flex: 1"
                                 v-if="designItemName !== 'Swatch in Dropdown'">
                                <div class="pv-design-item-value-name">Swatch Spacing</div>
                                <InputNumber v-model:value="design_setting.swatch_spacing"
                                             :formatter="value => `${value}px`"
                                             class="pv-design-item-input-number pv-style-settings" min="0" max="20"
                                             :parser="value => value.replace('px', '')"/>
                            </div>
                            <div class="flex-column-gap8" style="flex: 1">
                                <div class="pv-design-item-value-name">Border Spacing</div>
                                <InputNumber v-model:value="design_setting.border_spacing" min="0" max="30"
                                             :formatter="value => `${value}px`"

                                             class="pv-design-item-input-number pv-style-settings"
                                             :parser="value => value.replace('px', '')"/>
                            </div>
                        </div>
                    </div>
                    <div class="pv-flex-column pv-design-item-block" v-if="designItemName === 'Swatch in Dropdown'">
                        <div class="pv-design-item-title">Border</div>
                        <div class="pv-flex-column-24">
                            <div class="pv-grid-2-column">
                                <div class="pv-flex-column" style="width: 100%">
                                    <div class="flex-column-gap8" style="width: 100%">
                                        <div class="pv-design-item-value-name">Outer Border</div>
                                        <div class="option-block">
                                            <div class="wrap-input-color">
                                                <input v-model="design_setting.dropdown_outer_border"
                                                       style="width: 60px !important"
                                                       class="pv-input-large pv-input-color" type="color">
                                            </div>
                                            <input v-model="design_setting.dropdown_outer_border" style="height: 38px"
                                                   class="pv-input-mini pv-input-bundle-name" type="text" disabled>
                                        </div>
                                    </div>
                                </div>
                                <div class="pv-display-flex-1-gap-16">
                                    <div class="flex-column-gap8">
                                        <div class="pv-design-item-value-name">Thickness</div>
                                        <div>
                                            <InputNumber v-model:value="design_setting.dropdown_outer_border_thickness"
                                                         min="0" max="10"
                                                         class="pv-design-item-input-number"
                                                         :formatter="value => `${value}px`"
                                                         :parser="value => value.replace('px', '')"/>
                                        </div>
                                    </div>
                                    <div class="flex-column-gap8">
                                        <div class="pv-design-item-value-name">Radius</div>
                                        <div>
                                            <InputNumber v-model:value="design_setting.dropdown_outer_border_radius"
                                                         :max="Math.max(design_setting.img_height, design_setting.img_width)"
                                                         min="0"
                                                         class="pv-design-item-input-number"
                                                         :formatter="value => `${value}px`"
                                                         :parser="value => value.replace('px', '')"/>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="pv-grid-2-column">
                                <div class="pv-flex-column" style="width: 100%">
                                    <div class="flex-column-gap8" style="width: 100%">
                                        <div class="pv-design-item-value-name">Inner Border</div>
                                        <div class="option-block">
                                            <div class="wrap-input-color">
                                                <input v-model="design_setting.dropdown_inner_border"
                                                       style="width: 60px !important"
                                                       class="pv-input-large pv-input-color" type="color">
                                            </div>
                                            <input v-model="design_setting.dropdown_inner_border" style="height: 38px"
                                                   class="pv-input-mini pv-input-bundle-name" type="text" disabled>
                                        </div>
                                    </div>
                                </div>
                                <div class="pv-display-flex-1-gap-16">
                                    <div class="flex-column-gap8">
                                        <div class="pv-design-item-value-name">Thickness</div>
                                        <div>
                                            <InputNumber v-model:value="design_setting.dropdown_inner_border_thickness"
                                                         min="0" max="5"
                                                         class="pv-design-item-input-number"
                                                         :formatter="value => `${value}px`"
                                                         :parser="value => value.replace('px', '')"/>
                                        </div>
                                    </div>
                                    <div class="flex-column-gap8">
                                        <div class="pv-design-item-value-name">Radius</div>
                                        <div>
                                            <InputNumber v-model:value="design_setting.dropdown_inner_border_radius"
                                                         min="0"
                                                         :max="Math.max(design_setting.img_height, design_setting.img_width)"
                                                         class="pv-design-item-input-number"
                                                         :formatter="value => `${value}px`"
                                                         :parser="value => value.replace('px', '')"/>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="pv-flex-column pv-design-item-block" v-if="designItemName !== 'Swatch in Dropdown'">
                        <div class="pv-design-item-title">Selected Swatch</div>
                        <div class="pv-flex-column-24">
                            <div class="pv-grid-2-column">
                                <div class="pv-flex-column" style="width: 100%">
                                    <div class="flex-column-gap8" style="width: 100%">
                                        <div class="pv-design-item-value-name">Outer Border</div>
                                        <div class="option-block">
                                            <div class="wrap-input-color">
                                                <input v-model="design_setting.selected_outer_border"
                                                       style="width: 60px !important"
                                                       class="pv-input-large pv-input-color" type="color">
                                            </div>
                                            <input v-model="design_setting.selected_outer_border" style="height: 38px"
                                                   class="pv-input-mini pv-input-bundle-name" type="text" disabled>
                                        </div>
                                    </div>
                                </div>
                                <div :class="designItemName !== 'Circular Swatch' ? 'pv-display-flex-1-gap-16':''">
                                    <div class="flex-column-gap8">
                                        <div class="pv-design-item-value-name">Thickness</div>
                                        <div>
                                            <InputNumber v-model:value="design_setting.selected_outer_border_thickness"
                                                         min="0" max="10"

                                                         class="pv-design-item-input-number"
                                                         :formatter="value => `${value}px`"
                                                         :parser="value => value.replace('px', '')"/>
                                        </div>
                                    </div>
                                    <div class="flex-column-gap8" v-if="designItemName !== 'Circular Swatch'">
                                        <div class="pv-design-item-value-name">Radius</div>
                                        <div>
                                            <InputNumber v-model:value="design_setting.selected_outer_border_radius"
                                                         :max="Math.max(design_setting.img_height, design_setting.img_width)"
                                                         min="0"
                                                         class="pv-design-item-input-number"
                                                         :formatter="value => `${value}px`"
                                                         :parser="value => value.replace('px', '')"/>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="pv-grid-2-column">
                                <div class="pv-flex-column" style="width: 100%">
                                    <div class="flex-column-gap8" style="width: 100%">
                                        <div class="pv-design-item-value-name">Inner Border</div>
                                        <div class="option-block">
                                            <div class="wrap-input-color">
                                                <input v-model="design_setting.selected_inner_border"
                                                       style="width: 60px !important"
                                                       class="pv-input-large pv-input-color" type="color">
                                            </div>
                                            <input v-model="design_setting.selected_inner_border" style="height: 38px"
                                                   class="pv-input-mini pv-input-bundle-name" type="text" disabled>
                                        </div>
                                    </div>
                                </div>
                                <div
                                    :class="designItemName === 'Swatch in Dropdown' || designItemName === 'Swatch in Pill' || designItemName === 'Square Swatch' || designItemName === 'Swatch in Box' ? 'pv-display-flex-1-gap-16':''">
                                    <div class="flex-column-gap8">
                                        <div class="pv-design-item-value-name">Thickness</div>
                                        <div>
                                            <InputNumber v-model:value="design_setting.selected_inner_border_thickness"
                                                         min="0" max="5"
                                                         class="pv-design-item-input-number"
                                                         :formatter="value => `${value}px`"
                                                         :parser="value => value.replace('px', '')"/>
                                        </div>
                                    </div>
                                    <div class="flex-column-gap8"
                                         v-if="designItemName === 'Swatch in Dropdown' || designItemName === 'Swatch in Pill' || designItemName === 'Square Swatch' || designItemName === 'Swatch in Box'">
                                        <div class="pv-design-item-value-name">Radius</div>
                                        <div>
                                            <InputNumber v-model:value="design_setting.selected_inner_border_radius"
                                                         :max="Math.max(design_setting.img_height, design_setting.img_width)"
                                                         class="pv-design-item-input-number" min="0"
                                                         :formatter="value => `${value}px`"
                                                         :parser="value => value.replace('px', '')"/>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="pv-flex-column pv-design-item-block" v-if="designItemName !== 'Swatch in Dropdown'">
                        <div class="pv-design-item-title">Unselected Swatch</div>
                        <div class="pv-flex-column-24">
                            <div class="pv-grid-2-column">
                                <div class="pv-flex-column" style="width: 100%">
                                    <div class="flex-column-gap8" style="width: 100%">
                                        <div class="pv-design-item-value-name">Outer Border</div>
                                        <div class="option-block">
                                            <div class="wrap-input-color">
                                                <input v-model="design_setting.unselected_outer_border"
                                                       style="width: 60px !important"
                                                       class="pv-input-large pv-input-color" type="color">
                                            </div>
                                            <input v-model="design_setting.unselected_outer_border" style="height: 38px"
                                                   class="pv-input-mini pv-input-bundle-name" type="text" disabled>
                                        </div>
                                    </div>
                                </div>
                                <div :class="designItemName !== 'Circular Swatch' ? 'pv-display-flex-1-gap-16':''">
                                    <div class="flex-column-gap8">
                                        <div class="pv-design-item-value-name">Thickness</div>
                                        <div>
                                            <InputNumber
                                                v-model:value="design_setting.unselected_outer_border_thickness"
                                                min="0" max="10"
                                                class="pv-design-item-input-number"
                                                :formatter="value => `${value}px`"
                                                :parser="value => value.replace('px', '')"/>
                                        </div>
                                    </div>
                                    <div class="flex-column-gap8" v-if="designItemName !== 'Circular Swatch'">
                                        <div class="pv-design-item-value-name">Radius</div>
                                        <div>
                                            <InputNumber v-model:value="design_setting.unselected_outer_border_radius"
                                                         min="0"
                                                         :max="Math.max(design_setting.img_height, design_setting.img_width)"
                                                         class="pv-design-item-input-number"
                                                         :formatter="value => `${value}px`"
                                                         :parser="value => value.replace('px', '')"/>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="pv-grid-2-column">
                                <div class="pv-flex-column" style="width: 100%">
                                    <div class="flex-column-gap8" style="width: 100%">
                                        <div class="pv-design-item-value-name">Inner Border</div>
                                        <div class="option-block">
                                            <div class="wrap-input-color">
                                                <input v-model="design_setting.unselected_inner_border"
                                                       style="width: 60px !important"
                                                       class="pv-input-large pv-input-color" type="color">
                                            </div>
                                            <input v-model="design_setting.unselected_inner_border" style="height: 38px"
                                                   type="text" disabled class="pv-input-mini pv-input-bundle-name">
                                        </div>
                                    </div>
                                </div>
                                <div
                                    :class="designItemName === 'Swatch in Dropdown' || designItemName === 'Swatch in Pill' || designItemName === 'Square Swatch' || designItemName === 'Swatch in Box' ? 'pv-display-flex-1-gap-16':''">
                                    <div class="flex-column-gap8">
                                        <div class="pv-design-item-value-name">Thickness</div>
                                        <div>
                                            <InputNumber
                                                v-model:value="design_setting.unselected_inner_border_thickness"
                                                class="pv-design-item-input-number" min="0" max="5"
                                                :formatter="value => `${value}px`"
                                                :parser="value => value.replace('px', '')"/>
                                        </div>
                                    </div>
                                    <div class="flex-column-gap8"
                                         v-if="designItemName === 'Swatch in Dropdown' || designItemName === 'Swatch in Pill' || designItemName === 'Square Swatch' || designItemName === 'Swatch in Box'">
                                        <div class="pv-design-item-value-name">Radius</div>
                                        <div>
                                            <InputNumber v-model:value="design_setting.unselected_inner_border_radius"
                                                         class="pv-design-item-input-number" min="0"
                                                         :max="Math.max(design_setting.img_height, design_setting.img_width)"
                                                         :formatter="value => `${value}px`"
                                                         :parser="value => value.replace('px', '')"/>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>


                    <div class="pv-flex-column pv-design-item-block" v-if="designItemName !== 'Swatch in Dropdown'">
                        <div class="pv-design-item-title">Hover swatch</div>
                        <div class="pv-flex-column-24">
                            <div class="pv-flex-row" style="gap: 8px">
                                <Switch v-model:checked="design_setting.hover_show_variant_description"/>
                                <div>Show variant description</div>
                            </div>
                            <div class="pv-flex-column" style="gap: 16px">
                                <div class="pv-flex-row" style="gap: 8px">
                                    <Switch v-model:checked="design_setting.hover_show_shadow"/>
                                    <div>Show shadow</div>
                                </div>

                                <div class="pv-grid-2-column">

                                    <div class="pv-flex-column" style="width: 100%">
                                        <div class="flex-column-gap8" style="width: 100%">
                                            <div class="pv-design-item-value-name">Shadow</div>
                                            <div class="option-block"
                                                 :style="!design_setting.hover_show_shadow ? {cursor: 'not-allowed',background:'#f5f5f5 !important'}:{}">
                                                <div class="wrap-input-color">
                                                    <input v-model="design_setting.hover_shadow"
                                                           :style="!design_setting.hover_show_shadow ? {cursor: 'not-allowed',background:'#f5f5f5 !important'}:{}"
                                                           style="width: 60px !important"
                                                           :disabled="!design_setting.hover_show_shadow"
                                                           class="pv-input-large pv-input-color" type="color">
                                                </div>
                                                <input v-model="design_setting.hover_shadow" style="height: 38px"
                                                       :style="!design_setting.hover_show_shadow ? {cursor: 'not-allowed',background:'#f5f5f5 !important'}:{}"
                                                       class="pv-input-mini pv-input-bundle-name" type="text" disabled>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="pv-display-flex-1-gap-16">
                                        <div class="flex-column-gap8">
                                            <div class="pv-design-item-value-name">Thickness</div>
                                            <div>
                                                <InputNumber v-model:value="design_setting.hover_shadow_thickness"
                                                             min="0" max="10"
                                                             style="width: 100% !important;"
                                                             :disabled="!design_setting.hover_show_shadow"
                                                             class="pv-design-item-input-number"
                                                             :formatter="value => `${value}px`"
                                                             :parser="value => value.replace('px', '')"/>
                                            </div>
                                        </div>
                                        <div class="flex-column-gap8">
                                            <div class="pv-design-item-value-name">Blur</div>
                                            <div>
                                                <InputNumber v-model:value="design_setting.hover_shadow_blur"
                                                             :max="Math.max(design_setting.img_height, design_setting.img_width)"
                                                             min="0"
                                                             style="width: 100% !important;"
                                                             :disabled="!design_setting.hover_show_shadow"
                                                             class="pv-design-item-input-number"
                                                             :formatter="value => `${value}px`"
                                                             :parser="value => value.replace('px', '')"/>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="pv-flex-column" style="gap: 16px">
                                <div class="pv-grid-2-column">
                                    <div class="pv-flex-row" style="gap: 8px" v-if="currentPage === 'design'">
                                        <Switch v-model:checked="design_setting.hover_show_tooltip"/>
                                        <div>Show tooltip with variant image</div>
                                    </div>
                                    <div class="pv-flex-row" style="gap: 8px">
                                        <Switch v-model:checked="design_setting.hover_zoom_variant_image"/>
                                        <div>Zoom variant image</div>
                                    </div>
                                </div>
                                <div>
                                    <div class="pv-grid-2-column">
                                        <div class="flex-column-gap8" v-if="currentPage ==='design'">
                                            <div class="pv-design-item-value-name">Scaling size</div>
                                            <div>
                                                <Select v-model:value="design_setting.hover_scaling_size"
                                                        class="pv-select-variant-option"
                                                        :disabled="!design_setting.hover_show_tooltip"
                                                        style="height: 40px">
                                                    <SelectOption value="300">300%
                                                    </SelectOption>
                                                    <SelectOption value="400">400%
                                                    </SelectOption>
                                                    <SelectOption value="500">500%
                                                    </SelectOption>
                                                    <SelectOption value="750">750%
                                                    </SelectOption>
                                                    <SelectOption value="1000">1000%
                                                    </SelectOption>

                                                </Select>
                                            </div>
                                        </div>
                                        <div class="flex-column-gap8">
                                            <div class="pv-design-item-value-name">Zoom size</div>
                                            <div>
                                                <Select v-model:value="design_setting.hover_zoom_size"
                                                        class="pv-select-variant-option" style="height: 40px"
                                                        :disabled="!design_setting.hover_zoom_variant_image">
                                                    <SelectOption value="0.8">0.8
                                                    </SelectOption>
                                                    <SelectOption value="1.2">1.2
                                                    </SelectOption>
                                                    <SelectOption value="1.5">1.5
                                                    </SelectOption>
                                                </Select>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </Col>
                <Col :xs="{ span: 24, order: 1 }" :lg="{ span: 8, order: 2 }" style="margin-bottom: 10px">
                    <preview-design-setting style="flex: 3.5" v-if="currentPage === 'design'"
                                            :scrollPosition="scrollPosition"
                                            :design_setting="design_setting"
                                            :designItemName="designItemName"/>
                    <preview-design-setting-collection style="flex: 3.5" v-else
                                                       :temp_data="temp_data"
                                                       :scrollPosition="scrollPosition"
                                                       :design_setting="design_setting"
                                                       :designItemName="designItemName"/>
                </Col>
            </Row>
        </div>
    </div>
</template>
<script>
import axios from "axios"
import {DeleteOutlined, LeftOutlined, LoadingOutlined} from "@ant-design/icons-vue"
import PreviewDesignSetting from "./preview_design_setting.vue"
import {
    Row, Col,
    Button,
    notification,
    InputNumber,
    Select,
    SelectOption,
    RadioGroup,
    Radio,
    Checkbox, Switch, Dropdown, Menu, MenuItem, Input
} from "ant-design-vue"
import _ from 'lodash';
import PreviewDesignSettingCollection from "./preview_design_setting_collection.vue";

export default {
    name: 'DesignSettingItem',
    components: {
        DeleteOutlined,
        Input,
        PreviewDesignSettingCollection,
        Menu, MenuItem, Button, Dropdown, Row, Col,
        Switch,
        LoadingOutlined,
        SelectOption,
        Select,
        InputNumber,
        RadioGroup,
        Radio,
        Checkbox,
        LeftOutlined,
        PreviewDesignSetting
    },
    data() {
        return {

            temp_data: {},
            original_design_setting: {},
            design_setting: {},
            isLoading: false,
            collection_array_design: [],
            scrollPosition: 0,
            default_design: {},
            listDesignSettingDataCollection: [
                {
                    name: "Circular Swatch",
                    display_style: "circular_swatch",
                    img_position: "bottom",
                    img_width: 50,
                    img_height: 50,
                    swatch_spacing: 5,
                    style_height: 64,
                    style_width: 64,
                    hover_show_tooltip: false,
                    hover_zoom_variant_image: false,
                    maximum_number_of_variations: 3,
                    collection_position: "left",
                    limited_image: "no_image",
                    upload_image: "",
                    image_overlay: false,
                },
                {
                    name: "Swatch Circle in Square",
                    display_style: "swatch_circle_in_square",
                    img_position: "center",
                    img_height: 50,
                    img_width: 50,
                    border_spacing: 5,
                    style_height: 64,
                    style_width: 64,
                    hover_show_tooltip: false,
                    hover_zoom_variant_image: false,
                    maximum_number_of_variations: 3,
                    collection_position: "left",
                    limited_image: "no_image",
                    upload_image: "",
                    image_overlay: false,
                },
                {
                    display_style: "square_swatch",
                    name: "Square Swatch",
                    img_position: "center",
                    img_height: 40,
                    img_width: 40,
                    border_spacing: 5,
                    swatch_spacing: 10,
                    style_height: 54,
                    style_width: 54,
                    hover_show_tooltip: false,
                    hover_zoom_variant_image: false,
                    maximum_number_of_variations: 3,
                    collection_position: "left",
                    limited_image: "no_image",
                    upload_image: "",
                    image_overlay: false,
                }],
            listDesignSettingData: [
                {
                    name: "Swatch in Box",
                    display_style: "swatch_in_box",
                    border_spacing: 20,
                    swatch_spacing: 5,
                    img_width: 40,
                    img_height: 40,
                    style_height: 134,
                    style_width: 84
                },
                {
                    name: "Swatch in Pill",
                    img_width: 40,
                    img_height: 40,
                    display_style: "swatch_in_pill",
                    border_spacing: 5,
                    swatch_spacing: 5,
                    style_height: 54,
                    style_width: 154
                },
                {
                    name: "Circular Swatch",
                    display_style: "circular_swatch",
                    img_width: 40,
                    img_height: 40,
                    swatch_spacing: 5,
                    style_height: 54,
                    style_width: 54
                },
                {
                    name: "Swatch Circle in Square",
                    display_style: "swatch_circle_in_square",
                    img_position: "bottom",
                    img_height: 50,
                    img_width: 50,
                    border_spacing: 5,
                    style_height: 64,
                    style_width: 64
                },
                {
                    display_style: "swatch_in_dropdown",
                    name: "Swatch in Dropdown",
                    border_spacing: 5,
                    img_height: 40,
                    img_width: 40,
                    style_height: 50
                },
                {
                    display_style: "square_swatch",
                    name: "Square Swatch",
                    img_height: 40,
                    img_width: 40,
                    border_spacing: 10,
                    swatch_spacing: 10,
                    style_height: 64,
                    style_width: 64
                }
            ]
        }
    },
    props: {
        designItemName: String,
        currentPage: String
    },
    mounted() {
        this.isLoading = true
        let type = ''
        if (this.currentPage === 'collection_page') {
            type = 'collection'
        } else {
            type = 'product'
        }
        axios.post('/pv/get_design_setting/' + type, {
            jsonrpc: 2,
            params: {
                store_url: window.pv_settings.store_url,
                name: this.designItemName,
                referer: window.location.href
            }
        }).then(res => {
            if (res.data.result != 0) {
                if (type === 'collection') {
                    let collection_array = res.data.result[0]
                    this.original_design_setting = JSON.stringify(collection_array)
                    this.design_setting = collection_array

                    this.collection_array_design = res.data.result
                } else if (typeof res.data.result === 'object' && res.data.result !== null) {
                    this.original_design_setting = JSON.stringify(res.data.result)
                    this.design_setting = res.data.result

                }
                this.isLoading = false
                this.default_design = {
                    display_style: this.design_setting.display_style,
                    name: this.designItemName,
                    border_spacing: 5,
                    dropdown_inner_border: "#d1d1d1",
                    dropdown_inner_border_radius: 0,
                    dropdown_inner_border_thickness: 1,
                    dropdown_outer_border: "#dedede",
                    dropdown_outer_border_radius: 0,
                    dropdown_outer_border_thickness: 1,
                    img_fit: "cover",
                    img_height: 30,
                    img_position: "center",
                    img_width: "30",
                    label_show: true,
                    label_case: "default",
                    label_size: 14,
                    selected_inner_border: "#1890ff",
                    selected_inner_border_radius: 0,
                    selected_inner_border_thickness: 2,
                    selected_outer_border: "#a480ef",
                    selected_outer_border_radius: 0,
                    selected_outer_border_thickness: 2,
                    style_height: 40,
                    style_width: 40,
                    swatch_spacing: 5,
                    unselected_inner_border: "#dedede",
                    unselected_inner_border_radius: 0,
                    unselected_inner_border_thickness: 1,
                    unselected_outer_border: "#dedede",
                    unselected_outer_border_radius: 0,
                    unselected_outer_border_thickness: 1,
                    store_id: this.design_setting.store_id,
                    background_swatch_color: "#ffffff",
                    hover_show_variant_description: false,
                    hover_show_shadow: false,
                    hover_shadow: "#b0e3ff",
                    hover_shadow_thickness: 1,
                    hover_shadow_blur: 5,
                    hover_show_tooltip: false,
                    hover_zoom_variant_image: false,
                    hover_scaling_size: "300",
                    hover_zoom_size: "1.2",
                }
            }
        }).catch(error => {
            this.isLoading = false
            console.log(error)
        })
    },
    created() {
        document.getElementById('pv-main-container').addEventListener('scroll', this.handleScroll);
    },
    unmounted() {
        document.getElementById('pv-main-container').removeEventListener('scroll', this.handleScroll);
    },
    methods: {
        deleteImage() {
            this.temp_data = {}
            this.design_setting.upload_image = ''
        },
        handleFileChange(event) {
            let file = event.target.files[0] || event.dataTransfer.files[0];
            if (!file) return;

            if (file.size > 5242880) {
                this.show_toast('error', 'The image size must be less than 5MB');
                this.resetFileInput(event.target);
                return;
            }

            var reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onload = (e) => {
                let temp_data = {
                    imgName: file.name,
                    imgData: e.target.result
                };


                this.temp_data = JSON.parse(JSON.stringify(temp_data));


                this.resetFileInput(event.target);
            };
        },
        resetFileInput(inputElement) {
            inputElement.value = '';
        },
        handleScroll(event) {
            this.scrollPosition = event.target.scrollTop
        },
        applyDesignFromProduct() {
            let collection_array = this.collection_array_design[1]
            collection_array.maximum_number_of_variations = this.design_setting.maximum_number_of_variations
            this.design_setting = JSON.parse(JSON.stringify(collection_array))
        },
        show_toast: function (type, message, duration) {
            let background = ''
            if (type === 'success') {
                background = '#52c41a'
            } else if (type === 'error') {
                background = '#F5222D'
            } else {
                background = '#E9A317'
            }
            notification[type]({
                message: message,
                duration: duration,
                placement: 'bottomRight',
                style: {
                    backgroundColor: background,
                }
            })
        },
        backToPreviousPage() {
            this.$emit("changePage", this.currentPage, '')
        },
        saveDesignSetting() {
            let type = ''
            let params = {
                store_url: window.pv_settings.store_url,
                name: this.designItemName,
                border_spacing: this.design_setting.border_spacing,
                dropdown_inner_border: this.design_setting.dropdown_inner_border,
                dropdown_inner_border_radius: this.design_setting.dropdown_inner_border_radius,
                dropdown_inner_border_thickness: this.design_setting.dropdown_inner_border_thickness,
                dropdown_outer_border: this.design_setting.dropdown_outer_border,
                dropdown_outer_border_radius: this.design_setting.dropdown_outer_border_radius,
                dropdown_outer_border_thickness: this.design_setting.dropdown_outer_border_thickness,
                img_fit: this.design_setting.img_fit,
                img_height: this.design_setting.img_height,
                img_position: this.design_setting.img_position,
                img_width: this.design_setting.img_width,
                label_show: this.design_setting.label_show,
                label_case: this.design_setting.label_case,
                label_size: this.design_setting.label_size,
                selected_inner_border: this.design_setting.selected_inner_border,
                selected_inner_border_radius: this.design_setting.selected_inner_border_radius,
                selected_inner_border_thickness: this.design_setting.selected_inner_border_thickness,
                selected_outer_border: this.design_setting.selected_outer_border,
                selected_outer_border_radius: this.design_setting.selected_outer_border_radius,
                selected_outer_border_thickness: this.design_setting.selected_outer_border_thickness,
                style_height: this.design_setting.style_height,
                style_width: this.design_setting.style_width,
                swatch_spacing: this.design_setting.swatch_spacing,
                unselected_inner_border: this.design_setting.unselected_inner_border,
                unselected_inner_border_radius: this.design_setting.unselected_inner_border_radius,
                unselected_inner_border_thickness: this.design_setting.unselected_inner_border_thickness,
                unselected_outer_border: this.design_setting.unselected_outer_border,
                unselected_outer_border_radius: this.design_setting.unselected_outer_border_radius,
                unselected_outer_border_thickness: this.design_setting.unselected_outer_border_thickness,
                background_swatch_color: this.design_setting.background_swatch_color,
                hover_show_variant_description: this.design_setting.hover_show_variant_description,
                hover_show_shadow: this.design_setting.hover_show_shadow,
                hover_shadow: this.design_setting.hover_shadow,
                hover_shadow_thickness: this.design_setting.hover_shadow_thickness,
                hover_shadow_blur: this.design_setting.hover_shadow_blur,
                hover_show_tooltip: this.currentPage === 'design' ? this.design_setting.hover_show_tooltip : false,
                hover_zoom_variant_image: this.design_setting.hover_zoom_variant_image,
                hover_scaling_size: this.design_setting.hover_scaling_size,
                hover_zoom_size: this.design_setting.hover_zoom_size,
                show_price: this.design_setting.show_price,
                referer: window.location.href,
            }
            if (this.currentPage === 'collection_page') {
                let upload_image = ""
                if ('imgData' in this.temp_data) {
                    upload_image = JSON.parse(JSON.stringify(this.temp_data))
                    let origin_upload = JSON.parse(this.original_design_setting).upload_image
                    if (this.temp_data['imgName'] === origin_upload.split('/')[origin_upload.split('/').length - 1]) {
                        upload_image = origin_upload
                    }
                } else if (this.design_setting.upload_image !== '') {
                    upload_image = this.design_setting.upload_image
                }
                type = 'collection'
                params.collection_position = this.design_setting.collection_position
                params.maximum_number_of_variations = this.design_setting.maximum_number_of_variations;
                params.limited_image = this.design_setting.limited_image
                params.upload_image = upload_image
                params.image_overlay = this.design_setting.image_overlay
                if (this.design_setting.limited_image === 'custom') {
                    if (!('imgData' in this.temp_data) && this.design_setting.upload_image === '') {
                        this.show_toast('error', 'Field(s) must not be blank!', 2);
                        return false;
                    }
                }
            } else {
                type = 'product'
            }
            this.$emit('setLoadingData', true)
            axios.post('/pv/save_design_setting/' + type, {
                jsonrpc: 2,
                params: params
            }).then(res => {
                if ("success" in res.data.result) {
                    if (this.currentPage === 'collection_page') {
                        if (this.design_setting.limited_image === 'custom') {
                            if ('imgData' in this.temp_data) {
                                this.temp_data = {}
                                this.design_setting.upload_image = res.data.result.upload_image
                            }
                        }
                    }
                    this.original_design_setting = JSON.stringify(this.design_setting)
                    this.show_toast("success", `"${this.designItemName}" has been saved successfully.`, 2)
                } else {
                    console.log(res.data.result.error)
                    this.show_toast('error', "Something went wrong. Please contact the customer support", 2)
                }
                this.$emit('setLoadingData', false)
            }).catch(error => {
                this.show_toast('error', "Something went wrong. Please contact the customer support", 2)
                this.$emit('setLoadingData', false)
                console.log(error)
            })
        },
        cancelDesignSetting() {
            this.design_setting = JSON.parse(this.original_design_setting)
            this.temp_data = {}
        },
        resetToDefault() {
            let default_design_of_designItemName = JSON.parse(JSON.stringify(this.default_design))
            let design_from_list = {}
            if (this.currentPage === 'design') {
                for (let design of this.listDesignSettingData) {
                    if (this.designItemName === design.name) {
                        design_from_list = JSON.parse(JSON.stringify(design))
                        break
                    }
                }
            } else {
                for (let design of this.listDesignSettingDataCollection) {
                    if (this.designItemName === design.name) {
                        design_from_list = JSON.parse(JSON.stringify(design))
                        break
                    }
                }
            }
            Object.keys(design_from_list).forEach(key => {
                if (key !== 'name' && key !== 'display_style') {
                    default_design_of_designItemName[key] = design_from_list[key]
                }
            })

            // this.design_setting = JSON.parse(this.default_static_design)
            this.design_setting = JSON.parse(JSON.stringify(default_design_of_designItemName))
        },
        watch_img_height() {
            let max_pixel = Math.max(this.design_setting.selected_outer_border_thickness, this.design_setting.unselected_outer_border_thickness)
            if (this.designItemName === 'Swatch Circle in Square' || this.designItemName === "Circular Swatch") {
                this.design_setting.style_height = this.design_setting.img_height + 2 * this.design_setting.border_spacing + 2 * max_pixel
                this.design_setting.img_width = this.design_setting.img_height
            }
            if (this.designItemName === "Swatch in Box") {
                this.design_setting.style_height = this.design_setting.img_height + 2 * this.design_setting.border_spacing + 2 * max_pixel + 50
            }
            if (this.designItemName === 'Swatch in Dropdown') {
                this.design_setting.style_height = this.design_setting.img_height + this.design_setting.border_spacing * 2
            }
            if (this.designItemName === 'Square Swatch' || this.designItemName === 'Swatch in Pill') {
                this.design_setting.style_height = this.design_setting.img_height + 2 * this.design_setting.border_spacing + 2 * max_pixel
            }
        },
        watch_img_width() {
            let max_pixel = Math.max(this.design_setting.selected_outer_border_thickness, this.design_setting.unselected_outer_border_thickness)
            if (this.designItemName === 'Swatch Circle in Square' || this.designItemName === "Circular Swatch") {
                this.design_setting.style_width = this.design_setting.img_height + 2 * this.design_setting.border_spacing + 2 * max_pixel
                this.design_setting.img_width = this.design_setting.img_height
            }
            if (this.designItemName === "Swatch in Box") {
                this.design_setting.style_width = this.design_setting.img_width + 2 * this.design_setting.border_spacing + 2 * max_pixel
            }
            if (this.designItemName === 'Square Swatch') {
                this.design_setting.style_width = this.design_setting.img_width + 2 * this.design_setting.border_spacing + 2 * max_pixel
            }
            if (this.designItemName === 'Swatch in Pill') {
                this.design_setting.style_width = this.design_setting.img_width + 2 * this.design_setting.border_spacing + 2 * max_pixel + 100
            }
        }
    },
    emits: ['changePage', 'setChangeDesignSettingStatus', "setLoadingData"],
    computed: {
        design_is_change() {
            // if(Object.keys(this.original_design_setting).length > 0){
            //     console.log(_.isEqual(this.design_setting, JSON.parse(this.original_design_setting)));
            // }

            return JSON.stringify(this.design_setting) !== this.original_design_setting || Object.keys(this.temp_data).length !== 0
        },
        isNotLimitedImage() {
            return this.design_setting.limited_image === 'no_image'
        },
        inputFileStyle() {
            if (this.isNotLimitedImage) {
                return {
                    cursor: 'not-allowed',
                    background: "#F5F5F5",
                    opacity: "0.6"
                }
            }
            return {
                cursor: 'pointer',
            }
        }
    },
    watch: {
        design_is_change() {
            this.$emit("setChangeDesignSettingStatus", this.design_is_change)
        },
        'design_setting.img_height'() {
            this.watch_img_height()
        },
        'design_setting.img_width'() {
            this.watch_img_width()
        },
        'design_setting.border_spacing'() {
            this.watch_img_height()
            this.watch_img_width()
        },
        'design_setting.selected_outer_border_thickness'() {
            this.watch_img_height()
            this.watch_img_width()
        },
        'design_setting.unselected_outer_border_thickness'() {
            this.watch_img_height()
            this.watch_img_width()
        },
        "design_setting.dropdown_outer_border_thickness"() {
            this.watch_img_height()
        }
    }
}
</script>