from flask import Blueprint
main = Blueprint('main', __name__)
from .import views, errors

def create_app(config_name):
    app = Flask(__name__)
    
     #Create tha app configurations
    app.config.from_object(config_options[config_name])
    