#third party modules
from flask import Flask
from flask_restful import Api

#local imports
from instance.config import app_config
from app.api.v1.views.incident import Incident, SingleIncidentResource
from app.api.v1.views.users import UserRegistration
from app.api.v2.Auth.user import UserRegister

def create_app(config): 
    """this method creates all instance needed for endpoints"""
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(app_config[config])
    app.url_map.strict_slashes = False
    api.add_resource(Incident, '/api/v1/incidents')
    api.add_resource(SingleIncidentResource, '/api/v1/incident/<int:id>')
    api.add_resource(UserRegistration, '/api/v1/users')
    api.add_resource(UserRegister, '/api/v2/auth/signup')
    
            
    return app  
