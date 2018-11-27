#third party imports
from flask_restful import Resource, reqparse

#local imports
from app.api.v1.models import incidents, Models


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

        parser.add_argument('location',
        type=str,
        required=True, 
        help='please provide location')
        args = parser.parse_args()
        Models().add_record(args)

        return ({'Record': args}),201

   


