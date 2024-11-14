import {createApp, h} from 'vue/dist/vue.esm-bundler'
import Shopify from './Shopify.vue'
import '../static/css/shopify_store.css'
import axios from "axios"
import Collection from "./component/collection.vue";
import ShopifyProductGroup from "./ShopifyProductGroup.vue";


function insertAfterNode(newNode, referenceNode, parentNode) {
    if (referenceNode.nextSibling) {
        parentNode.insertBefore(newNode, referenceNode.nextSibling);
    } else {
        parentNode.insertBefore.appendChild(newNode);
    }
}

if (window.location.href.includes('products')) {
    let block_element_selector = '.product-variants.variant-swatch.swatches-circle,.product__variants-select.no-js-hidden,.product__block__variants'
    let block_element = document.querySelector(block_element_selector)
    if (!block_element) {
        block_element_selector = 'variant-radios,product-variants,variant-selects,variant-picker,.variantPickerWrap.noJs,.type_variant_picker,.type-variant_picker,fieldset.variant-picker,.product-details__options' +
            ',.selector-wrapper.product-category,div[data-name="options"],.product-swatches,.product-options,.product__variants-swatches,.swatch-options,.swatch_options' +
            ',.variant_picker,sht-variant-radios,sht-variant-selects,.product-options,.product__selector,.yv-main-product-detail.slider-product-detail' +
            ',.product-block[data-dynamic-variants-enabled],options-selection,.t4s-swatch,.product__form-block--swatches, .product-option-selector-box,.product__selectors,.product__controls-group,.ProductForm__Variants,.option-selectors,.product-variant-option'
    }
    block_element = document.querySelector(block_element_selector)
// add to conflict theme database
    if (!block_element) {
        block_element_selector = "#product-variants,form[action='/cart/add'],.product-detail__form__options--underlined" +
            ",.product__form-block.product__form-block--swatches,.form-vertical,.product-form.product-form--payment-button" +
            ",.selector-wrapper.selector-wrapper--fullwidth.js"
    }
    block_element = document.querySelector(block_element_selector)
    let option_block_selector = ".product-variant,.product-form__input.product-form__input--pills,.product-form__input.product-form__input--dropdown,.product-option-row,.form-field-swatch" +
        ",.variant-field,.item.product-option,.productSectionContainer.containerCorners,.product-option,.inline-field-wrapper,.product-options__option.dropdown" +
        ",.product-form__inpt.product-form__input--dropdown,.swatches__container.js-variant-selector,.variant-picker__dropdown,.selector-wrapper.js-required" +
        ",.selector-wrapper.variant-wrapper.js,.variant-wrapper,product-option-picker,.select-input.select-input--bordered.product-selector__dropdown" +
        ",.product__variants-radio,.product-option-selector,.product-details__option-wrapper,.product-options__default-options,.product-options__swatch" +
        ",.ProductForm__Option.ProductForm__Option--labelled,.t4s-swatch__option,.m-product-option,.selector-wrapper,.option-selector,.product-form__item"
    let option_blocks
    if (block_element) {
        option_blocks = block_element.querySelectorAll(option_block_selector)
        if (!option_blocks.length) {
            option_block_selector = "fieldset"
            option_blocks = block_element.querySelectorAll(option_block_selector)
        }
        if (!option_blocks.length) {
            option_block_selector = ".swatch"
            option_blocks = block_element.querySelectorAll(option_block_selector)
        }
        if (!option_blocks.length) {
            option_block_selector = ".mb-3.md\\:mb-4"
            option_blocks = block_element.querySelectorAll(option_block_selector)
        }
        // add to conflict theme database
        if (!option_blocks.length) {
            option_block_selector = ".radio__fieldset--swatches,.swatch.clearfix,.variant-wrapper--button,.option-selectors,.product-form__option-selector" +
                ",.variant-wrapper.variant-wrapper--boxes,.product-form__option,.maxus-productdetail__options,.ProductForm__Option,.selector-wrapper.product-form__item" +
                ",.selector-wrapper,.radio__fieldset,.product-option-item,.grid__item.product-form__item,.product__option,.product-form__input--swatches"
            option_blocks = block_element.querySelectorAll(option_block_selector)
        }
    }
    if (option_blocks) {
        if (option_blocks.length === 1) {
            if (option_blocks[0].style.display.includes("none") && option_blocks[0].innerHTML.includes("Default Title")) {
                option_blocks = null;
            } else {
                option_blocks[0].style.setProperty('display', 'none', 'important');
            }
        } else {
            option_blocks.forEach(option => option.style.setProperty('display', 'none', 'important'));
        }
    }
    let themeData = {}
    let isConflictTheme = false
    let wrapper_variant = document.createElement('div')
    wrapper_variant.id = "nestscale-product-variant"
    if (!block_element || !option_blocks.length) {
        await axios.post('/apps/nestscale_product_variant/check_conflict_theme', {
            jsonrpc: 2, params: {
                store_url: window.Shopify.shop,
                store_theme: window.Shopify.theme.name
            }
        }).then(res => {
            if (res.data.result.code == 1 && res.data.result.is_conflict) {
                isConflictTheme = true
                themeData = res.data.result.theme_data
                block_element = document.querySelector(themeData.parent_type_value)
            }
        }).catch(error => {
            console.log(error)
        })
    }
// Find block of conflix theme so not use else
    if (block_element) {
        try {
            if (nestvariant_display_setting_swatch === 'below') {
                insertAfterNode(wrapper_variant, block_element, block_element.parentElement);
            } else {
                block_element.parentElement.insertBefore(wrapper_variant, block_element);
            }
        } catch (err) {
            block_element.parentElement.insertBefore(wrapper_variant, block_element);
        }

        createApp({
            name: "ShopifyProductVariant",
            render: () => {
                return h(Shopify, {
                    data: {
                        block_element_selector: block_element_selector,
                        option_block_selector: option_block_selector,
                        isConflictTheme: isConflictTheme,
                        themeData: themeData
                    }
                })
            }
        }).mount("#nestscale-product-variant")
    }


    let product_group_container = document.getElementById('nestvariant-product-group')
    if (product_group_container) {
        createApp({
            name: "ShopifyProductVariantProductGroup",
            render: () => {
                return h(ShopifyProductGroup, {
                    data: {}
                })
            }
        }).mount(product_group_container)
    }
}


