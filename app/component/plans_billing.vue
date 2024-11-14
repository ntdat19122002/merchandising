<template>
    <div style="width: 100%">
        <div style="display: flex; margin-bottom: 32px">
            <div class="pv-flex-row pv-center-align" style="gap: 8px">
                <div class="pv-page-title">Plans & Billing</div>
            </div>
        </div>

        <div class="pv-flex-row" style="gap: 24px" v-if="!is_have_paid_plan">
            <div class="pv-block-plan pv-block-paid-plan-option" v-for="plan in list_plan">

                <div class="pv-paid-plan-block-style" style="border-bottom: 1px solid #D9D9D9;">
                    <div style="margin-bottom: 4px" class="pv-value-of-variant-option">{{ plan.name }}</div>
                    <div style="margin-bottom: 16px"><span class="pv-plan-price-text">{{
                            plan.price === 0 ? 'Free' : plan.price + "$"
                        }}</span>
                        <span class="pv-plan-month-text" v-if="plan.price > 0"> per month</span>
                    </div>
                    <div class="pv-paid-plan-button" @click="openUpgradePLan(plan)"
                         :class="plan.price > 0 ? 'pv-trial-button':'pv-current-plan-button'">
                        {{ plan.price > 0 ? 'Start 7-day trial' : 'Current plan' }}
                    </div>
                </div>

                <div class="pv-flex-column">
                    <div class="pv-paid-plan-block-style" style="gap: 8px">
                        <div v-for="feature in plan.features">
                            <div class="pv-flex-row pv-center-align" style="gap: 8px">
                                <svg
                                    v-if="feature.split('__')[0] === '1'"
                                    width="16" height="16" viewBox="0 0 16 16"
                                    fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="M7.99935 0.666626C3.95268 0.666626 0.666016 3.95329 0.666016 7.99996C0.666016 12.0466 3.95268 15.3333 7.99935 15.3333C12.046 15.3333 15.3327 12.0466 15.3327 7.99996C15.3327 3.95329 12.046 0.666626 7.99935 0.666626ZM7.99935 14C4.69268 14 1.99935 11.3066 1.99935 7.99996C1.99935 4.69329 4.69268 1.99996 7.99935 1.99996C11.306 1.99996 13.9993 4.69329 13.9993 7.99996C13.9993 11.3066 11.306 14 7.99935 14Z"
                                        fill="#1677FF"/>
                                    <path
                                        d="M10.526 5.52662L6.99935 9.05332L5.47268 7.52662C5.21268 7.26662 4.79268 7.26662 4.53268 7.52662C4.27268 7.78662 4.27268 8.20665 4.53268 8.46665L6.53268 10.4666C6.66601 10.6 6.83268 10.66 7.00601 10.66C7.17935 10.66 7.34601 10.5933 7.47935 10.4666L11.4793 6.46665C11.7393 6.20665 11.7393 5.78662 11.4793 5.52662C11.2193 5.26662 10.7993 5.26662 10.5393 5.52662H10.526Z"
                                        fill="#1677FF"/>
                                </svg>
                                <svg v-else
                                     height="16" viewBox="0 0 16 16" fill="none"
                                     xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="M5.52602 10.4733C5.78602 10.7333 6.20602 10.7333 6.46602 10.4733L7.99269 8.94659L9.51935 10.4733C9.65269 10.6066 9.81935 10.6666 9.99269 10.6666C10.166 10.6666 10.3327 10.5999 10.466 10.4733C10.726 10.2133 10.726 9.79326 10.466 9.53326L8.93935 8.00664L10.466 6.47995C10.726 6.21995 10.726 5.79993 10.466 5.53993C10.206 5.27993 9.78602 5.27993 9.52602 5.53993L7.99935 7.06662L6.47269 5.53993C6.21269 5.27993 5.79269 5.27993 5.53269 5.53993C5.27269 5.79993 5.27269 6.21995 5.53269 6.47995L7.05935 8.00664L5.53269 9.53326C5.27269 9.79326 5.27269 10.2133 5.53269 10.4733H5.52602Z"
                                        fill="#F5222D"/>
                                    <path
                                        d="M7.99935 15.3333C12.046 15.3333 15.3327 12.0466 15.3327 7.99996C15.3327 3.95329 12.046 0.666626 7.99935 0.666626C3.95268 0.666626 0.666016 3.95996 0.666016 7.99996C0.666016 12.04 3.95268 15.3333 7.99935 15.3333ZM7.99935 1.99996C11.306 1.99996 13.9993 4.69329 13.9993 7.99996C13.9993 11.3066 11.306 14 7.99935 14C4.69268 14 1.99935 11.3066 1.99935 7.99996C1.99935 4.69329 4.69268 1.99996 7.99935 1.99996Z"
                                        fill="#F5222D"/>
                                </svg>
                                <span>
                                {{ feature.split('__')[1] }}
                            </span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div v-else>
            <div class="pv-block-plan pv-design-item-component"
                 style="padding: 24px;align-items:normal !important;min-height:auto !important;">
                <div class="pv-flex-row" style="gap: 16px">
                    <Avatar
                        :style="{backgroundColor: `hsl(${generateFloat(store_info.store_id) * 360}, 100%, 40%)`}">
                        {{ store_info.store_name.toString()[0] }}
                    </Avatar>
                    <div class="pv-flex-column" style="gap: 12px">
                        <div class="pv-flex-row" style="gap: 16px">
                            <div class="pv-store-name">{{ store_info.store_name }}</div>
                            <div class="pv-button-style pb-plan-name-upgrade" style="padding: 0 8px">
                                {{
                                    current_plan.name + is_free_trial ? " (7 days trial remaining)" : ""
                                }}
                            </div>
                        </div>
                        <div class="pv-flex-column" style="gap: 4px">
                            <div class="pv-flex-row pv-center-align" style="gap: 16px">
                                <div class="pv-price-text">Billing amount:</div>
                                <div class="pv-make-sure-line">${{ current_plan.price }}</div>
                            </div>
                            <div class="pv-flex-row pv-center-align" style="gap: 16px">
                                <div class="pv-price-text">Current billing cycle:</div>
                                <div class="pv-make-sure-line">{{
                                        convert_date_time(current_plan.billing_on_start) + " - " + convert_date_time(current_plan.billing_on_end)
                                    }}
                                </div>
                            </div>
                            <div class="pv-flex-row pv-center-align" style="gap: 16px">
                                <div class="pv-price-text">Next renewal date:</div>
                                <div class="pv-make-sure-line">{{ convert_date_time(current_plan.next_billing) }}</div>
                            </div>
                            <div class="pv-flex-row pv-center-align" style="gap: 16px">
                                <div class="pv-price-text">Store URL:</div>
                                <div class="pv-flex-row" style="gap: 6px">
                                    <svg width="16" height="16" viewBox="0 0 16 16" fill="none"
                                         xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                        <rect width="16" height="16" fill="url(#pattern0_1242_7088)"/>
                                        <defs>
                                            <pattern id="pattern0_1242_7088" patternContentUnits="objectBoundingBox"
                                                     width="1" height="1">
                                                <use xlink:href="#image0_1242_7088" transform="scale(0.00540541)"/>
                                            </pattern>
                                            <image id="image0_1242_7088" width="185" height="185"
                                                   xlink:href="data:image/png;base64,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"/>
                                        </defs>
                                    </svg>

                                    <div class="pv-make-sure-line">{{
                                            store_info.store_name + " (" + store_info.store_url + ")"
                                        }}
                                    </div>

                                </div>

                            </div>
                        </div>
                    </div>
                </div>
                <div class="pv-make-sure-line">
                    <div class="pv-center-align" style="gap: 8px;cursor: pointer" @click="viewDetailPLan">
                        <div>View more</div>
                        <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M6.4721 3.52876L10.4722 7.52871C10.7326 7.78906 10.7326 8.21117 10.4722 8.47152L6.47209 12.4715C6.34194 12.6017 6.17138 12.6667 6.0008 12.6668C5.83015 12.6668 5.65948 12.6017 5.52928 12.4715C5.26893 12.2112 5.26893 11.7891 5.52928 11.5287L9.05799 8.00011L5.52929 4.47157C5.26894 4.21122 5.26894 3.78911 5.52929 3.52876C5.6595 3.39855 5.83016 3.33347 6.00081 3.3335C6.17139 3.33353 6.34196 3.39861 6.4721 3.52876Z"
                                fill="#333333"/>
                        </svg>
                    </div>

                </div>
            </div>
        </div>


        <Modal title="View detail" v-model:visible="modalViewDetailPlan" centered
               class="pv-modal pv-product-select"
               style="width: 1000px; border-radius: 6px">
            <template #footer style="display: flex">
            </template>
            <div class="pv-flex-column" style="width: 100%;gap: 8px">
                <div class="pv-upgrade-modal-container pv-paid-plan-block-style">
                    <div class="pv-flex-row" style="gap: 16px">
                        <Avatar
                            :style="{backgroundColor: `hsl(${generateFloat(store_info.store_id) * 360}, 100%, 40%)`}">
                            {{ store_info.store_name.toString()[0] }}
                        </Avatar>
                        <div class="pv-flex-column" style="gap: 12px">
                            <div class="pv-flex-row" style="gap: 16px">
                                <div class="pv-store-name">{{ store_info.store_name }}</div>
                                <div class="pv-button-style pb-plan-name-upgrade" style="padding: 0 8px">
                                    {{
                                        current_plan.name + is_free_trial ? " (7 days trial remaining)" : ""
                                    }}
                                </div>
                            </div>
                            <div class="pv-flex-column" style="gap: 4px">
                                <div class="pv-flex-row pv-center-align" style="gap: 16px">
                                    <div class="pv-price-text">Billing amount:</div>
                                    <div class="pv-make-sure-line">${{ current_plan.price }}</div>
                                </div>
                                <div class="pv-flex-row pv-center-align" style="gap: 16px">
                                    <div class="pv-price-text">Current billing cycle:</div>
                                    <div class="pv-make-sure-line">{{
                                            convert_date_time(current_plan.billing_on_start) + " - " + convert_date_time(current_plan.billing_on_end)
                                        }}
                                    </div>
                                </div>
                                <div class="pv-flex-row pv-center-align" style="gap: 16px">
                                    <div class="pv-price-text">Next renewal date:</div>
                                    <div class="pv-make-sure-line">{{
                                            convert_date_time(current_plan.next_billing)
                                        }}
                                    </div>
                                </div>
                                <div class="pv-flex-row pv-center-align" style="gap: 16px">
                                    <div class="pv-price-text">Store URL:</div>
                                    <div class="pv-flex-row" style="gap: 6px">
                                        <svg width="16" height="16" viewBox="0 0 16 16" fill="none"
                                             xmlns="http://www.w3.org/2000/svg"
                                             xmlns:xlink="http://www.w3.org/1999/xlink">
                                            <rect width="16" height="16" fill="url(#pattern0_1242_7088)"/>
                                            <defs>
                                                <pattern id="pattern0_1242_7088" patternContentUnits="objectBoundingBox"
                                                         width="1" height="1">
                                                    <use xlink:href="#image0_1242_7088" transform="scale(0.00540541)"/>
                                                </pattern>
                                                <image id="image0_1242_7088" width="185" height="185"
                                                       xlink:href="data:image/png;base64,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"/>
                                            </defs>
                                        </svg>

                                        <div class="pv-make-sure-line">{{
                                                store_info.store_name + " (" + store_info.store_url + ")"
                                            }}
                                        </div>

                                    </div>

                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="pv-flex-row" style="gap: 24px">
                    <div class="pv-upgrade-modal-container pv-half-width" v-for="plan in list_plan">
                        <div class="pv-paid-plan-block-style" style="border-bottom: 1px solid #D9D9D9;">
                            <div style="margin-bottom: 4px" class="pv-value-of-variant-option">{{
                                    plan.name
                                }}
                            </div>
                            <div style="margin-bottom: 16px"><span class="pv-plan-price-text">{{
                                    plan.price === 0 ? 'Free' : plan.price + "$"
                                }}</span>
                                <span class="pv-plan-month-text" v-if="plan.price > 0"> per month</span>
                            </div>
                            <div class="pv-paid-plan-button" @click="selectPlan(plan)"
                                 :class="plan.price !== current_plan.price ? 'pv-select-button':'pv-current-plan-button'">
                                {{ plan.price === current_plan.price ? 'Current plan' : 'Select plan' }}
                            </div>
                        </div>

                        <div class="pv-flex-column">
                            <div class="pv-paid-plan-block-style" style="gap: 8px">
                                <div v-for="feature in plan.features">
                                    <div class="pv-flex-row pv-center-align" style="gap: 8px">
                                        <svg
                                            v-if="feature.split('__')[0] === '1'"
                                            width="16" height="16" viewBox="0 0 16 16"
                                            fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path
                                                d="M7.99935 0.666626C3.95268 0.666626 0.666016 3.95329 0.666016 7.99996C0.666016 12.0466 3.95268 15.3333 7.99935 15.3333C12.046 15.3333 15.3327 12.0466 15.3327 7.99996C15.3327 3.95329 12.046 0.666626 7.99935 0.666626ZM7.99935 14C4.69268 14 1.99935 11.3066 1.99935 7.99996C1.99935 4.69329 4.69268 1.99996 7.99935 1.99996C11.306 1.99996 13.9993 4.69329 13.9993 7.99996C13.9993 11.3066 11.306 14 7.99935 14Z"
                                                fill="#1677FF"/>
                                            <path
                                                d="M10.526 5.52662L6.99935 9.05332L5.47268 7.52662C5.21268 7.26662 4.79268 7.26662 4.53268 7.52662C4.27268 7.78662 4.27268 8.20665 4.53268 8.46665L6.53268 10.4666C6.66601 10.6 6.83268 10.66 7.00601 10.66C7.17935 10.66 7.34601 10.5933 7.47935 10.4666L11.4793 6.46665C11.7393 6.20665 11.7393 5.78662 11.4793 5.52662C11.2193 5.26662 10.7993 5.26662 10.5393 5.52662H10.526Z"
                                                fill="#1677FF"/>
                                        </svg>
                                        <svg v-else
                                             width="16"
                                             height="16" viewBox="0 0 16 16" fill="none"
                                             xmlns="http://www.w3.org/2000/svg">
                                            <path
                                                d="M5.52602 10.4733C5.78602 10.7333 6.20602 10.7333 6.46602 10.4733L7.99269 8.94659L9.51935 10.4733C9.65269 10.6066 9.81935 10.6666 9.99269 10.6666C10.166 10.6666 10.3327 10.5999 10.466 10.4733C10.726 10.2133 10.726 9.79326 10.466 9.53326L8.93935 8.00664L10.466 6.47995C10.726 6.21995 10.726 5.79993 10.466 5.53993C10.206 5.27993 9.78602 5.27993 9.52602 5.53993L7.99935 7.06662L6.47269 5.53993C6.21269 5.27993 5.79269 5.27993 5.53269 5.53993C5.27269 5.79993 5.27269 6.21995 5.53269 6.47995L7.05935 8.00664L5.53269 9.53326C5.27269 9.79326 5.27269 10.2133 5.53269 10.4733H5.52602Z"
                                                fill="#F5222D"/>
                                            <path
                                                d="M7.99935 15.3333C12.046 15.3333 15.3327 12.0466 15.3327 7.99996C15.3327 3.95329 12.046 0.666626 7.99935 0.666626C3.95268 0.666626 0.666016 3.95996 0.666016 7.99996C0.666016 12.04 3.95268 15.3333 7.99935 15.3333ZM7.99935 1.99996C11.306 1.99996 13.9993 4.69329 13.9993 7.99996C13.9993 11.3066 11.306 14 7.99935 14C4.69268 14 1.99935 11.3066 1.99935 7.99996C1.99935 4.69329 4.69268 1.99996 7.99935 1.99996Z"
                                                fill="#F5222D"/>
                                        </svg>
                                        <span>
                                {{ feature.split('__')[1] }}
                            </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </Modal>


        <Modal title="Upgrade store plan" v-model:visible="modalUpgradePlan" centered
               class="pv-modal pv-product-select"
               style="width: 1000px; border-radius: 6px">
            <template #footer style="display: flex">
                <div style="width: 100%" class="pv-design-item-component">
                    <div style="color: #F5222D;cursor: pointer" @click="closeUpgradePLan">
                        Cancel
                    </div>
                    <div class="pv-flex-row" style="gap: 16px">
                        <div class="ant-btn ant-btn-primary pv-button-plan pv-back-button"
                             style="border: 1px solid #D9D9D9;color: #333">
                            Back
                        </div>
                        <div class="ant-btn ant-btn-primary pv-button-plan pv-upgrade-button"
                             @click="upgradeStorePlan"
                             style="color: #FDFDFD">
                            Upgrade
                        </div>
                    </div>
                </div>
            </template>
            <div class="pv-flex-column pv-upgrade-modal-container" style="width: 100%;gap: 8px">
                <div class="pv-paid-plan-block-style" style="border-bottom: 1px solid  #D9D9D9">
                    <div class="pv-modal-title" style="margin-bottom: 16px">Billing store</div>
                    <div class="pv-modal-upgrade-plan" style="margin-bottom: 8px">Billing store for subscriptions</div>
                    <div class="pv-upgrade-modal-container" style="padding: 12px;">
                        <div class="pv-flex-row pv-center-align" style="gap: 10px">
                            <Avatar
                                :style="{backgroundColor: `hsl(${generateFloat(store_info.store_id) * 360}, 100%, 40%)`}">
                                {{ store_info.store_name.toString()[0] }}
                            </Avatar>
                            <div class="pv-flex-column" style="gap: 4px">
                                <div class="pv-store-name">{{ store_info.store_name }}</div>
                                <div class="pv-price-text">{{ store_info.store_url }}</div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="pv-paid-plan-block-style pv-flex-column" style="gap:16px;border-bottom: 1px solid  #D9D9D9">
                    <div class="pv-modal-title" style="margin-bottom: 16px">Billing details</div>
                    <div style="width: 100%;gap: 16px" class="pv-modal-upgrade-plan pv-flex-column">
                        <div class="pv-flex-column" style="gap: 4px">
                            <div class="pv-design-item-component">
                                <div>Plan name</div>
                                <div class="pv-button-style pb-plan-name-upgrade" style="padding: 0 8px">
                                    {{ current_upgrade_plan_model.name }}
                                </div>
                            </div>
                            <div class="pv-design-item-component">
                                <div>Cost per month</div>
                                <div>${{ current_upgrade_plan_model.price }}/per month</div>
                            </div>
                        </div>
                        <div class="pv-flex-column" style="gap: 4px">
                            <div class="pv-design-item-component">
                                <div>Store name</div>
                                <div class="">
                                    {{ store_info.store_name }}
                                </div>
                            </div>
                        </div>
                        <div class="pv-flex-column" style="gap: 4px">
                            <div class="pv-design-item-component">
                                <div>Free trial period</div>
                                <div class="">
                                    7-day trial
                                </div>
                            </div>
                            <div class="pv-design-item-component">
                                <div>Free trial expiration date</div>
                                <div class="">
                                    {{ next_week_date }}
                                </div>
                            </div>
                            <div class="pv-design-item-component">
                                <div>Billing start date</div>
                                <div class="">
                                    {{ current_date }}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="pv-paid-plan-block-style pv-flex-column"
                     style="padding:18px !important;gap:16px;border-bottom: 1px solid  #D9D9D9">
                    <div class="pv-design-item-component" style="width: 100%">
                        <div>Total</div>
                        <div class="">
                            <div class="pv-modal-title">${{ current_upgrade_plan_model.price }}/per month</div>
                        </div>
                    </div>
                </div>
            </div>
        </Modal>


        <Modal v-model:visible="modalWarmDownGrade" centered

               style="width: 400px; border-radius: 6px">
            <template #footer>
                <div class="pv-justify-center pv-flex-row" style="gap: 16px">
                    <div class="ant-btn ant-btn-primary pv-button-plan pv-back-button"
                         @click="()=>{modalViewDetailPlan = true;modalWarmDownGrade= false }"
                         style="border: 1px solid #D9D9D9;color: #333">
                        Cancel
                    </div>
                    <div class="ant-btn ant-btn-primary pv-button-plan pv-downgrade-button"
                         @click="confirmDowngrade"
                         style="color: #FDFDFD">
                        Confirm
                    </div>
                </div>
            </template>
            <div class="pv-center-align pv-flex-column" style="gap: 16px">
                <svg width="56" height="56" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M47.18 51.2875H8.79667C7.02713 51.5568 5.21794 51.2457 3.64 50.4008C3.11214 50.0154 2.67113 49.5233 2.34555 48.9566C2.01996 48.3898 1.81707 47.761 1.75 47.1108C1.58667 45.5941 2.28667 44.3808 3.54667 42.1875L22.75 9.0308C24.71 5.62414 25.6667 5.20414 26.11 5.01747C26.7052 4.75382 27.349 4.61761 28 4.61761C28.651 4.61761 29.2948 4.75382 29.89 5.01747C31.2667 5.62414 31.9667 6.83747 33.25 9.00747L52.43 42.1875C53.7133 44.3808 54.4133 45.5941 54.25 47.1108C54.1829 47.761 53.98 48.3898 53.6545 48.9566C53.3289 49.5233 52.8879 50.0154 52.36 50.4008C50.7742 51.2476 48.9571 51.5586 47.18 51.2875ZM6.46333 46.6208H49.5367L28 9.4508L6.46333 46.6208ZM28 43.1208C27.3812 43.1208 26.7877 42.875 26.3501 42.4374C25.9125 41.9998 25.6667 41.4063 25.6667 40.7875C25.6667 40.1686 25.9125 39.5751 26.3501 39.1376C26.7877 38.7 27.3812 38.4541 28 38.4541C28.6188 38.4541 29.2123 38.7 29.6499 39.1376C30.0875 39.5751 30.3333 40.1686 30.3333 40.7875C30.3333 41.4063 30.0875 41.9998 29.6499 42.4374C29.2123 42.875 28.6188 43.1208 28 43.1208ZM28 33.7875C27.3812 33.7875 26.7877 33.5416 26.3501 33.1041C25.9125 32.6665 25.6667 32.073 25.6667 31.4541V22.1208C25.6667 21.502 25.9125 20.9085 26.3501 20.4709C26.7877 20.0333 27.3812 19.7875 28 19.7875C28.6188 19.7875 29.2123 20.0333 29.6499 20.4709C30.0875 20.9085 30.3333 21.502 30.3333 22.1208V31.4541C30.3333 32.073 30.0875 32.6665 29.6499 33.1041C29.2123 33.5416 28.6188 33.7875 28 33.7875Z"
                        fill="#E9A317"/>
                </svg>
                <div class="pv-center-align pv-flex-column">
                    <div class="pv-modal-title" style="margin-bottom: 4px">Downgrade to Free</div>
                    <div class="pv-modal-upgrade-plan" style="text-align: center">You will lose access to Growth
                        features.
                        Billing store will remain unchanged for future subscriptions.
                    </div>
                </div>
            </div>
        </Modal>
        <Modal v-model:visible="modalSuccessDownGrade" centered

               style="width: 400px; border-radius: 6px">
            <template #footer>
                <div class="pv-justify-center pv-flex-row" style="gap: 16px">
                    <div class="ant-btn ant-btn-primary pv-button-plan pv-back-button"
                         @click="()=>{modalSuccessDownGrade = false }"
                         style="border: 1px solid #D9D9D9;color: #333">
                        Cancel
                    </div>
                </div>
            </template>
            <div class="pv-center-align pv-flex-column" style="gap: 16px">
                <svg width="56" height="56" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M27.9987 2.33333C13.8354 2.33333 2.33203 13.8367 2.33203 28C2.33203 42.1633 13.8354 53.6667 27.9987 53.6667C42.162 53.6667 53.6654 42.1633 53.6654 28C53.6654 13.8367 42.162 2.33333 27.9987 2.33333ZM27.9987 49C16.4254 49 6.9987 39.5733 6.9987 28C6.9987 16.4267 16.4254 7 27.9987 7C39.572 7 48.9987 16.4267 48.9987 28C48.9987 39.5733 39.572 49 27.9987 49Z"
                        fill="#51C01A"/>
                    <path
                        d="M36.842 19.3433L24.4987 31.6867L19.1554 26.3433C18.2454 25.4333 16.7754 25.4333 15.8654 26.3433C14.9554 27.2533 14.9554 28.7234 15.8654 29.6334L22.8654 36.6334C23.332 37.1001 23.9154 37.31 24.522 37.31C25.1287 37.31 25.712 37.0767 26.1787 36.6334L40.1787 22.6334C41.0887 21.7234 41.0887 20.2533 40.1787 19.3433C39.2687 18.4333 37.7987 18.4333 36.8887 19.3433H36.842Z"
                        fill="#51C01A"/>
                </svg>

                <div class="pv-center-align pv-flex-column">
                    <div class="pv-modal-title" style="margin-bottom: 4px">Downgrade successfully</div>
                    <div class="pv-modal-upgrade-plan" style="text-align: center">You can change your subscription plan
                        anytime.
                    </div>
                </div>
            </div>
        </Modal>
    </div>
