from flask_restful import Resource, reqparse
from app.api.v2.validator import Validators
from werkzeug.security import check_password_hash, generate_password_hash

from app.api.v2.token import Token as t
from app.api.v2.model.user import ModelUser

model = ModelUser()
validator = Validators()


class UserRegister(Resource):
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
		parser.add_argument(
			'is_admin',
			type=bool,
			required=True,
			help='provide a role'
		)

		args = parser.parse_args()
		validator.check_email(args['email'])
		if args['password'] == args['confirm_password']:
			validator.check_password(args['password'])
			data = model.add_user(args)
			return (
				{
					"status":201,
					"message":"Registration success",
					"data":data
				}
			), 201
		return({'message':"passwords do not match"}),200

class Login(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('email',
		type=str,
		required=True,
		help='please provide an email'
		)
		parser.add_argument('password',
		type=str,
		required=True,
		help='please provide a password'
		)
		args = parser.parse_args()
		email = validator.check_email(args['email'])
		password = validator.check_password(args['password'])
		user = model.check_email(email)
		print(model.get_user_password(email)[0])
		print(user)
		#print(email)
		#if user:
		if check_password_hash(model.get_user_password(email)[6], password):
			token = t.encode_auth_token(str(model.get_user_password(email)[0]))
			return ({"token": token.decode()})
		#	return ({"message":"passwords do not match"})
		return({"message":"user not found"})
		
