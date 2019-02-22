#third party imports
from flask_restful import Resource, reqparse

#local imports
from app.api.v2 import validator
from app.api.v2.model.incident_model import IncidentModel 
from app.api.v2.protect import *

from app.api.v2.helpers import Helper as h
model = IncidentModel()
#validity = Validators()

class AuthIncident(Resource):
    """incident endpoints """
    @auth_required
    def post(self): 
        """create an incident"""
        parser = reqparse.RequestParser()
        parser.add_argument('title', 
        type=str, 
        required=True, 
        help='provide a title')

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
        data = {'title':args['title'],'comment': args['comment'],"user_id":h.default_user(), 
        'location':args['location'],
        'type_of_incident':args['type_of_incident']}
        model.add_incident(data)
        return (
            {
                'status':201,
                'message':'incident created',
                'Incident': data
            }
            ),201

    @check_admin        
    def get(self):
        """get all incidents"""
        incidents = model.get_all_incidents()
        if incidents:
            serialized_incidents = []
            for i in incidents:
                serialized_incidents.append(h.incident_serializer(i))
            return serialized_incidents
        return (
            {
                "message":"no incidents found"
            }
            ),201

 
class SingleIncidentResource(Resource, IncidentModel):
    """Get specific record class"""
    @auth_required
    def get(self, id):
        """get a specific incident"""
        logged_user = h.default_user() 
        incident = model.get_specific_incident(id)
        if incident[7] == logged_user:
            if incident:
                incidents = h.incident_serializer(incident)
                return({"incident":incidents})
            return({"message":"incident not found"}) 
        return({"message":"Access denied"})
    @auth_required
    def delete(self, id):
        """delete a specific incident"""
        logged_user = h.default_user()     
        incident = model.get_specific_incident(id)
        if incident:
            if incident[7] == logged_user:
                if incident[4] == 'draft':
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
            return({"message":"status updated","status":status}),201
        return ({"message":"incident not found"}),201

class UpdateIncident(Resource):
    """updating an incident"""
    @auth_required
    def put(self, id):
        """update an incident"""
        logged_user = h.default_user()     
        incident = model.get_specific_incident(id)
        if incident:
        # if incident[7] == logged_user:
            parser = reqparse.RequestParser()
            parser.add_argument('comment',
            type=str,
            required=False
            )
            parser.add_argument('location',
            type=str,
            required=False
            )
            parser.add_argument('title',
            type=str,
            required=False
            )
            args = parser.parse_args()
            comment = args['comment']
            title = args['title']
            location = args['location']
            #print(incident[7])
            if incident[7] == logged_user:
                if incident[4] == 'draft':
                    if comment:
                            model.update_comment_only(comment, id)
                            if location:
                                model.update_location_only(location, id)
                                if title:
                                    model.update_title_only(title,id) 
                                return(
                                    {
                                        'status':201,
                                        'message':'comments, title and location updated'
                                    }
                                    ),201
                            return(
                                {
                                    'status':201,
                                    'message':'comment only updated'
                                }
                                ),201
                    elif not comment:
                        if location:
                            model.update_location_only(location, id)
                            if title:
                                model.update_title_only(title, id)
                            return({'status':201,'message':'location and title updated'}),201
                    elif title:
                            model.update_title_only(title, id)
                    return (
                        {"message":"title only updated","title":title})
                return({'message':'can no longer update incident'}),404  
            return({"message": "Access denied"}),201
        return({"message": "incident not found"}),201