/*
Need to check this:
Core logic/payments flow for this comes from here:
https://stripe.com/docs/payments/accept-a-payment?integration=elements
https://stripe.com/docs/payments/integration-builder
Css from here:
https://stripe.com/docs/stripe-js
*/

var stripe_public_key = $('#id_stripe_public_key').text().slice(1,-1);
var stripe_public_key = $('#id_stripe_public_key').text().slice(1,-1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Oswald"',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#fa755a',
        iconColor: '#fa755a'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');
