<template>
    <div class="">
        <div class="section">
            <div class="space-between">
                <h2 class="">
                    Judge.me setting
                </h2>
                <button @click="syncData">Sync data</button>
            </div>

            <div class="margin-y-10">
                <label for="">Public API token</label>
                <input type="text" id="" name="" v-model="judgeme.publicApiToken" />
            </div>
            <div class="margin-y-10">
                <label for="">Private API token</label>
                <input type="text" id="" name="" v-model="judgeme.privateApiToken" />
            </div>
            <button @click="saveJudgemeToken">Save</button>
        </div>

    </div>
</template>

<script>
import axios from "axios";
import {notification} from "ant-design-vue";

export default {
    name: "Review.vue",
    data() {
        return {
            judgeme: {
                publicApiToken: null,
                privateApiToken: null,
            },
        };
    },
    methods: {
        saveJudgemeToken() {
            axios.post('/judgeme/token', {
                jsonrpc: 2.0,
                params: {
                    public_api_token: this.judgeme.publicApiToken,
                    private_api_token: this.judgeme.privateApiToken,
                    store_url: window.md_settings.store_url,
                }
            })
               .then((response) => {
                    notification['success']({
                        message: 'Judgeme',
                        description:
                          'Token have been saved',
                        placement:'bottomRight',
                      });
                })
               .catch((error) => {
                    console.error(error);
                });
        },
        syncData() {
            axios.post('/judgeme/reviews/products', {
                jsonrpc: 2.0,
                params: {
                    store_url: window.md_settings.store_url,
                }
            })
               .then((response) => {
                    notification['success']({
                        message: 'Judgeme',
                        description:
                          'Sync data successfully',
                        placement:'bottomRight',
                      });
                })
               .catch((error) => {
                    console.error(error);
                });
        }
    },
    mounted() {
        axios.get('/judgeme/token',{
            params: {
                store_url: window.md_settings.store_url,
            }
        })
            .then((response) => {
                 this.judgeme.publicApiToken = response.data.public_api_token;
                 this.judgeme.privateApiToken = response.data.private_api_token;

            })
    }
}
</script>

<style scoped>
    label{
        margin-right: 20px;
    }
</style>