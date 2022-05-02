from flask import current_app as app, jsonify, render_template, request
import os
import stripe

stripe_keys = {
  'secret_key': os.environ['STRIPE_SECRET_KEY'],
  'publishable_key': os.environ['STRIPE_PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', key=stripe_keys['publishable_key'])

@app.route('/checkout', methods=['POST'])
def checkout():
    amount = 50000000

    customer = stripe.Customer.create(
        email='sample@customer.com',
        source=request.form['stripeToken']
    )

    stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='ngn',
        description='Flask Charge'
    )

    return render_template('checkout.html', amount=amount)