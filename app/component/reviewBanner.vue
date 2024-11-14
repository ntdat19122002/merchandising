<template>
    <div class="pd-16 pd-l-20 pd-r-20 w100 nestscale-center-align nestscale-between-justify na-review-banner"
         v-if="isShowBanner"
         style="border-radius: 10px;border: 1px solid #3199FF;background: #E2F1FF;margin-bottom: 20px;">
        <div class="size-16 semibold" style="color:#1D1E21">
            Hi {{ username }}, let us know how we are doing by rating our app
        </div>
        <Rate v-model:value="rate" @change="rating"/>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"
             class="cur-pointer" @click="actionBanner('close')">
            <path d="M17 7L7 17M7 7L17 17" stroke="#636366" stroke-width="2" stroke-linecap="round"
                  stroke-linejoin="round"/>
        </svg>
    </div>
    <Modal v-model:visible="modal.internalReview" :footer="null" :width="580" v-if="isShowBanner"
           :cancel-button-props="{ style: {display: 'none'} }" :ok-button-props="{ style: {display: 'none'} }"
           centered :afterClose="()=>{this.rate=0}" class="na-modal-no-pd">
        <div class="w100 flex-column nestscale-center-justify nestscale-lower-align gap-20">
            <div class="flex-stretch nestscale-center-justify nestscale-center-align"
                 style="background: linear-gradient(180deg, #EDF8FF 0%, #DBDFFC 100%);border-radius: 10px 10px 0 0;">
                <img src="/app_base/static/img/Frame 427319490.png" alt="" class="w100"/>
            </div>
            <div class="flex-stretch flex-column nestscale-center-align gap-16" style="padding: 0 24px;">
                <div class="size-16 semibold c100" style="text-align: center">Your opinion matters a lot to our
                    development of the app 💖
                </div>
                <div class="flex-stretch flex-column nestscale-upper-align gap-6" style="height: 128px;">
                    <span>What else could we have done to improve our app?</span>
                    <textarea v-model="review" placeholder="Enter your answer here"
                              style="width: 100%;border-radius: 6px;height: 138px;padding: 11px 14px;resize: none;outline: none;border-color: #D1D1D1"></textarea>
                </div>
            </div>
            <div class="flex-stretch nestscale-end-justify" style="padding: 0 24px 24px 0;">
                <button class="nestscale-btn" @click="this.actionBanner('review')">Submit</button>
            </div>
        </div>
    </Modal>
</template>

<script>
import {Rate, Modal} from 'ant-design-vue'
import axios from "axios";

export default {
    name: "reviewBanner",
    components: {Rate, Modal},
    props: {
        username: {
            type: String,
        },
        currentWorkspace: {
            type: Number,
            default: 0
        },
        appCode: {
            type: String,
        },
    },
    data() {
        return {
            rate: 0,
            modal: {
                internalReview: false
            },
            review: null,
            isShowBanner: false,
            redirect: ''
        }
    },
    methods: {
        rating: function () {
            if (this.rate > 0) {
                if (this.rate < 4) {
                    this.modal.internalReview = true
                } else {
                    window.open(this.redirect, '_blank')
                    this.actionBanner('review')
                }
            }
        },
        actionBanner: async function (action) {
            let params = {
                wpid: this.currentWorkspace,
                ac: this.appCode,
                referer: window.location.href
            }
            if (action === 'review') {
                params.star = this.rate
                params.review = this.review
            }
            await axios.post('/nestscale/review_banner/' + action, {
                jsonrpc: "2.0",
                params: params
            }).then((response) => {
                let data = response.data.result
                this.isShowBanner = data.show
                if (data.redirect) {
                    this.redirect = data.redirect
                }
                if (data.error) {
                    console.log(data.error)
                }
            }).catch((error) => {
                console.log(error)
            })
        },
    },
    async mounted() {
        await this.actionBanner('check')
    }
}
</script>

<style>
.pd-16 {
    padding: 16px;
}

.pd-l-20 {
    padding-left: 20px;
}

.pd-r-20 {
    padding-right: 20px;
}

.w100 {
    width: 100%;
}

.nestscale-upper-align {
    display: flex;
    align-items: flex-start;
}

.nestscale-center-align {
    display: flex;
    align-items: center;
}

.nestscale-lower-align {
    display: flex;
    align-items: flex-end;
}

.nestscale-center-justify {
    display: flex;
    justify-content: center;
}

.nestscale-between-justify {
    display: flex;
    justify-content: space-between;
}

.nestscale-end-justify {
    display: flex;
    justify-content: flex-end;
}

.gap-20 {
    gap: 20px;
}

.na-review-banner .ant-rate-star-first, .na-review-banner .ant-rate-star-second {
    color: #d1d1d1;
}

.size-16 {
    font-size: 16px;
}

.semibold {
    font-weight: 600;
}

.cur-pointer {
    cursor: pointer;
}

.na-modal-no-pd .ant-modal-body {
    padding: 0;
}

.flex-column {
    flex-direction: column;
}

.flex-stretch {
    align-items: stretch;
}

.gap-16 {
    gap: 16px;
}

.gap-6 {
    gap: 6px;
}

.c100 {
    color: #1C1C1E;
}

.nestscale-btn,
.nestscale-btn.ant-btn,
.nestscale-btn.ant-btn:hover {
    background: #1C1C1E;
    border-radius: 6px;
    padding: 8px 16px 10px;
    align-items: center;
    display: flex;
    cursor: pointer;
    color: #FDFDFD;
    font-weight: 600;
    font-size: 14px;
    line-height: 20px;
    border: none;
    height: unset;
}

</style>