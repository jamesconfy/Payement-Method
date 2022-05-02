from flask import Flask
from config import DevConfig


def create_app():
    app = Flask("paymentmethod")
    app.config.from_object(DevConfig)

    with app.app_context():
        from paymentmethod import routes
        
    return app