if (nestvariant_theme_settings_value !== null) {

    !async function () {
        let card_product_object = {
                productCards: [],
                collectionContainers: [],
                urlObserver: null,
                async init() {
                    if (card_product_object.collectionContainers.length > 0 && card_product_object.collectionContainers.forEach(e => {
                            e.remove()
                        }
                    ),
                        card_product_object.productCards = await card_product_object.getProductCards(),
                    0 === card_product_object.productCards.length) {
                        console.log("Products card not found!");
                        return
                    }
                    card_product_object.createOptionMarkup()
                },

                async getProductCards() {

                    for (let productCardSelector of utility_function.productCardSelector) {
                        let product_info = await card_product_object.searchProductCards(productCardSelector);
                        if (product_info.length > 0)
                            return product_info
                    }
                    await utility_function.sleep(2e3)

                    return []
                },
                createOptionMarkup() {

                    card_product_object.productCards.forEach((card_product, index) => {


                        // Find the target element where the Vue app should be mounted
                        let targetElement = card_product.element.querySelector(card_product.targetSelector);
                        if (!targetElement) {
                            // If the target element is not found, loop over productCardSelector to find a match
                            for (let S of utility_function.productCardSelector) {
                                targetElement = card_product.element.querySelector(S.targetSelector);
                                if (targetElement) break;
                            }
                        }
                        let filteredArray = []
                        try {
                            filteredArray = nestvariant_theme_settings_value.list_option_setting.filter(item =>
                                card_product.product.options.some(option => option.name === item.name)
                            );
                        } catch (e) {

                        }
                        let pv_data = []
                        filteredArray.forEach(item => {
                            if (item.hasOwnProperty('option_setting_color_custom_image')) {
                                pv_data.push({
                                    "design_setting": item.display_type_collection_page,
                                    "option_setting": item,
                                    "option_setting_color_custom_image": item.option_setting_color_custom_image
                                })
                            } else {
                                pv_data.push({
                                    "design_setting": item.display_type_collection_page,
                                    "option_setting": item,
                                })
                            }
                        })
                        if (targetElement) {
                            let mountPoint = document.createElement('div');
                            mountPoint.setAttribute('id', 'product_variant');
                            card_product.element.classList.add('product_variant-card-' + index)
                            // Depending on the 'append' property, append or replace the target element with the Vue app
                            switch (card_product.append) {
                                case "parent":
                                    targetElement.parentElement.appendChild(mountPoint);
                                    break;
                                case "self":
                                    targetElement.appendChild(mountPoint);
                                    break;
                                case "before":
                                    targetElement.parentNode.insertBefore(mountPoint, targetElement);
                                    break;
                                case "replace":
                                    targetElement.parentNode.replaceChild(mountPoint, targetElement)
                            }

                            createApp({
                                name: 'collection',
                                render: () => {
                                    return h(Collection, {
                                        data: {
                                            pv_data: pv_data,
                                            card_product_info: card_product,
                                            card_index: index
                                        }
                                    });
                                }
                            }).mount(mountPoint);
                        }
                    });
                },

                async searchProductCards(e) {
                    let t = []
                        , o = document.querySelectorAll(e.cardSelector);
                    if (o.length > 0)
                        for (let l of o) {
                            let a = l.querySelector("[href*='/products']")
                                , i = a?.href.substring(a.href.lastIndexOf("/")).replace("/", "").split("?")[0];

                            let object = {
                                url: `${location.origin}/products/${i}.js`,
                                element: l,
                                targetSelector: e.targetSelector,
                                append: e.append,
                            }
                            if (e.hasOwnProperty('hide_variant')) {
                                let hide_elements = document.querySelectorAll(e['hide_variant'])
                                hide_elements.forEach(element => {
                                    element.style.display = 'none'
                                })
                            }
                            t.push(object)
                        }
                    if (t.length > 0) {
                        card_product_object.urlObserver && card_product_object.urlObserver.disconnect();
                        let r = window.location.href;
                        card_product_object.urlObserver = new MutationObserver(function (e) {
                                !window.location.search.includes('variant') && window.location.href !== r && (r = window.location.href,
                                    card_product_object.productCards = [],
                                    setTimeout(() => {
                                            card_product_object.init()
                                        }
                                        , 1e3))
                            }
                        ),
                            card_product_object.urlObserver.observe(document, {
                                subtree: !0,
                                childList: !0
                            });
                        let n = await Promise.allSettled(t.map(e => fetch(e.url).then(e => e.json())));
                        return t.map((e, t) => ({
                            ...e,
                            product: n[t].value
                        }))
                    }
                    console.log(t,e,n)
                    return []
                },

            },

            utility_function = {
                sleep: async function (e) {
                    return new Promise(t => setTimeout(t, e))
                },
                selectors: ["variant-radios", "variant-selects", ".t4s-swatch", ".product-form.product-form-product-template .product-form__controls-group", ".product-info__block-item[data-block-type='variant-picker']", ".product-info .product-info__variant-picker", ".input-row .option-selectors", "variant-selection", ".product__form__outer .product__selectors", ".product-info__block.product-options", ".product__block__variants", ".product-detail__form .product-detail__form__options", ".main-product__block.main-product__block-variant_picker", "product-variants[class='product-form__variants']", ".product-form .product-form__variants", ".shopify-product-form .product-form-block", ".product-details .option-selectors", ".product-layout-grid__detail .product-detail__options", ".product__form .product__selectors", ".product-text product-variants", ".product-block-container .product-block.product-block-variant-picker", ".product-page--info .product-page--block", ".product__content .product__selector", ".product__section-details .product__form-container", ".shopify-product-form .product-swatches", ".product__section-details .product__section-details__inner .product_form", ".f8pr .f8pr-variant-selection", ".product-info-wrapper .variants-container", ".product-grid__detail .product-form-block.product-options", ".product-details.grid__item .product-form-block.product-options", "product-form[data-name='main-product-form'] .no-js-hide", ".product__meta .product__controls-group.product__variants-wrapper", ".product-form .product_swatches", ".product__info-wrapper .product__info .product-variant-picker", "[class='#product-meta'] product-variant-selector", ".shopify-product-form .swatch_options", ".grid__wrapper .product-blocks .product-blocks__block.product-blocks__block--variant_picker", ".shopify-product-form .options", ".site-box-content product-variants", ".product__section-content .product__section-content__block.product__section-content__block--variant_picker", ".product__details .product__meta .product__controls-group", ".main-product__blocks .main-product__block-variant-picker", "#product-form.shopify-product-form .swatch-options", ".product__form .product__form-block.product__form-block--swatches", ".product__info .product__variants--radios", ".product__detail-content .product-option-selector-box", ".product .product-form .product-options", "form .tab-body .clearfix", ".product-content div[data-product-form-variant-container]", ".product-details .product-contents .product-details__options", "product-variant-selector", ".product-form-content-wrapper .product__form .product-options", "#product-description .product-form__variants.product__section--variants", ".product .product__grid-top .product-options", "div[data-product-form-container] div[data-product-form-variant-container]", ".product-info.product-form .productoptions", ".product-form .product-form__inner .product-form__controls-group--options", ".main-product__details-wrapper .main-product__selector", ".f-product-single__blocks .f-product-single__block--variant_picker", "product-variants", "selector-wrapper product-category form-group", "product-info__product-picker", ".product-block[data-dynamic-variants-enabled]", ".page-content--product .product-single__meta [data-product-blocks] .product-block",],
                clickSelectors: "[name='nameField'][value='valueField'],[name='optionPosition'][value='valueField'],input[data-value='valueField'],[id='optionPosition'][value='valueField'],[data-value='valueField']",
                assignValueSelectors: "option[value='valueField']",
                productCardSelector: [{
                    cardSelector: ".product-grid .grid__item",
                    targetSelector: "h3[class*='card__heading'][id*='title']",
                    append: "parent"
                }, {
                    cardSelector: ".collection__main .product-list .product-card",
                    targetSelector: ".product-card__info .price-list",
                    append: "parent"
                }, {
                    cardSelector: ".collection-grid__wrapper .grid .grid__item",
                    targetSelector: ".grid-product__content .grid__item-image-wrapper",
                    append: "parent"
                }, {
                    cardSelector: ".collection__results .product-list .product-card",
                    targetSelector: ".product-card__info .product-card__title",
                    append: "parent"
                }, {
                    cardSelector: ".collection-listing .product-list .product-block",
                    targetSelector: ".product-info .innerer .product-link",
                    append: "parent"
                }, {
                    cardSelector: ".grid .grid-item.product-item",
                    targetSelector: ".product-item__info .product-link",
                    append: "parent"
                }, {
                    cardSelector: ".productgrid--items .productgrid--item",
                    targetSelector: ".productitem--info .productitem--title",
                    append: "parent"
                }, {
                    cardSelector: ".grid .card.card--product",
                    targetSelector: ".card__info .card__title",
                    append: "parent"
                }, {
                    cardSelector: ".collection .product-grid .grid__item",
                    targetSelector: ".card-wrapper",
                    append: "self",

                }, {
                    cardSelector: ".collection__products product-grid-item",
                    targetSelector: ".product__grid__info",
                    append: "self"
                }, {
                    cardSelector: ".grid .grid__item.grid-product",
                    targetSelector: ".grid-product__meta",
                    append: "self"
                }, {
                    cardSelector: ".product-list.product-list--collection .product-item",
                    targetSelector: ".product-item__info-inner",
                    append: "self"
                }, {
                    cardSelector: ".collection__products .product-item,.search__results .product-item",
                    targetSelector: ".product-item__text",
                    append: "self"
                }, {
                    cardSelector: ".product-list .product-list__inner .product-item",
                    targetSelector: ".product-item-meta",
                    append: "self"
                }, {
                    cardSelector: ".product-grid .grid-item.grid-product",
                    targetSelector: ".grid-item__meta",
                    append: "self"
                }, {
                    cardSelector: "#product-grid .product-card",
                    targetSelector: ".product-card-info",
                    append: "self"
                }, {
                    cardSelector: "#CollectionProductGrid .product-item,#recently-viewed-products-list-2 .product",
                    targetSelector: ".product-item__price,.card-information__wrapper",
                    append: "self"
                }, {
                    cardSelector: ".grid .product-grid-item.grid__item",
                    targetSelector: ".product-grid-item__info-content",
                    append: "self"
                }, {
                    cardSelector: ".products.collection .product-card",
                    targetSelector: ".product-card-info",
                    append: "self"
                }, {
                    cardSelector: "[data-collection-products] [data-product-grid]",
                    targetSelector: ".yv-product-information",
                    append: "self"
                }, {
                    cardSelector: ".collection-main-body .grid__item",
                    targetSelector: ".product-grid--price",
                    append: "self"
                }, {
                    cardSelector: ".product-list￼-container .product-list .product-block",
                    targetSelector: ".product-block__inner .image",
                    append: "self"
                }, {
                    cardSelector: ".cc-filters-results .grid-flex .product-block",
                    targetSelector: ".product-block__image-container",
                    append: "self"
                }, {
                    cardSelector: ".collection-products .collection__cards .product-card",
                    targetSelector: ".product-card__details",
                    append: "self"
                }, {
                    cardSelector: ".collection.grid .product-item__wrapper",
                    targetSelector: ".product-item__wrapper",
                    append: "self"
                }, {
                    cardSelector: ".grid__item.product-grid li",
                    targetSelector: ".hp-subtitle",
                    append: "parent"
                }, {
                    cardSelector: ".results.collection-products .collection-product",
                    targetSelector: ".product-card__info",
                    append: "parent"
                }, {
                    cardSelector: ".product-grid.grid-bs li",
                    targetSelector: ".card-information__wrapper",
                    append: "parent"
                }, {
                    cardSelector: "#product-grid li",
                    targetSelector: ".card_info",
                    append: "parent"
                }, {
                    cardSelector: ".product-grid .grid__item",
                    targetSelector: ".product-card-item__colors",
                    append: "parent"
                }, {
                    cardSelector: "#product-grid .shop-block",
                    targetSelector: ".title-of-product",
                    append: "parent"
                }, {
                    cardSelector: "#main-collection-products li",
                    targetSelector: ".item-price.item-price--no-label",
                    append: "parent"
                }, {
                    cardSelector: ".row.products-on-page .collection-toggle",
                    targetSelector: ".product-thumb",
                    append: "parent"
                }, {
                    cardSelector: ".products.js-product-grid .clm",
                    targetSelector: ".card__content",
                    append: "parent"
                }, {
                    cardSelector: ".products.slider li",
                    targetSelector: ".item-details-wrapper",
                    append: "parent"
                }, {
                    cardSelector: "#collection li",
                    targetSelector: ".text-start",
                    append: "parent"
                }, {
                    cardSelector: "#CollectionLoop .grid-item.product-item",
                    targetSelector: ".product-item__info",
                    append: "parent"
                }, {
                    cardSelector: "#main-collection-product-grid product-card",
                    targetSelector: ".product-card_price_action",
                    append: "parent"
                }, {
                    cardSelector: "#main-collection-product-grid li",
                    targetSelector: ".card-information__wrapper",
                    append: "self"
                }, {
                    cardSelector: ".collection-products article",
                    targetSelector: ".product-list-item-details",
                    append: "parent"
                }, {
                    cardSelector: ".collection-grid__row .product-block",
                    targetSelector: ".product-block__info",
                    append: "parent"
                }, {
                    cardSelector: ".t4s-product-wrapper",
                    targetSelector: ".t4s-product-title",
                    append: "self"
                }, {
                    cardSelector: ".col-xs-12.col-md-3.single__pro.col-sm-6",
                    targetSelector: ".product__details",
                    append: "self"
                }, {
                    cardSelector: ".product-grid .product-block",
                    targetSelector: ".product-block__detail.align-ltr-left .inner .innerer",
                    append: "parent",
                    hide_variant: '.product-block-options__inner'
                }]
            };
        if (window.location.href.includes("products")) {
            setTimeout(function () {
                card_product_object.init();
            }, 2250);
        } else {
            card_product_object.init();
        }
    }();
}