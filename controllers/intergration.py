from crypt import methods

import shopify

from odoo import http
from odoo.http import request, Response
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException
import datetime


class Pixel(http.Controller):
    def upload_conversion(self, customer_id, conversion_action_id, gclid, conversion_date, conversion_value):
        """
        Upload a conversion to Google Ads.

        Args:
            customer_id (str): The Google Ads customer ID.
            conversion_action_id (str): The conversion action ID.
            gclid (str): The Google Click Identifier (GCLID).
            conversion_date (str): The conversion date in 'yyyy-mm-dd hh:mm:ss+|-hh:mm' format.
            conversion_value (float): The value of the conversion.

        """
        client = GoogleAdsClient.load_from_storage("google-ads.yaml")

        conversion_upload_service = client.get_service("ConversionUploadService")
        conversion_action_resource_name = client.get_service("ConversionActionService").conversion_action_path(
            customer_id, conversion_action_id
        )

        conversion = client.get_type("ClickConversion")
        conversion.conversion_action = conversion_action_resource_name
        conversion.gclid = gclid
        conversion.conversion_date_time = conversion_date
        conversion.conversion_value = conversion_value
        conversion.currency_code = "USD"  # Adjust as per your requirements

        try:
            response = conversion_upload_service.upload_click_conversions(
                customer_id=customer_id,
                conversions=[conversion],
                partial_failure=False,
            )
            if response.partial_failure_error:
                print("Partial failure occurred: ", response.partial_failure_error.message)
            else:
                print("Conversion successfully uploaded:", response.results)
        except GoogleAdsException as ex:
            print("Google Ads API request failed with errors:")
            for error in ex.failure.errors:
                print(f"Error: {error.message}")

    @http.route('/integration/google_ads',methods=['POST'],type='json', auth='public')
    def intergration_google_ads(self,**kw):
        CUSTOMER_ID = "1234567890"  # Replace with your customer ID
        CONVERSION_ACTION_ID = "123456"  # Replace with your conversion action ID
        GCLID = "example_gclid"  # Replace with the GCLID from the ad click
        CONVERSION_DATE = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S+00:00")
        CONVERSION_VALUE = 100.00  # Replace with the actual conversion value

        self.upload_conversion(CUSTOMER_ID, CONVERSION_ACTION_ID, GCLID, CONVERSION_DATE, CONVERSION_VALUE)