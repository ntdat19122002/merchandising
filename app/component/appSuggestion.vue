<template>
    <div style="padding: 40px 28px">
        <div style="font-weight: 700; font-size: 26px; line-height: 33px; color: #2C2F32; margin-bottom: 28px">
            Recommendations
        </div>

        <div class="nestscale-start-justify gap-20">
            <div class="nestscale-start-justify flex-column gap-20" style="flex: 6">
                <div class="nestscale-block" style="padding: 20px; min-width: 500px">
                    <div style="font-weight: 600; font-size: 16px; line-height: 22px; color: #48484A;">
                        More apps by NestScale
                    </div>
                    <div class="nestscale-start-justify gap-24"
                         style="margin-top: 24px; flex-wrap: wrap; align-items: flex-start;">
                        <div v-for="app in tempAppNestScale" class="nestscale-start-justify gap-10"
                             style="width: 300px;">
                            <img :src="app.app_logo"
                                 style="width: 60px; height: 60px; object-fit: cover; border: 1px solid #D9D9D9; border-radius: 8px; padding: 1px">
                            <div class="nestscale-start-justify flex-column gap-4">
                                <div style="font-weight: 600; font-size: 16px; line-height: 20px; color: #000000;">
                                    {{ app.name }}
                                </div>
                                <div class="nestscale-center-align gap-4">
                                    <div>{{ app.rate_number }}</div>
                                    <img src="https://apps.nestscale.com/omnichat/static/img/start_review.svg">
                                    <div>({{ parseInt(app.reviews_number).toLocaleString() }})</div>
                                </div>
                                <div
                                    style="font-weight: 400; font-size: 14px; color: #6B6B6B; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden;">
                                    {{
                                        app.short_description
                                    }}
                                </div>
                                <div class="nestscale-center-align gap-4"
                                     @click="openLink(app.app_link)"
                                     style="color: #3199FF; font-weight: 500; font-size: 14px; cursor: pointer">
                                    <div>Visit app</div>
                                    <svg width="11" height="12" viewBox="0 0 11 12" fill="none"
                                         xmlns="http://www.w3.org/2000/svg">
                                        <path
                                            d="M10.167 4.5L10.167 1.5M10.167 1.5H7.16699M10.167 1.5L6.16699 5.5M4.66699 2.5H3.56699C2.72691 2.5 2.30687 2.5 1.98601 2.66349C1.70376 2.8073 1.47429 3.03677 1.33048 3.31901C1.16699 3.63988 1.16699 4.05992 1.16699 4.9V8.1C1.16699 8.94008 1.16699 9.36012 1.33048 9.68099C1.47429 9.96323 1.70376 10.1927 1.98601 10.3365C2.30687 10.5 2.72691 10.5 3.56699 10.5H6.76699C7.60707 10.5 8.02711 10.5 8.34798 10.3365C8.63022 10.1927 8.85969 9.96323 9.0035 9.68099C9.16699 9.36012 9.16699 8.94008 9.16699 8.1V7"
                                            stroke="#1890FF" stroke-width="1.4" stroke-linecap="round"
                                            stroke-linejoin="round"/>
                                    </svg>

                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="nestscale-center-justify" style="margin-top: 30px" v-if="pageCountAppNestScale > 0">
                        <div class="nestscale-center-align gap-16">
                            <svg width="6" height="11"
                                 style="cursor: pointer"
                                 @click="decreasePage"
                                 viewBox="0 0 6 11" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M4.83203 9.5L0.832031 5.5L4.83203 1.5" stroke="black" stroke-width="1.5"
                                      stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                            <div v-for="i in pageCountAppNestScale"
                                 class="pagination"
                                 @click="currentPageNestScale = i"
                                 :class="currentPageNestScale === i ? 'selected': ''">
                                {{ i }}
                            </div>
                            <svg width="6" height="11"
                                 style="cursor: pointer"
                                 @click="nextPage()"
                                 viewBox="0 0 6 11" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M0.832031 9.5L4.83203 5.5L0.832031 1.5" stroke="black" stroke-width="1.5"
                                      stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </div>
                    </div>
                </div>

                <div class="nestscale-block" style="padding: 20px; min-width: 500px;">
                    <div style="font-weight: 600; font-size: 16px; line-height: 22px; color: #48484A;">
                        Suggested apps from our partners
                    </div>
                    <div class="nestscale-start-justify gap-24"
                         style="margin-top: 24px; flex-wrap: wrap; align-items: flex-start;">
                        <div v-for="app in tempAppPartner" class="nestscale-start-justify gap-10"
                             style="width: 300px;">
                            <img :src="app.app_logo"
                                 style="width: 60px; height: 60px; object-fit: cover; border: 1px solid #D9D9D9; border-radius: 8px; padding: 1px">
                            <div class="nestscale-start-justify flex-column gap-4">
                                <div style="font-weight: 600; font-size: 16px; line-height: 20px; color: #000000;">
                                    {{ app.name }}
                                </div>
                                <div class="nestscale-center-align gap-4">
                                    <div>{{ app.rate_number }}</div>
                                    <img src="https://apps.nestscale.com/omnichat/static/img/start_review.svg">
                                    <div>({{ parseInt(app.reviews_number).toLocaleString() }})</div>
                                </div>
                                <div
                                    style="font-weight: 400; font-size: 14px; color: #6B6B6B; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
                                    {{
                                        app.short_description
                                    }}
                                </div>
                                <div class="nestscale-center-align gap-4"
                                     @click="openLink(app.app_link)"
                                     style="color: #3199FF; font-weight: 500; font-size: 14px; cursor: pointer">
                                    <div>Visit app</div>
                                    <svg width="11" height="12" viewBox="0 0 11 12" fill="none"
                                         xmlns="http://www.w3.org/2000/svg">
                                        <path
                                            d="M10.167 4.5L10.167 1.5M10.167 1.5H7.16699M10.167 1.5L6.16699 5.5M4.66699 2.5H3.56699C2.72691 2.5 2.30687 2.5 1.98601 2.66349C1.70376 2.8073 1.47429 3.03677 1.33048 3.31901C1.16699 3.63988 1.16699 4.05992 1.16699 4.9V8.1C1.16699 8.94008 1.16699 9.36012 1.33048 9.68099C1.47429 9.96323 1.70376 10.1927 1.98601 10.3365C2.30687 10.5 2.72691 10.5 3.56699 10.5H6.76699C7.60707 10.5 8.02711 10.5 8.34798 10.3365C8.63022 10.1927 8.85969 9.96323 9.0035 9.68099C9.16699 9.36012 9.16699 8.94008 9.16699 8.1V7"
                                            stroke="#1890FF" stroke-width="1.4" stroke-linecap="round"
                                            stroke-linejoin="round"/>
                                    </svg>

                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="nestscale-center-justify" style="margin-top: 30px">
                        <div class="nestscale-center-align gap-16">
                            <svg width="6" height="11"
                                 style="cursor: pointer"
                                 @click="decreasePage"
                                 viewBox="0 0 6 11" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M4.83203 9.5L0.832031 5.5L4.83203 1.5" stroke="black" stroke-width="1.5"
                                      stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                            <div v-for="i in pageCountAppPartner"
                                 class="pagination"
                                 @click="currentPagePartner = i"
                                 :class="currentPagePartner === i ? 'selected': ''">
                                {{ i }}
                            </div>
                            <svg width="6" height="11"
                                 style="cursor: pointer"
                                 @click="nextPage()"
                                 viewBox="0 0 6 11" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M0.832031 9.5L4.83203 5.5L0.832031 1.5" stroke="black" stroke-width="1.5"
                                      stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </div>
                    </div>
                </div>
                <div class="nestscale-block" style="padding: 20px; min-width: 500px;">
                    <div style="font-weight: 600; font-size: 16px; line-height: 22px; color: #48484A;">
                        Empower your business with our service partners
                    </div>
                    <div class="nestscale-start-justify flex-column gap-12"
                         style="margin-top: 24px; flex-wrap: wrap; align-items: flex-start;">
                        <div v-for="app in tempService" class="nestscale-start-justify gap-10">
                            <img :src="app.app_logo"
                                 style="width: 60px; height: 60px; object-fit: cover; border: 1px solid #D9D9D9; border-radius: 8px; padding: 1px">
                            <div class="nestscale-start-justify flex-column gap-4">
                                <div style="font-weight: 600; font-size: 16px; line-height: 20px; color: #000000;">
                                    {{ app.name }}
                                </div>
                                <div
                                    style="font-weight: 400; font-size: 14px; color: #6B6B6B; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
                                    {{
                                        app.short_description
                                    }}
                                </div>
                                <div class="nestscale-center-align gap-4"
                                     @click="openLink(app.app_link)"
                                     style="color: #3199FF; font-weight: 500; font-size: 14px; cursor: pointer">
                                    <div>Explore now</div>
                                    <svg width="11" height="12" viewBox="0 0 11 12" fill="none"
                                         xmlns="http://www.w3.org/2000/svg">
                                        <path
                                            d="M10.167 4.5L10.167 1.5M10.167 1.5H7.16699M10.167 1.5L6.16699 5.5M4.66699 2.5H3.56699C2.72691 2.5 2.30687 2.5 1.98601 2.66349C1.70376 2.8073 1.47429 3.03677 1.33048 3.31901C1.16699 3.63988 1.16699 4.05992 1.16699 4.9V8.1C1.16699 8.94008 1.16699 9.36012 1.33048 9.68099C1.47429 9.96323 1.70376 10.1927 1.98601 10.3365C2.30687 10.5 2.72691 10.5 3.56699 10.5H6.76699C7.60707 10.5 8.02711 10.5 8.34798 10.3365C8.63022 10.1927 8.85969 9.96323 9.0035 9.68099C9.16699 9.36012 9.16699 8.94008 9.16699 8.1V7"
                                            stroke="#1890FF" stroke-width="1.4" stroke-linecap="round"
                                            stroke-linejoin="round"/>
                                    </svg>

                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="nestscale-center-justify" style="margin-top: 30px">
                        <div class="nestscale-center-align gap-16">
                            <svg width="6" height="11"
                                 style="cursor: pointer"
                                 @click="decreasePage"
                                 viewBox="0 0 6 11" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M4.83203 9.5L0.832031 5.5L4.83203 1.5" stroke="black" stroke-width="1.5"
                                      stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                            <div v-for="i in pageCountService"
                                 class="pagination"
                                 @click="currentPageService = i"
                                 :class="currentPageService === i ? 'selected': ''">
                                {{ i }}
                            </div>
                            <svg width="6" height="11"
                                 style="cursor: pointer"
                                 @click="nextPage()"
                                 viewBox="0 0 6 11" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M0.832031 9.5L4.83203 5.5L0.832031 1.5" stroke="black" stroke-width="1.5"
                                      stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </div>
                    </div>
                </div>
                <div class="na-card">
                    <div class="na-title" style="margin-bottom: 24px;">More resources</div>
                    <div class="na-resources-wrapper">
                        <div v-for="resource in resources" class="na-resource-item">
                            <div class="na-resource-item-icon">
                                <img :src="resource.icon">
                            </div>
                            <div class="na-resource-item-body">
                                <div class="na-resource-item-name" style="width: max-content;">
                                    <a :href="resource.url" class="na-app-item-link" target="_blank">
                                        <div class="na-flex-center-alight">
                                            <span>{{ resource.name }}</span>
                                            <svg width="12" height="12" viewBox="0 0 12 12" fill="none"
                                                 xmlns="http://www.w3.org/2000/svg">
                                                <g clip-path="url(#clip0_2432_64431)">
                                                    <path
                                                        d="M10.5 4.5L10.5 1.5M10.5 1.5H7.5M10.5 1.5L6.5 5.5M5 2.5H3.9C3.05992 2.5 2.63988 2.5 2.31901 2.66349C2.03677 2.8073 1.8073 3.03677 1.66349 3.31901C1.5 3.63988 1.5 4.05992 1.5 4.9V8.1C1.5 8.94008 1.5 9.36012 1.66349 9.68099C1.8073 9.96323 2.03677 10.1927 2.31901 10.3365C2.63988 10.5 3.05992 10.5 3.9 10.5H7.1C7.94008 10.5 8.36012 10.5 8.68099 10.3365C8.96323 10.1927 9.1927 9.96323 9.33651 9.68099C9.5 9.36012 9.5 8.94008 9.5 8.1V7"
                                                        stroke="#1890FF" stroke-width="1.4" stroke-linecap="round"
                                                        stroke-linejoin="round"/>
                                                </g>
                                                <defs>
                                                    <clipPath id="clip0_2432_64431">
                                                        <rect width="12" height="12" fill="white"/>
                                                    </clipPath>
                                                </defs>
                                            </svg>
                                        </div>
                                    </a>
                                </div>
                                <div class="na-resource-item-description">{{ resource.description }}</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <a v-if="current_app === 'nest_desk'" target="_blank" href="https://nestscale.com/blog/customer-service?utm_source=in_app&utm_medium=banner&utm_campaign=nestdesk" style="height: max-content;width: max-content;">
                <img class="nestscale-suggestion"
                     src="https://apps.nestscale.com/omnichat/static/img/NestDesk_banner.png">
            </a>
            <a v-if="current_app === 'nest_send'" target="_blank" href="https://nestscale.com/blog/email-marketing?utm_source=in_app&utm_medium=banner&utm_campaign=nestsend" style="height: max-content;width: max-content;">
                <img class="nestscale-suggestion"
                     src="https://apps.nestscale.com/omnichat/static/img/NestSend.png">
            </a>
            <a v-if="current_app === 'nest_widget'" target="_blank" href="https://nestscale.com/blog/tiktok-for-business?utm_source=in_app&utm_medium=banner&utm_campaign=nestwidget" style="height: max-content;width: max-content;">
                <img class="nestscale-suggestion"
                     src="https://apps.nestscale.com/omnichat/static/img/NestWidget.png">
            </a>
            <a v-if="current_app === 'nest_ads'" target="_blank" href="https://megadigital.ai/en/tiktok-agency-account/?utm_source=nestscale" style="height: max-content;width: max-content;">
                <img class="nestscale-suggestion"
                     src="https://apps.nestscale.com/omnichat/static/img/banner_mega_tiktok.png">
            </a>
        </div>
    </div>
