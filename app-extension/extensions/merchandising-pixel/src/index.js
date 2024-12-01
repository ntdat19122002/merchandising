import {register} from "@shopify/web-pixels-extension";

register(({ analytics, browser, init, settings }) => {
    // Sample subscribe to page view
    analytics.subscribe('page_viewed', (event) => {
      console.log('Page viewed', event);
      fetch('https://20aa-42-113-60-43.ngrok-free.app/pixel/view');
    });

    analytics.subscribe('cart_viewed', (event) => {
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
        fetch('https://testsroredat.myshopify.com/apps/merchandising/pixel/view', {
          method: 'POST',
          body: JSON.stringify(payload),
          keepalive: true,
        });
    });
});

