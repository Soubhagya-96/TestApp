import requests
from flask import request,abort
from functools import wraps

def token_required(f):
    @wraps(f)
    def verify(*args, **kwargs):
        user_verified = False
        token = request.headers.get('authorization')

        if(token == None):
            return abort(403)
        url = 'https://www.googleapis.com/oauth2/v3/tokeninfo?access_token='
        response = requests.get(url+token)
        values = response.json().items()
        for key, value in values:
            if(key == 'email_verified' and value == 'true'):
                user_verified = True
        if(user_verified != True):
            return abort(403)
        return f(*args, **kwargs)
    return verify