#third party imports
from flask_restful import Resource, reqparse

#local imports
from app.api.v2 import validator
from app.api.v2.model.incident_model import IncidentModel 
from app.api.v2.protect import *

from app.api.v2.helpers import Helper as h
model = IncidentModel()
#validity = Validators()

class AuthIncident(Resource, IncidentModel):
    """incident endpoints """
    @auth_required
    def post(self): 
        """create an incident"""
        parser = reqparse.RequestParser()
        parser.add_argument('comment', 
        type=str, 
        required=True, 
        help='provide a comment')

        parser.add_argument('type_of_incident', 
        type=str, 
        required=True, 
        help='provide type of incident')

        parser.add_argument('location',
        type=str,
        required=True,
        help='please provide location')
        args = parser.parse_args()
        data = {'comment': args['comment'],"user_id":h.default_user(), 
        'location':args['location'],
        'type_of_incident':args['type_of_incident']}
        model.add_incident(data)
        return (
            {
                'status':201,
                'Incident': data
            }
            ),201

    @check_admin        
    def get(self):
        """get all incidents"""
        incidents = model.get_all_incidents()
        if len(incidents) == 0:
            return ({"message":"no incidents found"})
        return ({"incidents": incidents})

   
class SingleIncidentResource(Resource, IncidentModel):
    """Get specific record class"""
    @auth_required
    def get(self, id):
        """get a specific incident"""
        specific_incident = model.get_specific_incident(id)
        if specific_incident:
            return({"incident":specific_incident})
        return({"message":"invalid id"}) 

    @auth_required
    def delete(self, id):
        """delete a specific incident"""
        #draft = model.check_status_draft()
        logged_user = h.default_user()     
        incident = model.get_specific_incident(id)
        if incident:
            if incident[6] == logged_user:
                if incident[3] == 'draft':
                    model.delete_specific_incident(id)
                    return({"message":"incident deleted"})
                return({"message":"can no longer delete incident"})
            return({"message":"cannot delete incident"})
        return({"message":"incident not found"})

    @check_admin
    def put(self, id):
        """update an incident status"""
        parser = reqparse.RequestParser()
        parser.add_argument('status',
        type=str,
        )
        args = parser.parse_args()
        status = args['status']
        incident = model.get_specific_incident(id)
        if incident:
            model.update_incident_status(status, id)
            return({"message":"status updated","status":status})
        return ({"message":"incident not found"})
