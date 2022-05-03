from flask import current_app as app, render_template

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')