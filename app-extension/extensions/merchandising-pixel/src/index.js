import {register} from "@shopify/web-pixels-extension";
import axios from "axios";

register(({analytics, browser, init, settings}) => {
    analytics_page_viewed(analytics)
    analytics_product_viewed(analytics)
    analytics_product_added_to_cart(analytics)
    analytics_cart_viewed(analytics)
    analytics_checkout_started(analytics)
    analytics_checkout_completed(analytics)
    // analytics_alert_displayed(analytics)
    // analytics_checkout_address_info_submitted(analytics)
    // analytics_checkout_contact_info_submitted(analytics)
    // analytics_checkout_shipping_info_submitted(analytics)
    // analytics_collection_viewed(analytics)
    // analytics_payment_info_submitted(analytics)
    // analytics_product_removed_from_cart(analytics)
    // analytics_search_submitted(analytics)
    // analytics_ui_extension_errored(analytics)
});


function analytics_page_viewed(analytics) {
    analytics.subscribe('page_viewed', (event) => {
        console.log('Page viewed12', event);
        axios.get('https://odoo.website/pixel/events/page_viewed', {
            params: {
                store_url: event.context.document.location.host,
                client_id: event.clientId,
                event: event.name,
            }
        })
    });
}

function analytics_product_viewed(analytics) {
    analytics.subscribe('product_viewed', (event) => {
        console.log('Product viewed', event)
        const productPrice = event.data.productVariant.price.amount;

        const productTitle = event.data.productVariant.title;

        const payload = {
            event_name: event.name,
            event_data: {
                productPrice: productPrice,
                productTitle: productTitle,
            },
        };

        // Example for sending event to third party servers
        axios.get('https://odoo.website/pixel/events/product_viewed', {
            params: {
                store_url: event.context.document.location.host,
                client_id: event.clientId,
                event: event.name,
            }
        })
    });
}

function analytics_product_added_to_cart(analytics) {
    analytics.subscribe('product_added_to_cart', (event) => {
        console.log('Added to cart', event)
        const cartLine = event.data.cartLine;

        const cartLineCost = cartLine.cost.totalAmount.amount;

        const cartLineCostCurrency = cartLine.cost.totalAmount.currencyCode;

        const merchandiseVariantTitle = cartLine.merchandise.title;

        const payload = {
            event_name: event.name,
            event_data: {
                cartLineCost: cartLineCost,
                cartLineCostCurrency: cartLineCostCurrency,
                merchandiseVariantTitle: merchandiseVariantTitle,
            },
        };

        // Example for sending event to third party servers
        axios.get('https://odoo.website/pixel/events/product_added_to_cart', {
            params: {
                store_url: event.context.document.location.host,
                client_id: event.clientId,
                event: event.name,
            }
        })
    });
}

function analytics_cart_viewed(analytics) {
    analytics.subscribe('cart_viewed', (event) => {
        console.log('Cart viewed1', event);
        // Example for accessing event data

        const totalCartCost = event.data.cart.cost.totalAmount.amount;

        const firstCartLineItemName =
            event.data.cart.lines[0]?.merchandise.product.title;

        const payload = {
            event_name: event.name,
            event_data: {
                cartCost: totalCartCost,
                firstCartItemName: firstCartLineItemName,
            },
        };

        // Example for sending event data to third party servers
        axios.get('https://odoo.website/pixel/events/cart_viewed', {
            params: {
                store_url: event.context.document.location.host,
                client_id: event.clientId,
                event: event.name,
            }
        })
    });
}

function analytics_checkout_started(analytics) {
    analytics.subscribe('checkout_started', (event) => {
        console.log('Checkout started', event)
        const checkout = event.data.checkout;

        const checkoutTotalPrice = checkout.totalPrice?.amount;

        const allDiscountCodes = checkout.discountApplications.map((discount) => {
            if (discount.type === 'DISCOUNT_CODE') {
                return discount.title;
            }
        });

        const firstItem = checkout.lineItems[0];

        const firstItemDiscountedValue = firstItem.discountAllocations[0]?.amount;

        const customItemPayload = {
            quantity: firstItem.quantity,
            title: firstItem.title,
            discount: firstItemDiscountedValue,
        };

        const payload = {
            event_name: event.name,
            event_data: {
                totalPrice: checkoutTotalPrice,
                discountCodesUsed: allDiscountCodes,
                firstItem: customItemPayload,
            },
        };

        // Example for sending event data to third party servers
        axios.get('https://odoo.website/pixel/events/checkout_started', {
            params: {
                store_url: event.context.document.location.host,
                client_id: event.clientId,
                event: event.name,
            }
        })
    });
}

function analytics_checkout_completed(analytics) {
    analytics.subscribe('checkout_completed', (event) => {
        console.log('Checkout completed', event)
        const checkout = event.data.checkout;

        const checkoutTotalPrice = checkout.totalPrice?.amount;

        const allDiscountCodes = checkout.discountApplications.map((discount) => {
            if (discount.type === 'DISCOUNT_CODE') {
                return discount.title;
            }
        });

        const firstItem = checkout.lineItems[0];

        const firstItemDiscountedValue = firstItem.discountAllocations[0]?.amount;

        const customItemPayload = {
            quantity: firstItem.quantity,
            title: firstItem.title,
            discount: firstItemDiscountedValue,
        };

        const paymentTransactions = event.data.checkout.transactions.map((transaction) => {
            return {
                paymentGateway: transaction.gateway,
                amount: transaction.amount,
            };
        });

        const payload = {
            event_name: event.name,
            event_data: {
                totalPrice: checkoutTotalPrice,
                discountCodesUsed: allDiscountCodes,
                firstItem: customItemPayload,
                paymentTransactions: paymentTransactions,
            },
        };

        // Example for sending event data to third party servers
        axios.get('https://odoo.website/pixel/events/checkout_completed', {
            params: {
                store_url: event.context.document.location.host,
                client_id: event.clientId,
                event: event.name,
            }
        })
    });
}