</template>

<script>
import axios from "axios"

export default {
    name: "appSuggestion",
    components: {}, props: {
        current_app: {
            type: String,
            default: null
        }
    },
    data() {
        return {
            app_data: [],
            pageCountAppNestScale: 1,
            pageCountAppPartner: 1,
            pageCountService: 1,
            currentPageNestScale: 1,
            currentPagePartner: 1,
            currentPageService: 1,
            resources: [{
                name: 'Visit Help Center',
                description: 'All answers, tutorials and help articles you need. Make the most of NestScale Product Variants to enhance the shopping experience and drive store sales.',
                url: 'https://support.nestscale.com/nestscale-product-variants/?utm_source=in_app&utm_medium=resource&utm_campaign=nestscale_variants',
                icon: 'https://apps.nestscale.com/nestads/static/img/Help Center.png'
            }, {
                name: 'Join NestScale Community',
                description: 'Connect with us and other NestScale users to get the best insights and practices.',
                url: 'https://www.facebook.com/groups/1283074155552184',
                icon: 'https://apps.nestscale.com/nestads/static/img/NestAds Community.png'
            }, {
                name: 'Learning blog',
                description: 'Dive into valuable e-commerce insights to strategically grow your business and maximize your revenue.',
                url: 'https://nestscale.com/blog?utm_source=in_app&utm_medium=resource&utm_campaign=nestscale',
                icon: 'https://apps.nestscale.com/nestads/static/img/Resources.png'
            }, {
                name: 'NestScale YouTube channel',
                description: 'Find the latest online courses, actionable tutorials, best tips and tricks to grow and scale your business.',
                url: 'https://www.youtube.com/@nestscale',
                icon: 'https://apps.nestscale.com/nestads/static/img/Youtube Channel.png'
            }]
        }
    },
    watch: {},
    methods: {
        initData: function () {
            this.getListApp(this.current_app, this.currentPage)
        },
        getListApp: function (current_app, currentPage) {
            axios.post("https://apps.nestscale.com/sc/get_list_suggestion", {
                "jsonrpc": "2.0",
                "params": {
                    "app": current_app,
                    "offset": currentPage - 1
                }
            }).then(res => {
                let data = res.data.result
                if (data.status === "success") {
                    this.app_data = data.object_app
                    this.pageCountAppNestScale = Math.ceil(data.object_app.list_app_by_nestscale.length / 4);
                    this.pageCountAppPartner = Math.ceil(data.object_app.list_app.length / 4);
                    this.pageCountService = Math.ceil(data.object_app.list_services.length / 4);
                }
            }).catch(err => {
                console.error(err.message)
            })
        },
        decreasePage() {
            if (this.currentPage > 1) {
                this.currentPage--;
            }
        },
        nextPage() {
            if (this.currentPage < this.pageCount) {
                this.currentPage++;
            }
        },
        openLink: function (link) {
            window.open(link, '_blank')
        }
    }, computed: {
        tempAppNestScale: function () {
            let app_data = []
            if (this.app_data.list_app !== undefined) {
                app_data = [...this.app_data.list_app_by_nestscale].splice((this.currentPageNestScale - 1 ) * 4, 4)
            }
            return app_data
        },
        tempAppPartner: function () {
            let app_data = []
            if (this.app_data.list_app !== undefined) {
                app_data = [...this.app_data.list_app].splice((this.currentPagePartner - 1 ) * 4, 4)
            }
            return app_data
        },
        tempService: function () {
            let app_data = []
            if (this.app_data.list_app !== undefined) {
                app_data = [...this.app_data.list_services].splice((this.currentPageService - 1 ) * 4, 4)
            }
            return app_data
        }
    },
    async mounted() {
        this.initData()
    }
}
</script>

