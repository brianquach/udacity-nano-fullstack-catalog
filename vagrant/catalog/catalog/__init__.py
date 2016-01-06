from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json


# This app's client Id to generate an access token from Google's OAuth API
CLIENT_ID = json.loads(
    open('client_secret.json', 'r').read()
)['web']['client_id']

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catalog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from catalog import views