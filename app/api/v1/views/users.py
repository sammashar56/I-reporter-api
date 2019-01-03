from flask_restful import Resource, reqparse

#local imports
from app.api.v1.models import UsersModel
from app.api.v1.validators import Validators 

validator = Validators()
model = UsersModel()

class UserRegistration(Resource):
	""" user regstration"""
	def post(self):
		"""user registration"""
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
		email = validator.check_email(args['email'])
		password = validator.check_password(args['password'])
		if email and password:
			if args['password'] == args['confirm_password']:
				model.add_user(args)
				return({'status':201,
						'user':args}),201
			return({'message': 'passwords do not match'}),401


class UserLogin(Resource):
	"""user login"""
	def post(self):
		"""loging in a user"""
		parser = reqparse.RequestParser()
		parser.add_argument('email',
		required=True,
		type=str,
		help='provide a valid email'
		)

		parser.add_argument('password',
		required=True,
		type=str,
		help='provide a password'
		)

		args = parser.parse_args()
		email = validator.check_email(args['email'])
		password = validator.check_password(args['password'])
		if email and password:
			return({'status':200,
			'message':'logged in'})