<style scoped>
.nestscale-center-align {
    display: flex;
    align-items: center;
}

.nestscale-center-justify {
    display: flex;
    justify-content: center;
}

.nestscale-start-justify {
    display: flex;
    justify-content: flex-start;
}

.flex-column {
    flex-direction: column;
}

.nestscale-block {
    background: #FCFCFC;
    border-radius: 6px;
}

.gap-4 {
    gap: 4px;
}

.gap-10 {
    gap: 10px;
}

.gap-16 {
    gap: 16px;
}

.gap-20 {
    gap: 20px;
}

.gap-24 {
    gap: 24px;
}

.pagination {
    border-radius: 4px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 5px;
    width: 23px;
    height: 23px;
    font-weight: 600;
    font-size: 13px;
    line-height: 19px;
    cursor: pointer;
}

.pagination.selected {
    background: #000000;
    color: white;
}

.na-title {
    font-weight: 700;
    font-size: 18px;
    line-height: 22px;
    margin-bottom: 12px;
}

.na-resources-wrapper {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    /*grid-template-rows: repeat(2, 1fr);*/
    grid-column-gap: 20px;
    grid-row-gap: 24px;
}

.na-resource-item {
    display: flex;
    align-items: flex-start;
    gap: 15px;
}

.na-resource-item-icon {
    background: #000000;
    border-radius: 4px;
    width: 32px;
    height: 32px;
    justify-content: center;
    align-items: center;
    display: flex;
}

.na-resource-item-name {
    margin-bottom: 4px;
    font-weight: 600;
    font-size: 14px;
    line-height: 20px;
    color: #1890FF;
}

.na-app-item-link {
    color: #3199FF;
    font-weight: 600;
    font-size: 14px;
    line-height: 22px;
}

.na-app-item-link > div {
    gap: 4px;
    display: flex;
    align-items: center;
}

.na-flex-center-alight {
    display: flex;
    align-items: center;
    /*justify-content: space-between;*/
}

.na-resource-item-description {
    font-weight: 400;
    font-size: 12px;
    line-height: 22px;
    color: #6B6B6B;
}

.na-card {
    padding: 20px;
    border-radius: 6px;
    background-color: #FCFCFC;
    border: none;
}

.nestscale-suggestion {
    border-radius: 8px;
    height: 100%;
}
</style>