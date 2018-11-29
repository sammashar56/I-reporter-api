#third party imports
from flask_restful import Resource, reqparse

#local imports
from app.api.v1.models import incidents, Models

model = Models()

class Redflag(Resource, Models):
    """redflag endpoints """
    def get(self):
        """get all records of redflags and interventions"""
        if len(self.db) == 0:
            return ({'message': 'no records found'}), 200
        return ({'incidents': self.db}), 200

    def post(self): 
        """create a redflag"""
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
        # model.add_record(args)

        data = {'comment': args['comment'], 
        'location':args['location'],
        'type_of_incident':args['type_of_incident']}

        incident_data = model.add_record(data)


        return ({'status':'success','Incident': data}),201

class Get_incident(Resource):
    specific_incident = model.get_specif_record(id)
    """class to get specific record"""

    def get(self, id):
        if model.get_specif_record(id):
            return ({'status': "ok",
                "Incident":model.get_specif_record(id)}),200
        else: 
            return ({"status":"success",
                "incident": 'incident not found'}),200



