from app import create_app
from flask_script import Manager, Server

# Creating app instance
app = create_app('development')
