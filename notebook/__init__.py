from flask_sqlalchemy import SQLAlchemy
from flask import Flask

"""
initialize app and database
"""
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
db = SQLAlchemy(app)

from notebook import routes
