from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
print("Flask app instance created")

app.config.from_object(Config)

db = SQLAlchemy(app)

from .routes import main  # Importação relativa correta
app.register_blueprint(main)
print("Blueprint registered")
