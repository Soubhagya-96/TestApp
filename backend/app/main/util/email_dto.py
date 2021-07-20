from flask_restx import Namespace, fields

class EmailDto:
    api = Namespace('checkemail', description='Email verification to check its existence')
    email = api.model('email_details', {
        'user_id': fields.Integer(required=True, description='User ID')
    })