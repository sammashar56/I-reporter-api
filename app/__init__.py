#third party modules
from flask import Flask
from flask_restful import Api

#local imports
from instance.config import app_config
from app.api.v1.views.incident import Redflag, Get_incident

def create_app(config):
    """this method creates all instance needed for endpoints"""
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(app_config[config])
    api.add_resource(Redflag, '/api/v1/incidents')
    api.add_resource(Get_incident, '/api/v1/incident/<int:id>')

            
    return app  