</template>
<script>


import {Modal, Select, SelectOption, Avatar, notification} from "ant-design-vue";
import {DownOutlined} from "@ant-design/icons-vue";
import axios from "axios";

export default {
    name: "PlansBilling",
    components: {Select, DownOutlined, Modal, SelectOption, Avatar},
    data() {
        return {
            list_plan: [],
            list_feature: [],
            modalUpgradePlan: false,
            modalViewDetailPlan: false,
            modalWarmDownGrade: false,
            modalSuccessDownGrade: false,
            store_info: {},
            current_plan: {},
            current_upgrade_plan_model: {},
            current_date: null,
            next_week_date: null,
            is_have_paid_plan: false,
            is_free_trial: false,
            tempConfirmDownGrade: {},
            isLoadingData: false
        }
    },
    async mounted() {
        if ("pv_settings" in window) {
            this.store_info = {
                store_id: window.pv_settings.store_id,
                store_name: window.pv_settings.store_name,
                store_url: window.pv_settings.store_url,
                current_plan: window.pv_settings.current_plan
            }
        }
        let dates = this.getCurrentAndNextWeekDate();
        this.current_date = dates.currentDate
        this.next_week_date = dates.nextWeekDate
        this.get_current_plan_list()
        this.is_have_paid_plan = this.store_info.current_plan.price > 0
        this.current_plan = this.store_info.current_plan
    },
    methods: {
        get_current_plan_list: function () {
            var self = this;
            this.isLoadingData = true;
            axios.post("/pv/get_plan_list", {
                "jsonrpc": "2.0",
                "params": {
                    referer: window.location.href
                }
            }).then(res => {
                let data = res.data.result
                if (data) {
                    self.list_plan = data
                    let current_plan = self.list_plan.find(plan => plan.id === window.pv_settings.current_plan.id);
                    if (current_plan) {
                        self.$emit('returnPaidFeatureVariable', current_plan.collection_page, current_plan.product_groups);
                    }
                }
                self.isLoadingData = false;
            }).catch(err => {
                console.error(err.message)
                self.isLoadingData = false;
            })
        },
        selectPlan(plan) {
            if (this.is_free_trial || this.is_have_paid_plan) {
                if (plan.price === 0) {
                    // this.modalViewDetailPlan = false
                    this.modalWarmDownGrade = true
                    this.current_upgrade_plan_model = plan
                }
            }
        },
        confirmDowngrade() {
            if (this.isLoadingData) {
                return
            }
            this.isLoadingData = true;
            var self = this
            axios.post("/pv/plan/charge", {
                "jsonrpc": "2.0",
                "params": {
                    referer: window.location.href,
                    plan_id: this.current_upgrade_plan_model.id,
                    store_url: this.store_info.store_url,
                }
            }).then(res => {
                // this.is_have_paid_plan = true
                let data = res.data.result
                if ('status' in data && data['status'] === 'error') {
                    self.show_toast('error', data['message'])
                }
                window.top.location.href = data['redirect_url']
                // self.modalUpgradePlan = false
                // self.is_free_trial = true
                self.isLoadingData = false;
            }).catch(err => {
                self.isLoadingData = false;
            })
        },
        viewDetailPLan() {
            this.modalViewDetailPlan = true
        },
        upgradeStorePlan() {
            if (this.isLoadingData) {
                return
            }
            this.isLoadingData = true;
            var self = this
            axios.post("/pv/plan/charge", {
                "jsonrpc": "2.0",
                "params": {
                    referer: window.location.href,
                    plan_id: this.current_upgrade_plan_model.id,
                    store_url: this.store_info.store_url,
                }
            }).then(res => {
                // this.is_have_paid_plan = true
                let data = res.data.result
                if ('status' in data && data['status'] === 'error') {
                    self.show_toast('error', data['message'])
                }
                // self.modalUpgradePlan = false
                // self.is_free_trial = true
                self.isLoadingData = false;
                window.top.location.href = data['charge_url']
            }).catch(err => {
                self.isLoadingData = false;
            })
        },
        convert_date_time: function (dateString) {
            const [year, month, day] = dateString.split('-');
            const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
            const monthName = months[parseInt(month, 10) - 1];
            return `${day} ${monthName} ${year}`;
        },
        getCurrentAndNextWeekDate() {
            let currentDate = new Date();
            let nextWeekDate = new Date(currentDate);
            nextWeekDate.setDate(currentDate.getDate() + 7);

            return {
                currentDate: this.formatDate(currentDate),
                nextWeekDate: this.formatDate(nextWeekDate)
            };
        },
        formatDate(date) {
            const day = date.getDate();
            const monthNames = [
                'January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December'
            ];
            const month = monthNames[date.getMonth()];
            const year = date.getFullYear();
            return `${day} ${month} ${year}`;
        },
        openUpgradePLan(plan) {
            if (plan.price > 0) {
                this.modalUpgradePlan = true
                this.current_upgrade_plan_model = plan
            }
        },
        closeUpgradePLan() {
            this.modalUpgradePlan = false
            this.current_upgrade_plan_model = {}
        },
        generateFloat: function (number) {
            function hash(n) {
                const prime1 = 2654435761;
                const prime2 = 4294967291;
                const hash = (n * prime1) % prime2;
                return hash;
            }

            const hashedValue = hash(number);
            const floatNumber = hashedValue / 4294967291;
            return floatNumber;
        },
        show_toast: function (type, message, duration = 2) {
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
    },
    computed: {}
}
</script>