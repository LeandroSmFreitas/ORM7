from flask import Flask

from .cachorro_view import bp as bp_cachorro

def init_app(app:Flask):
    app.register_blueprint(bp_cachorro)