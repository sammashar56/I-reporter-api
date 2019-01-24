#third party modules
from flask import Flask
from flask_restful import Api

#local imports
from instance.config import app_config
from app.api.v1.views.incident import Incident, SingleIncident
from app.api.v1.views.users import UserRegistration
from app.api.v2.Auth.user import UserRegister, Login
from app.api.v2.Auth.incidents import AuthIncident, SingleIncidentResource, UpdateIncident
from flask_cors import CORS
def create_app(config): 
    """this method creates all instance needed for endpoints"""
    app = Flask(__name__)
    CORS(app)
    api = Api(app)
    app.config.from_object(app_config[config])
    app.url_map.strict_slashes = False
    api.add_resource(Incident, '/api/v1/incidents')
    api.add_resource(SingleIncident, '/api/v1/incident/<int:id>')
    api.add_resource(UserRegistration, '/api/v1/users')
    api.add_resource(UserRegister, '/api/v2/auth/signup')
    api.add_resource(AuthIncident, '/api/v2/incident')
    api.add_resource(UpdateIncident, '/api/v2/incident/update/<int:id>')
    api.add_resource(Login, '/api/v2/auth/login')
    api.add_resource(SingleIncidentResource, '/api/v2/incident/<int:id>')        
    return app  
