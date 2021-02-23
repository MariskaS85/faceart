from django.http import HttpResponse


class StripeWH_Handler:
    """ Handle Stripe Webhooks """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle a generic unknown webhook event"""

        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200)


    def handle_payment_intent_succeeded(self, event):
        """Handle a succesfull payment intent webhook from Stripe """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200)


    def handle_payment_intent_payment_failed(self, event):
        """Handle a failed payment intent webhook from Stripe """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200)