function analytics_ui_extension_errored(analytics) {
    analytics.subscribe('ui_extension_errored', (event) => {
        console.log('Analytics ui extension errored', event)
        const {apiVersion, appId, appName, appVersion, trace} = event.data.alert;

        const payload = {
            event_name: event.name,
            event_data: {
                apiVersion,
                appId,
                appName,
                appVersion,
                trace,
            },
        };

        // Example for sending event data to third party servers
        fetch('https://example.com/pixel', {
            method: 'POST',
            body: JSON.stringify(payload),
            keepalive: true,
        });
    });
}

function analytics_search_submitted(analytics) {
    analytics.subscribe('search_submitted', (event) => {
        console.log('Search submitted', event)
        const searchResult = event.data.searchResult;

        const searchQuery = searchResult.query;

        const firstProductReturnedFromSearch =
            searchResult.productVariants[0]?.product.title;

        const payload = {
            event_name: event.name,
            event_data: {
                searchQuery: searchQuery,
                firstProductTitle: firstProductReturnedFromSearch,
            },
        };

        // Example for sending event to third party servers
        fetch('https://example.com/pixel', {
            method: 'POST',
            body: JSON.stringify(payload),
            keepalive: true,
        });
    });
}

function analytics_product_removed_from_cart(analytics) {
    analytics.subscribe('product_removed_from_cart', (event) => {
        console.log('Product removed from cart', event)
        const cartLine = event.data.cartLine;

        const cartLineCost = cartLine.cost.totalAmount.amount;

        const cartLineCostCurrency = cartLine.cost.totalAmount.currencyCode;

        const merchandiseVariantTitle = cartLine.merchandise.title;

        const payload = {
            event_name: event.name,
            event_data: {
                cartLineCost: cartLineCost,
                cartLineCostCurrency: cartLineCostCurrency,
                merchandiseVariantTitle: merchandiseVariantTitle,
            },
        };

        // Example for sending event to third party servers
        fetch('https://example.com/pixel', {
            method: 'POST',
            body: JSON.stringify(payload),
            keepalive: true,
        });
    });
}

function analytics_payment_info_submitted(analytics) {
    analytics.subscribe('payment_info_submitted', (event) => {
        console.log('Payment info submitted', event)
        const checkout = event.data.checkout;

        const checkoutTotalPrice = checkout.totalPrice?.amount;

        const firstDiscountType = checkout.discountApplications[0]?.type;

        const discountCode =
            firstDiscountType === 'DISCOUNT_CODE'
                ? checkout.discountApplications[0]?.title
                : null;

        const payload = {
            event_name: event.name,
            event_data: {
                totalPrice: checkoutTotalPrice,
                firstDiscountCode: discountCode,
            },
        };

    });
}

function analytics_collection_viewed(analytics) {
    analytics.subscribe('collection_viewed', (event) => {
        console.log('Collection viewed', event)
        const collection = event.data.collection;

        const collectionTitle = collection.title;

        const priceOfFirstProductInCollection =
            collection.productVariants[0]?.price.amount;

        const payload = {
            event_name: event.name,
            event_data: {
                collectionTitle: collectionTitle,
                priceFirstItem: priceOfFirstProductInCollection,
            },
        };

        // Example for sending event to third party servers
        fetch('https://example.com/pixel', {
            method: 'POST',
            body: JSON.stringify(payload),
            keepalive: true,
        });
    });
}

function analytics_checkout_shipping_info_submitted(analytics) {
    analytics.subscribe('checkout_shipping_info_submitted', (event) => {
        console.log('Checkout shipping info submitted', event)
        const checkout = event.data.checkout;
        const shippingLine = checkout.shippingLine;

        const price = shippingLine.price.amount;
        const currency = shippingLine.price.currencyCode;

        const payload = {
            event_name: event.name,
            event_data: {
                price: price,
                currency: currency,
            },
        };

        // Example for sending event to third party servers
        fetch('https://example.com/pixel', {
            method: 'POST',
            body: JSON.stringify(payload),
            keepalive: true,
        });
    });
}

function analytics_checkout_contact_info_submitted(analytics) {
    analytics.subscribe('checkout_contact_info_submitted', (event) => {
        console.log('Checkout contact info submitted', event)
        const checkout = event.data.checkout;

        const email = checkout.email;
        const phone = checkout.phone;

        const payload = {
            event_name: event.name,
            event_data: {
                email: email,
                phone: phone,
            },
        };

        // Example for sending event data to third party servers
        fetch('https://example.com/pixel', {
            method: 'POST',
            body: JSON.stringify(payload),
            keepalive: true,
        });
    });
}

function analytics_checkout_address_info_submitted(analytics) {
    analytics.subscribe('checkout_address_info_submitted', (event) => {
        console.log('Checkout address info submitted', event)
        const checkout = event.data.checkout;

        const payload = {
            event_name: event.name,
            event_data: {
                addressLine1: checkout.shippingAddress?.address1,
                addressLine2: checkout.shippingAddress?.address2,
                city: checkout.shippingAddress?.city,
                country: checkout.shippingAddress?.country,
            },
        };
    });
}

function analytics_alert_displayed(event) {
    analytics.subscribe('alert_displayed', (event) => {
        console.log('Alert displayed', event);
        const {target, type, message} = event.data.alert;

        const payload = {
            event_name: event.name,
            event_data: {
                target,
                type,
                message,
            },
        };
    });
}