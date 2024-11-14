<template>
    <div v-if="isShowWebinar" class="na-tiktok-course-modal">
        <a :href="this.bannerUrl"
           target="_blank" @click="closeCourseModal">
            <img :src="this.bannerImg" alt="">
        </a>
        <div class="na-tiktok-course-close" @click="closeCourseModal"/>
    </div>
</template>
<script>
import axios from "axios"

export default {
    name: "webinarBanner",
    data() {
        return {
            isShowWebinar: true,
            bannerId: null,
            bannerImg: null,
            bannerUrl: null
        }
    },
    methods: {
        closeCourseModal: function () {
            this.isShowWebinar = false
            if (this.bannerId) localStorage.setItem("hide_webinar", this.bannerId.toString())
        },
        getWebinar: async function () {
            await axios.post('https://apps.nestscale.com/nestscale/webinar_banner/check', {
                jsonrpc: 2, params: {referer: window.location.href}
            }).then(response => {
                let data = response.data.result
                if (data.message === 'OK') {
                    this.bannerId = data.data.id
                    this.bannerImg = data.data.image
                    this.bannerUrl = data.data.url
                }
                if (data.error) {
                    console.log(data.error)
                }
            }).catch((error) => {
                console.log(error)
            })
        }
    },
    async mounted() {
        await this.getWebinar()
        if (this.bannerId && localStorage.getItem("hide_webinar") === (this.bannerId).toString()) {
            this.isShowWebinar = false
        }
    }
}
</script>
<style>
.na-tiktok-course-modal {
    position: fixed;
    bottom: 25px;
    right: 25px;
    z-index: 9999999;
    cursor: pointer;
    border-radius: 8px;
}

.na-tiktok-course-close {
    position: absolute;
    top: 14px;
    right: 14px;
    width: 32px;
    height: 32px;
    z-index: 9999999;
}

.na-tiktok-course-close:empty {
    display: block;
}
</style>