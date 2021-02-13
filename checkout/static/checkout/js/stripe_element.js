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
var card = elements.create('card');
card.mount('#card-element')