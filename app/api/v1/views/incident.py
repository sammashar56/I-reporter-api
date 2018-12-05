#third party imports
from flask_restful import Resource, reqparse

#local imports
from app.api.v1.validators import Validators 
from app.api.v1.models import IncidentModel 
model = IncidentModel()
validator = Validators()
class Incident(Resource, IncidentModel):
    """incident endpoints """
    def get(self):
        """get all records of incidents"""
        if len(self.incident) == 0:
            return ({'message': 'no records found'}), 200
        return ({'incidents': self.incident}), 200
 
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
        data = {'comment': args['comment'], 
        'location':args['location'],
        'type_of_incident':args['type_of_incident']}

        model.add_incident(data)

        return ({'status':201,'Incident': data}),201

class SingleIncidentResource(Resource, IncidentModel):
    """Get specific record class"""
    specific_incident = model.get_specif_incident(id)
    def get(self, id):
        """gets a specific incident"""
        is_valid_id = validator.check_id_valid(id)
        if is_valid_id:
            if model.get_specif_incident(id):
                return ({'status': 200,
                "Incident":model.get_specif_incident(id)}),200
            return ({"status":404,
            "incident": 'incident not found'}),404

    def put(self, id):
        """updates a specific incident"""
        is_valid_id = validator.check_id_valid(id)
        if is_valid_id:
            specific_incident = model.get_specif_incident(id)
            parser = reqparse.RequestParser()
            parser.add_argument('comment',
            type=str,
            required=False
            )
            parser.add_argument('location',
            type=str,
            required=False
            )

            args = parser.parse_args()
            # pdb.set_trace()
            
            if specific_incident:
                if args['comment']:
                    specific_incident[0]['comment'] = args['comment']
                    if args['location']:
                        specific_incident[0]['location'] = args['location']
                        return({'status':201,'message':'comments and location updated'}),201
                    return({'status':201,'message':'comment only updated'}),201
                elif not args['comment']:
                    if args['location']:
                        specific_incident[0]['location'] = args['location']
                        return({'status':201,'message':'location only updated'}),201
            return({'message':'incident not found'}),404  

    def delete(self, id):
        """deletes a specififc incident"""
        if validator.check_id_valid(id):     
            specific_incident = model.get_specif_incident(id)
            if specific_incident:
                model.delete_incident(id)
                return({'status':200}),200
            return({'message':'incident not found'}),404
        return({'message':'invalid id'})
