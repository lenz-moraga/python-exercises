from flask import Flask
from infrastructure.database import Base, engine
from .routes import bp
import os

def create_app():
    app = Flask(__name__)

    # Crear tablas si no existen
    Base.metadata.create_all(bind=engine)

    app.register_blueprint(bp)
    return app
