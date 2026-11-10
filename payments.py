import stripe

stripe.api_key = "sk_test_placeholder"


def charge(amount):
    return stripe.PaymentIntent.create(amount=amount, currency="usd")
