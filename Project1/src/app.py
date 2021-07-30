from flask import Flask
from flask_session import Session
from flask_cors import CORS

# Setting static_url_path removes "static" from url paths for static resources
flask_app = Flask(__name__, static_url_path='', template_folder='static')
sess = Session()
CORS(flask_app)
