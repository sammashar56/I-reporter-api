#third party imports
from flask_restful import Resource, reqparse

#local imports
from app.api.models import incidents, Models


class Redflag(Resource, Models):
    """redflag endpoints """
    def get(self):
        """get all records of redflags and interventions"""
        if len(self.db) == 0:
            return ({'message': 'no records found'}),200
        return ({'incidents': self.db}),200

