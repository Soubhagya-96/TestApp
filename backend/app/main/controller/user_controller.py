from flask import request, json
import requests
import urllib.request
from flask_restx import Resource
from app.main.util.verify_token import *

from ..util.user_dto import UserDto
from ..service.user_service import save_new_user, get_all_users, validateUser

api = UserDto.api
_user = UserDto.user

@api.route('/')
class UserList(Resource):
    # @token_required
    @api.doc('list_of_registered_users')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @token_required
    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)

@api.route('/checkUser')
class UserCheck(Resource):
    @api.expect(_user, validate=True)
    @api.doc('validate user')
    def post(self):
        data = request.json
        return validateUser(data)