from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='User Related Operations')
    user = api.model('user_details', {
        'email': fields.String(required=True, description='User Email Address'),
        'user_name': fields.String(required=True, description='User Username'),
        'password': fields.String(required=False, description='Password'),
        'user_type': fields.String(required=True, description='User Type')
    })