from flask import request, abort
from flask_restx import Resource
from app.main import db
import requests

from ..util.email_dto import EmailDto
from app.main.model.user_model import User
from app.main.util.verify_token import *
api = EmailDto.api
_email = EmailDto.email


@api.route('/<email>')
@api.param('email', 'The email to be verified')
@api.response(404, 'Email not found.')
class UserEmail(Resource):
    @token_required
    def get(self, email):
        """Returns the name of the user for the corresponding email address"""

        try:

            exists = db.session.query(
            User.user_id).filter_by(email=email).scalar()
            print("Output: ", exists)
            user = bool(db.session.query(User).filter_by(email=email).all())
            if user:
                print("User exists")
                return exists
            else:
                print("user doesnot exist")
                return user

        except:
            db.session.rollback()