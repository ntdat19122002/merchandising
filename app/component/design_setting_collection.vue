<template>

    <div style="width: 100%" v-if="is_has_plan_collection">
        <div style="display: flex; margin-bottom: 26px">
            <div class="pv-flex-row pv-center-align" style="gap: 8px">
                <div class="pv-page-title">Option Configuration</div>

                <Tooltip color="#171717">
                    <template #title>
                        <div class="pv-question-tooltip">
                            <a style="color: #4096FF" target="_blank"
                               href="https://support.nestscale.com/nestscale-product-variants/how-to-custom-swatch-display-on-collection-page/">Click
                                here</a> get more information
                            about option configuration
                        </div>
                    </template>
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M12.5899 6.05006C11.6599 5.89006 10.6999 6.07005 9.88995 6.54005C9.07995 7.02005 8.45995 7.77005 8.13995 8.66005C7.95995 9.18005 8.22995 9.75006 8.74995 9.93007C9.26995 10.1201 9.83995 9.84008 10.0199 9.32008C10.1799 8.88008 10.4899 8.50008 10.8999 8.26008C11.2999 8.02008 11.7799 7.93008 12.2499 8.01008C12.7199 8.09008 13.1399 8.33007 13.4399 8.68007C13.7499 9.06007 13.9199 9.51005 13.9099 9.98005C13.9099 11.0101 12.1899 11.8301 11.5899 12.0301C11.0699 12.2001 10.7799 12.7701 10.9599 13.2901C11.0999 13.7101 11.4899 13.97 11.9099 13.97C12.0099 13.97 12.1199 13.9501 12.2299 13.9201C12.6099 13.8001 15.9099 12.62 15.9099 9.97004C15.9099 9.04004 15.5799 8.12008 14.9699 7.38008C14.3599 6.66008 13.5199 6.18009 12.5899 6.02009V6.05006Z"
                            fill="#666666"/>
                        <path
                            d="M12.01 16C11.46 16 11.01 16.45 11.01 17C11.01 17.55 11.46 18 12.01 18C12.56 18 13.01 17.55 13.01 17C13.01 16.45 12.56 16 12.01 16Z"
                            fill="#666666"/>
                        <path
                            d="M12 1C5.93 1 1 5.93 1 12C1 18.07 5.93 23 12 23C18.07 23 23 18.07 23 12C23 5.93 18.07 1 12 1ZM12 21C7.04 21 3 16.96 3 12C3 7.04 7.04 3 12 3C16.96 3 21 7.04 21 12C21 16.96 16.96 21 12 21Z"
                            fill="#666666"/>
                    </svg>
                </Tooltip>
            </div>
        </div>
        <div class="pv-flex-column" style="gap: 24px">
            <div class="pv-flex-column pv-design-setting-item">
                <div class=" pv-design-item-component">
                    <div class="pv-flex-row-center" style="gap: 16px">
                        <div class="pv-value-of-variant-option">Swatch Circle in Square</div>
                        <div class="pv-design-item-component-in-use" style="background: #E6F4FF;"
                             v-if="statusInUse('swatch_circle_in_square')">
                            <svg width="12" height="12" viewBox="0 0 12 12" fill="none"
                                 xmlns="http://www.w3.org/2000/svg">
                                <path
                                    d="M2 6C2 3.79086 3.79086 2 6 2C8.20914 2 10 3.79086 10 6C10 8.20914 8.20914 10 6 10C3.79086 10 2 8.20914 2 6Z"
                                    fill="#1677FF"/>
                            </svg>
                            <div class="pv-button-style" style="color: #1677FF">In use</div>
                        </div>
                        <div class="pv-design-item-component-in-use" v-else style="background: #FAFAFA">
                            <svg width="12" height="12" viewBox="0 0 12 12" fill="none"
                                 xmlns="http://www.w3.org/2000/svg">
                                <path
                                    d="M2 6C2 3.79086 3.79086 2 6 2C8.20914 2 10 3.79086 10 6C10 8.20914 8.20914 10 6 10C3.79086 10 2 8.20914 2 6Z"
                                    fill="#333333"/>
                            </svg>
                            <div class="pv-button-style" style="color: #333">Unused</div>
                        </div>
                    </div>
                    <div class="pv-custom-design-setting"
                         @click="openDesignItem('Swatch Circle in Square')">
                        <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M1.53627 8.16269C1.32627 8.46019 1.20377 8.80434 1.18044 9.16601C1.16294 9.52184 1.25044 9.88935 1.43127 10.1985C1.61211 10.5077 1.87461 10.7585 2.20711 10.9394C2.53377 11.1027 2.89544 11.1668 3.25127 11.126L4.07961 11.0386C4.25461 11.0211 4.44127 11.0618 4.58711 11.1435C4.74461 11.2368 4.86127 11.3652 4.93127 11.5285L5.26961 12.2985C5.41544 12.631 5.66044 12.911 5.95211 13.0977C6.25544 13.3018 6.61127 13.4068 6.97877 13.4068C7.34627 13.4068 7.70211 13.3018 7.99377 13.1035C8.29711 12.911 8.54211 12.631 8.68794 12.2927L9.02627 11.5227C9.09627 11.3652 9.21294 11.231 9.37044 11.1435C9.52211 11.056 9.69711 11.0211 9.87211 11.0386L10.7004 11.126C11.0679 11.1668 11.4354 11.1027 11.7504 10.9335C12.0771 10.7702 12.3454 10.5194 12.5263 10.2044C12.7071 9.88936 12.7946 9.5335 12.7771 9.16601C12.7596 8.80434 12.6313 8.44853 12.4213 8.16853L11.9254 7.48016C11.8263 7.34016 11.7679 7.17102 11.7679 6.99018C11.7679 6.81518 11.8263 6.6402 11.9254 6.5002L12.4213 5.81768C12.6313 5.52018 12.7538 5.17603 12.7771 4.81436C12.7946 4.45853 12.7071 4.09101 12.5321 3.77601C12.3513 3.46684 12.0888 3.216 11.7563 3.041C11.4296 2.87767 11.0621 2.81354 10.7121 2.85437L9.88377 2.94188C9.70877 2.95938 9.52211 2.91852 9.37627 2.83685C9.22461 2.74935 9.10211 2.61517 9.03211 2.45183L8.68794 1.68186C8.54211 1.34936 8.29711 1.06937 8.00544 0.882699C7.39877 0.480199 6.54711 0.486033 5.95794 0.882699C5.65461 1.08103 5.41544 1.35521 5.26377 1.69354L4.92544 2.46351C4.85544 2.62684 4.73294 2.76102 4.58711 2.84269C4.43544 2.93019 4.25461 2.96516 4.07377 2.95349L3.24544 2.86605C2.88961 2.82521 2.52211 2.88935 2.18377 3.05852C1.86294 3.22769 1.59461 3.47853 1.41961 3.79353C1.24461 4.10853 1.15127 4.47021 1.16877 4.82604C1.18627 5.18771 1.30877 5.53186 1.52461 5.83519L2.01461 6.50604C2.11961 6.65188 2.17794 6.82686 2.17794 7.00186C2.17794 7.17686 2.12544 7.34601 2.02044 7.49184L1.52461 8.17437L1.53627 8.16269ZM2.97711 5.81184L2.48711 5.14099C2.40544 5.02432 2.35877 4.89604 2.35294 4.75604C2.34711 4.62187 2.37627 4.48768 2.44627 4.36518C2.51627 4.24852 2.61544 4.14936 2.73211 4.08519C2.85461 4.02103 2.99461 3.9977 3.13461 4.0152L3.97461 4.10271C4.39461 4.14938 4.80877 4.05601 5.18211 3.84601C5.54961 3.63017 5.83544 3.30937 6.00461 2.92437L6.34294 2.15433C6.40127 2.03183 6.48877 1.92688 6.61127 1.84521C6.83294 1.69938 7.14211 1.69355 7.38127 1.84521C7.49211 1.91521 7.58544 2.02015 7.63794 2.14849L7.98211 2.91853C8.15127 3.30936 8.43711 3.62434 8.81044 3.84601C9.17794 4.05017 9.59794 4.14354 10.0121 4.09687L10.8579 4.00936C10.9863 3.99186 11.1263 4.01518 11.2371 4.07352C11.3654 4.13768 11.4646 4.23684 11.5346 4.35934C11.6046 4.47601 11.6338 4.61604 11.6279 4.7502C11.6221 4.8902 11.5754 5.01855 11.4938 5.12938L10.9979 5.81184C10.7471 6.156 10.6188 6.56434 10.6188 6.98434C10.6188 7.41018 10.7529 7.83019 10.9979 8.16269L11.4938 8.85105C11.5696 8.95605 11.6163 9.09016 11.6279 9.22432C11.6338 9.36432 11.6046 9.50436 11.5346 9.62102C11.4646 9.73769 11.3654 9.83101 11.2371 9.89517C11.1204 9.95934 10.9863 9.97684 10.8463 9.96517L10.0179 9.87765C9.59794 9.83099 9.16627 9.91852 8.79877 10.1344C8.43127 10.3502 8.14544 10.6652 7.97627 11.0502L7.63794 11.8202C7.57961 11.9427 7.49211 12.0477 7.36961 12.1294C7.14794 12.2752 6.83877 12.281 6.59961 12.1235C6.48294 12.0535 6.39544 11.9485 6.34294 11.826L6.00461 11.056C5.83544 10.671 5.54961 10.3502 5.17044 10.1285C4.80294 9.91852 4.38877 9.83682 3.96877 9.87765L3.12877 9.96517C2.99461 9.97684 2.86044 9.95351 2.74377 9.90101C2.61544 9.83684 2.51627 9.73768 2.44627 9.61518C2.37627 9.49852 2.34711 9.35849 2.35294 9.22432C2.35877 9.08432 2.40544 8.95605 2.48711 8.84521L2.98294 8.16269C3.23377 7.81269 3.36211 7.41018 3.36211 6.99018C3.36211 6.57018 3.23377 6.16184 2.97711 5.81184Z"
                                fill="#333333"/>
                            <path
                                d="M6.98464 9.32938C8.27381 9.32938 9.31797 8.28521 9.31797 6.99604C9.31797 5.70688 8.27381 4.66271 6.98464 4.66271C5.69547 4.66271 4.65131 5.70688 4.65131 6.99604C4.65131 8.28521 5.69547 9.32938 6.98464 9.32938ZM6.98464 5.82938C7.62631 5.82938 8.15131 6.35438 8.15131 6.99604C8.15131 7.63771 7.62631 8.16271 6.98464 8.16271C6.34297 8.16271 5.81797 7.63771 5.81797 6.99604C5.81797 6.35438 6.34297 5.82938 6.98464 5.82938Z"
                                fill="#333333"/>
                        </svg>

                        Customize
                    </div>
                </div>
                <div class="pv-design-setting-swatch-square" style="display: flex; gap: 16px">
                    <img src="/nestprdvariant/static/images/design_setting/SwatchCircleInSquare/Frame427319054.png"
                         alt="">
                    <img src="/nestprdvariant/static/images/design_setting/SwatchCircleInSquare/Frame427319056.png"
                         alt="">
                    <img src="/nestprdvariant/static/images/design_setting/SwatchCircleInSquare/Frame427319059.png"
                         alt="">
                    <img src="/nestprdvariant/static/images/design_setting/SwatchCircleInSquare/Frame427319062.png"
                         alt="">
                    <img src="/nestprdvariant/static/images/design_setting/SwatchCircleInSquare/Frame427319063.png"
                         alt="">
                    <img style="border: 1px #ECECEC solid" alt=""
                         src="/nestprdvariant/static/images/design_setting/SwatchCircleInSquare/Frame27319064.png">
                    <div class="pv-rainbow-container"
                         style="border-radius: 4px;border: 1px solid #D9D9D9;height: 64px;width: 64px;">
                        <div style="height: 48px;width: 48px;
                                background: linear-gradient(0deg, rgba(255, 255, 255, 0.40) 0%, rgba(255, 255, 255, 0.40) 100%), url('https://app.nestscale.com/nestprdvariant/static/images/rainbow.png') lightgray 50% / cover no-repeat;">
                        </div>
                        <div class="pv-plus-variant-hidden">+2</div>
                    </div>
                </div>
            </div>


            <div class="pv-design-setting-item pv-flex-column">
                <div class="pv-design-item-component">
                    <div class="pv-flex-row-center" style="gap: 16px">
                        <div class="pv-value-of-variant-option">Circular Swatch</div>
                        <div class="pv-design-item-component-in-use" v-if="statusInUse('circular_swatch')"
                             style="background: #E6F4FF;">
                            <svg width="12" height="12" viewBox="0 0 12 12" fill="none"
                                 xmlns="http://www.w3.org/2000/svg">
                                <path
                                    d="M2 6C2 3.79086 3.79086 2 6 2C8.20914 2 10 3.79086 10 6C10 8.20914 8.20914 10 6 10C3.79086 10 2 8.20914 2 6Z"
                                    fill="#1677FF"/>
                            </svg>
                            <div class="pv-button-style" style="color: #1677FF">In use</div>
                        </div>
                        <div class="pv-design-item-component-in-use" v-else style="background: #FAFAFA">
                            <svg width="12" height="12" viewBox="0 0 12 12" fill="none"
                                 xmlns="http://www.w3.org/2000/svg">
                                <path
                                    d="M2 6C2 3.79086 3.79086 2 6 2C8.20914 2 10 3.79086 10 6C10 8.20914 8.20914 10 6 10C3.79086 10 2 8.20914 2 6Z"
                                    fill="#333333"/>
                            </svg>
                            <div class="pv-button-style" style="color: #333">Unused</div>
                        </div>
                    </div>

                    <div class="pv-custom-design-setting" @click="openDesignItem('Circular Swatch')">
                        <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M1.53627 8.16269C1.32627 8.46019 1.20377 8.80434 1.18044 9.16601C1.16294 9.52184 1.25044 9.88935 1.43127 10.1985C1.61211 10.5077 1.87461 10.7585 2.20711 10.9394C2.53377 11.1027 2.89544 11.1668 3.25127 11.126L4.07961 11.0386C4.25461 11.0211 4.44127 11.0618 4.58711 11.1435C4.74461 11.2368 4.86127 11.3652 4.93127 11.5285L5.26961 12.2985C5.41544 12.631 5.66044 12.911 5.95211 13.0977C6.25544 13.3018 6.61127 13.4068 6.97877 13.4068C7.34627 13.4068 7.70211 13.3018 7.99377 13.1035C8.29711 12.911 8.54211 12.631 8.68794 12.2927L9.02627 11.5227C9.09627 11.3652 9.21294 11.231 9.37044 11.1435C9.52211 11.056 9.69711 11.0211 9.87211 11.0386L10.7004 11.126C11.0679 11.1668 11.4354 11.1027 11.7504 10.9335C12.0771 10.7702 12.3454 10.5194 12.5263 10.2044C12.7071 9.88936 12.7946 9.5335 12.7771 9.16601C12.7596 8.80434 12.6313 8.44853 12.4213 8.16853L11.9254 7.48016C11.8263 7.34016 11.7679 7.17102 11.7679 6.99018C11.7679 6.81518 11.8263 6.6402 11.9254 6.5002L12.4213 5.81768C12.6313 5.52018 12.7538 5.17603 12.7771 4.81436C12.7946 4.45853 12.7071 4.09101 12.5321 3.77601C12.3513 3.46684 12.0888 3.216 11.7563 3.041C11.4296 2.87767 11.0621 2.81354 10.7121 2.85437L9.88377 2.94188C9.70877 2.95938 9.52211 2.91852 9.37627 2.83685C9.22461 2.74935 9.10211 2.61517 9.03211 2.45183L8.68794 1.68186C8.54211 1.34936 8.29711 1.06937 8.00544 0.882699C7.39877 0.480199 6.54711 0.486033 5.95794 0.882699C5.65461 1.08103 5.41544 1.35521 5.26377 1.69354L4.92544 2.46351C4.85544 2.62684 4.73294 2.76102 4.58711 2.84269C4.43544 2.93019 4.25461 2.96516 4.07377 2.95349L3.24544 2.86605C2.88961 2.82521 2.52211 2.88935 2.18377 3.05852C1.86294 3.22769 1.59461 3.47853 1.41961 3.79353C1.24461 4.10853 1.15127 4.47021 1.16877 4.82604C1.18627 5.18771 1.30877 5.53186 1.52461 5.83519L2.01461 6.50604C2.11961 6.65188 2.17794 6.82686 2.17794 7.00186C2.17794 7.17686 2.12544 7.34601 2.02044 7.49184L1.52461 8.17437L1.53627 8.16269ZM2.97711 5.81184L2.48711 5.14099C2.40544 5.02432 2.35877 4.89604 2.35294 4.75604C2.34711 4.62187 2.37627 4.48768 2.44627 4.36518C2.51627 4.24852 2.61544 4.14936 2.73211 4.08519C2.85461 4.02103 2.99461 3.9977 3.13461 4.0152L3.97461 4.10271C4.39461 4.14938 4.80877 4.05601 5.18211 3.84601C5.54961 3.63017 5.83544 3.30937 6.00461 2.92437L6.34294 2.15433C6.40127 2.03183 6.48877 1.92688 6.61127 1.84521C6.83294 1.69938 7.14211 1.69355 7.38127 1.84521C7.49211 1.91521 7.58544 2.02015 7.63794 2.14849L7.98211 2.91853C8.15127 3.30936 8.43711 3.62434 8.81044 3.84601C9.17794 4.05017 9.59794 4.14354 10.0121 4.09687L10.8579 4.00936C10.9863 3.99186 11.1263 4.01518 11.2371 4.07352C11.3654 4.13768 11.4646 4.23684 11.5346 4.35934C11.6046 4.47601 11.6338 4.61604 11.6279 4.7502C11.6221 4.8902 11.5754 5.01855 11.4938 5.12938L10.9979 5.81184C10.7471 6.156 10.6188 6.56434 10.6188 6.98434C10.6188 7.41018 10.7529 7.83019 10.9979 8.16269L11.4938 8.85105C11.5696 8.95605 11.6163 9.09016 11.6279 9.22432C11.6338 9.36432 11.6046 9.50436 11.5346 9.62102C11.4646 9.73769 11.3654 9.83101 11.2371 9.89517C11.1204 9.95934 10.9863 9.97684 10.8463 9.96517L10.0179 9.87765C9.59794 9.83099 9.16627 9.91852 8.79877 10.1344C8.43127 10.3502 8.14544 10.6652 7.97627 11.0502L7.63794 11.8202C7.57961 11.9427 7.49211 12.0477 7.36961 12.1294C7.14794 12.2752 6.83877 12.281 6.59961 12.1235C6.48294 12.0535 6.39544 11.9485 6.34294 11.826L6.00461 11.056C5.83544 10.671 5.54961 10.3502 5.17044 10.1285C4.80294 9.91852 4.38877 9.83682 3.96877 9.87765L3.12877 9.96517C2.99461 9.97684 2.86044 9.95351 2.74377 9.90101C2.61544 9.83684 2.51627 9.73768 2.44627 9.61518C2.37627 9.49852 2.34711 9.35849 2.35294 9.22432C2.35877 9.08432 2.40544 8.95605 2.48711 8.84521L2.98294 8.16269C3.23377 7.81269 3.36211 7.41018 3.36211 6.99018C3.36211 6.57018 3.23377 6.16184 2.97711 5.81184Z"
                                fill="#333333"/>
                            <path
                                d="M6.98464 9.32938C8.27381 9.32938 9.31797 8.28521 9.31797 6.99604C9.31797 5.70688 8.27381 4.66271 6.98464 4.66271C5.69547 4.66271 4.65131 5.70688 4.65131 6.99604C4.65131 8.28521 5.69547 9.32938 6.98464 9.32938ZM6.98464 5.82938C7.62631 5.82938 8.15131 6.35438 8.15131 6.99604C8.15131 7.63771 7.62631 8.16271 6.98464 8.16271C6.34297 8.16271 5.81797 7.63771 5.81797 6.99604C5.81797 6.35438 6.34297 5.82938 6.98464 5.82938Z"
                                fill="#333333"/>
                        </svg>
                        Customize
                    </div>

                </div>
                <div class="pv-design-setting-circular-swatch-block pv-center-align">
                    <svg width="58" height="58" viewBox="0 0 58 58" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <rect x="5" y="5" width="48" height="48" rx="24" fill="white"/>
                        <circle cx="29" cy="29" r="23.5" fill="#FD72A4" stroke="#D9D9D9"/>
                        <g filter="url(#filter0_d_245_26967)">
                            <circle cx="29" cy="29" r="26.5" stroke="#1890FF" shape-rendering="crispEdges"/>
                        </g>
                        <defs>
                            <filter id="filter0_d_245_26967" x="0" y="0" width="58" height="58"
                                    filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                                <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                                <feColorMatrix in="SourceAlpha" type="matrix"
                                               values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                                <feMorphology radius="2" operator="dilate" in="SourceAlpha"
                                              result="effect1_dropShadow_245_26967"/>
                                <feOffset/>
                                <feComposite in2="hardAlpha" operator="out"/>
                                <feColorMatrix type="matrix"
                                               values="0 0 0 0 0.690196 0 0 0 0 0.890196 0 0 0 0 1 0 0 0 1 0"/>
                                <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_245_26967"/>
                                <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_245_26967"
                                         result="shape"/>
                            </filter>
                        </defs>
                    </svg>


                    <svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <g clip-path="url(#clip0_245_26905)">
                            <circle cx="24" cy="24" r="23.5" fill="#A480EF" stroke="#D9D9D9"/>
                        </g>
                        <defs>
                            <clipPath id="clip0_245_26905">
                                <rect width="48" height="48" rx="24" fill="white"/>
                            </clipPath>
                        </defs>
                    </svg>
                    <svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <g clip-path="url(#clip0_245_26907)">
                            <circle cx="24" cy="24" r="23.5" fill="#6B8E23" stroke="#D9D9D9"/>
                        </g>
                        <defs>
                            <clipPath id="clip0_245_26907">
                                <rect width="48" height="48" rx="24" fill="white"/>
                            </clipPath>
                        </defs>
                    </svg>
                    <svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <g clip-path="url(#clip0_245_26909)">
                            <circle cx="24" cy="24" r="23.5" fill="#FFA07A" stroke="#D9D9D9"/>
                        </g>
                        <defs>
                            <clipPath id="clip0_245_26909">
                                <rect width="48" height="48" rx="24" fill="white"/>
                            </clipPath>
                        </defs>
                    </svg>
                    <svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <g clip-path="url(#clip0_245_26911)">
                            <circle cx="24" cy="24" r="23.5" fill="#36C3FF" stroke="#D9D9D9"/>
                        </g>
                        <defs>
                            <clipPath id="clip0_245_26911">
                                <rect width="48" height="48" rx="24" fill="white"/>
                            </clipPath>
                        </defs>
                    </svg>
                    <svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <g clip-path="url(#clip0_245_26913)">
                            <circle cx="24" cy="24" r="23.5" fill="#FFCD4C" fill-opacity="0.3" stroke="#D9D9D9"/>
                            <path d="M0 0L48 48" stroke="#D9D9D9" stroke-linecap="round"/>
                        </g>
                        <defs>
                            <clipPath id="clip0_245_26913">
                                <rect width="48" height="48" rx="24" fill="white"/>
                            </clipPath>
                        </defs>
                    </svg>
                    <div class="pv-rainbow-container" style="width: auto">
                        <div style="height: 48px;width: 48px;
                                background: linear-gradient(0deg, rgba(255, 255, 255, 0.40) 0%, rgba(255, 255, 255, 0.40) 100%), url('https://app.nestscale.com/nestprdvariant/static/images/rainbow.png') lightgray 50% / cover no-repeat;">
                        </div>
                        <div class="pv-plus-variant-hidden">+2</div>
                    </div>

                </div>
            </div>
            <div class="pv-design-setting-item pv-flex-column">
                <div class="pv-design-item-component">
                    <div class="pv-flex-row-center" style="gap:16px">
                        <div class="pv-value-of-variant-option">Square Swatch</div>
                        <div class="pv-design-item-component-in-use" v-if="statusInUse('square_swatch')"
                             style="background: #E6F4FF;">
                            <svg width="12" height="12" viewBox="0 0 12 12" fill="none"
                                 xmlns="http://www.w3.org/2000/svg">
                                <path
                                    d="M2 6C2 3.79086 3.79086 2 6 2C8.20914 2 10 3.79086 10 6C10 8.20914 8.20914 10 6 10C3.79086 10 2 8.20914 2 6Z"
                                    fill="#1677FF"/>
                            </svg>
                            <div class="pv-button-style" style="color: #1677FF">In use</div>
                        </div>
                        <div class="pv-design-item-component-in-use" v-else style="background: #FAFAFA">
                            <svg width="12" height="12" viewBox="0 0 12 12" fill="none"
                                 xmlns="http://www.w3.org/2000/svg">
                                <path
                                    d="M2 6C2 3.79086 3.79086 2 6 2C8.20914 2 10 3.79086 10 6C10 8.20914 8.20914 10 6 10C3.79086 10 2 8.20914 2 6Z"
                                    fill="#333333"/>
                            </svg>
                            <div class="pv-button-style" style="color: #333">Unused</div>
                        </div>
                    </div>

                    <div class="pv-custom-design-setting" @click="openDesignItem('Square Swatch')">
                        <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M1.53627 8.16269C1.32627 8.46019 1.20377 8.80434 1.18044 9.16601C1.16294 9.52184 1.25044 9.88935 1.43127 10.1985C1.61211 10.5077 1.87461 10.7585 2.20711 10.9394C2.53377 11.1027 2.89544 11.1668 3.25127 11.126L4.07961 11.0386C4.25461 11.0211 4.44127 11.0618 4.58711 11.1435C4.74461 11.2368 4.86127 11.3652 4.93127 11.5285L5.26961 12.2985C5.41544 12.631 5.66044 12.911 5.95211 13.0977C6.25544 13.3018 6.61127 13.4068 6.97877 13.4068C7.34627 13.4068 7.70211 13.3018 7.99377 13.1035C8.29711 12.911 8.54211 12.631 8.68794 12.2927L9.02627 11.5227C9.09627 11.3652 9.21294 11.231 9.37044 11.1435C9.52211 11.056 9.69711 11.0211 9.87211 11.0386L10.7004 11.126C11.0679 11.1668 11.4354 11.1027 11.7504 10.9335C12.0771 10.7702 12.3454 10.5194 12.5263 10.2044C12.7071 9.88936 12.7946 9.5335 12.7771 9.16601C12.7596 8.80434 12.6313 8.44853 12.4213 8.16853L11.9254 7.48016C11.8263 7.34016 11.7679 7.17102 11.7679 6.99018C11.7679 6.81518 11.8263 6.6402 11.9254 6.5002L12.4213 5.81768C12.6313 5.52018 12.7538 5.17603 12.7771 4.81436C12.7946 4.45853 12.7071 4.09101 12.5321 3.77601C12.3513 3.46684 12.0888 3.216 11.7563 3.041C11.4296 2.87767 11.0621 2.81354 10.7121 2.85437L9.88377 2.94188C9.70877 2.95938 9.52211 2.91852 9.37627 2.83685C9.22461 2.74935 9.10211 2.61517 9.03211 2.45183L8.68794 1.68186C8.54211 1.34936 8.29711 1.06937 8.00544 0.882699C7.39877 0.480199 6.54711 0.486033 5.95794 0.882699C5.65461 1.08103 5.41544 1.35521 5.26377 1.69354L4.92544 2.46351C4.85544 2.62684 4.73294 2.76102 4.58711 2.84269C4.43544 2.93019 4.25461 2.96516 4.07377 2.95349L3.24544 2.86605C2.88961 2.82521 2.52211 2.88935 2.18377 3.05852C1.86294 3.22769 1.59461 3.47853 1.41961 3.79353C1.24461 4.10853 1.15127 4.47021 1.16877 4.82604C1.18627 5.18771 1.30877 5.53186 1.52461 5.83519L2.01461 6.50604C2.11961 6.65188 2.17794 6.82686 2.17794 7.00186C2.17794 7.17686 2.12544 7.34601 2.02044 7.49184L1.52461 8.17437L1.53627 8.16269ZM2.97711 5.81184L2.48711 5.14099C2.40544 5.02432 2.35877 4.89604 2.35294 4.75604C2.34711 4.62187 2.37627 4.48768 2.44627 4.36518C2.51627 4.24852 2.61544 4.14936 2.73211 4.08519C2.85461 4.02103 2.99461 3.9977 3.13461 4.0152L3.97461 4.10271C4.39461 4.14938 4.80877 4.05601 5.18211 3.84601C5.54961 3.63017 5.83544 3.30937 6.00461 2.92437L6.34294 2.15433C6.40127 2.03183 6.48877 1.92688 6.61127 1.84521C6.83294 1.69938 7.14211 1.69355 7.38127 1.84521C7.49211 1.91521 7.58544 2.02015 7.63794 2.14849L7.98211 2.91853C8.15127 3.30936 8.43711 3.62434 8.81044 3.84601C9.17794 4.05017 9.59794 4.14354 10.0121 4.09687L10.8579 4.00936C10.9863 3.99186 11.1263 4.01518 11.2371 4.07352C11.3654 4.13768 11.4646 4.23684 11.5346 4.35934C11.6046 4.47601 11.6338 4.61604 11.6279 4.7502C11.6221 4.8902 11.5754 5.01855 11.4938 5.12938L10.9979 5.81184C10.7471 6.156 10.6188 6.56434 10.6188 6.98434C10.6188 7.41018 10.7529 7.83019 10.9979 8.16269L11.4938 8.85105C11.5696 8.95605 11.6163 9.09016 11.6279 9.22432C11.6338 9.36432 11.6046 9.50436 11.5346 9.62102C11.4646 9.73769 11.3654 9.83101 11.2371 9.89517C11.1204 9.95934 10.9863 9.97684 10.8463 9.96517L10.0179 9.87765C9.59794 9.83099 9.16627 9.91852 8.79877 10.1344C8.43127 10.3502 8.14544 10.6652 7.97627 11.0502L7.63794 11.8202C7.57961 11.9427 7.49211 12.0477 7.36961 12.1294C7.14794 12.2752 6.83877 12.281 6.59961 12.1235C6.48294 12.0535 6.39544 11.9485 6.34294 11.826L6.00461 11.056C5.83544 10.671 5.54961 10.3502 5.17044 10.1285C4.80294 9.91852 4.38877 9.83682 3.96877 9.87765L3.12877 9.96517C2.99461 9.97684 2.86044 9.95351 2.74377 9.90101C2.61544 9.83684 2.51627 9.73768 2.44627 9.61518C2.37627 9.49852 2.34711 9.35849 2.35294 9.22432C2.35877 9.08432 2.40544 8.95605 2.48711 8.84521L2.98294 8.16269C3.23377 7.81269 3.36211 7.41018 3.36211 6.99018C3.36211 6.57018 3.23377 6.16184 2.97711 5.81184Z"
                                fill="#333333"/>
                            <path
                                d="M6.98464 9.32938C8.27381 9.32938 9.31797 8.28521 9.31797 6.99604C9.31797 5.70688 8.27381 4.66271 6.98464 4.66271C5.69547 4.66271 4.65131 5.70688 4.65131 6.99604C4.65131 8.28521 5.69547 9.32938 6.98464 9.32938ZM6.98464 5.82938C7.62631 5.82938 8.15131 6.35438 8.15131 6.99604C8.15131 7.63771 7.62631 8.16271 6.98464 8.16271C6.34297 8.16271 5.81797 7.63771 5.81797 6.99604C5.81797 6.35438 6.34297 5.82938 6.98464 5.82938Z"
                                fill="#333333"/>
                        </svg>
                        Customize
                    </div>

                </div>
                <div class="pv-design-setting-square_swatch-block">
                    <div style="display: flex; align-items: center; gap: 16px">
                        <img src="/nestprdvariant/static/images/design_setting/SquareSwatch/image28.png" alt="">
                        <img src="/nestprdvariant/static/images/design_setting/SquareSwatch/image29.png" alt="">
                        <img src="/nestprdvariant/static/images/design_setting/SquareSwatch/image30.png" alt="">
                        <img src="/nestprdvariant/static/images/design_setting/SquareSwatch/image31.png" alt="">
                        <img src="/nestprdvariant/static/images/design_setting/SquareSwatch/image32.png" alt="">
                        <img src="/nestprdvariant/static/images/design_setting/SquareSwatch/image33.png" alt="">
                        <div class="pv-rainbow-container"
                             style="border-radius: 4px;border: 1px solid #D9D9D9;height: 57px;width: 57px">
                            <div style="height: 42px;width: 42px;
                                background: linear-gradient(0deg, rgba(255, 255, 255, 0.40) 0%, rgba(255, 255, 255, 0.40) 100%), url('https://app.nestscale.com/nestprdvariant/static/images/rainbow.png') lightgray 50% / cover no-repeat;">
                            </div>
                            <div class="pv-plus-variant-hidden">+2</div>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
    <div v-else style="padding: 26px 40px">
        <div class="pv-flex-column" style="gap: 8px">
            <div class="pv-page-title">Option Configuration</div>
            <div
                style=" width: 1535px;height:520px;background-image: url('https://app.nestscale.com/nestprdvariant/static/images/design_setting/collectionFrame.png'); background-size: cover; background-position: center; background-repeat: no-repeat;">
            </div>
        </div>
    </div>

