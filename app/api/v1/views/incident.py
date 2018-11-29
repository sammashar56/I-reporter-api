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

        model.add_record(data)


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

    def put(self, id):
        specific_incident = model.get_specif_record(id)
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
                    return({'status':'success','message':'comments and location updated'}),201
                else:
                    return({'status':'success','message':'comment only updated'}),201
            elif not args['comment']:
                if args['location']:
                    specific_incident[0]['location'] = args['location']
                    return({'status':'success','message':'only location updated'}),201
        else:
            return({'msg':'incident not found'}),404  

    def delete(self, id):
        specific_incident = model.get_specif_record(id)
        if specific_incident:
            value = model.delete_incident(id)
            return({'status':'successfully deleted'}),200
        else:
            return({'status':'failed to delete'}),404

