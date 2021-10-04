from flask import Flask
from flask_migrations import Migrations


def init_app(app:Flask):
    Migrations(app, app.db)