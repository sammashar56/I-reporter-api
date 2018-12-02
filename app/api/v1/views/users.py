from flask_restful import Resource, reqparse

from app.api.v1.models import Models

model = Models()

class Users(Resource):
	""" user regstration"""
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('firstname',
			type=str,
			required=True,
			help='provide a firstname'
			)
		parser.add_argument('lastname',
			type=str,
			required=True,
			help='provide a lastname'
			)
		parser.add_argument('phone_no',
			type=int,
			required=True,
			help='provide a phone number'
			)
		parser.add_argument('email',
			type=str,
			required=True,
			help='provide an email'
			)
		parser.add_argument('password',
			type=str,
			required=True,
			help='provide a password'
			)
		parser.add_argument('confirm_password',
			type=str,
			required=True,
			help='confirm password'
			) 

		args = parser.parse_args()
		if args['password'] == args['confirm_password']:
			model.add_user(args)
			return({'status':'user successfully created',
				    'user':args}),201
		else:
			return({'message': 'passwords do not match'}),401