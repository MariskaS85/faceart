from django.conf import settings
from django.http import HttpResponse
from django.views.decorators import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import Stripe_WH_Handler

import stripe

@require_POST
@csrf_exempt


def webhook(request):
    #listen for webhooks from Stripe
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignetureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        # Invalid signature
        return HttpResponse(content=e, status=400)

    print('Succes!')
    return HttpResponse(status=200)