</template>
<script>
import {Select, SelectOption, Tooltip} from "ant-design-vue"
import axios from "axios"

export default {
    name: 'DesignSettingCollection',
    emits: ["changePage"],
    components: {Tooltip, Select, SelectOption},
    props: {
        is_has_plan_collection: Boolean
    },
    data() {
        return {
            list_option: [],
            select_option: '2',
            data_select_option: [{
                value: '1',
                label: "Baby Pink Buckled Flatform Sandals",
                url_img: '/nestprdvariant/static/images/design_setting/preview_design_setting/360e319423a9198a82efa471f5487300.png'
            }, {
                url_img: '/nestprdvariant/static/images/design_setting/preview_design_setting/b5db6ab0fae1f58595559cc432b10e7f.jpeg',
                label: 'Lilac Purple Buckled Flatform Sandals',
                value: '2'
            }, {
                value: '3',
                label: "Sand Brown Pink Buckled Flatform Sandals",
                url_img: "/nestprdvariant/static/images/design_setting/preview_design_setting/e49abe93ef9e2c16f65cf8969100d9f6.png"
            }, {
                value: '4',
                url_img: '/nestprdvariant/static/images/design_setting/preview_design_setting/7c010d272cd9c537ebbddbd637222a62.png',
                label: "Light Green Buckled Flatform Sandals"
            }, {
                value: '5',
                url_img: '/nestprdvariant/static/images/design_setting/preview_design_setting/ec8406eafffaabdba2d3b1514fcf82df.jpeg',
                label: "Sky Blue Buckled Flatform Sandals"
            }]
        }
    },
    methods: {
        selectSquareInDropdown() {
            for (let option of this.data_select_option) {
                if (option.value === this.select_option) {
                    this.selected_option = JSON.parse(JSON.stringify(option))
                }
            }
        },
        openDesignItem(designItemName) {
            this.$emit('changePage', 'collection_page', designItemName)
        },
        statusInUse(option_name) {
            for (let option of this.list_option) {
                if (option.display_type_collection_page === option_name) {
                    return true
                }
            }
            return false
        }
    },
    mounted() {
        axios.post("/pv/fetch_variant", {
            jsonrpc: 2,
            params: {store_url: window.pv_settings.store_url, referer: window.location.href}
        }).then(res => {
            if (res.data.result.code === 1) {
                this.list_option = res.data.result.list_option
            }
            if (res.data.result.code === -1) {
                this.show_toast("error", "Something went wrong. Please contact the customer support.")
                console.log(res.data.result.exception)
            }
        }).catch(error => {
            console.log(error)
        })
    }
}
</script>