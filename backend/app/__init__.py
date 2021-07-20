from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.email_controller import api as email_ns
from .main.controller.books_controller import api as book_ns

db = main.model.db
blueprint = Blueprint('api', __name__)
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'authorization'
    }
}
api = Api(blueprint,authorizations=authorizations,security='apikey',
          title='Eiodola Public API',
          version='1.0',
          description='Eiodola Public API for Diagnostic data analytics'
          )

api.add_namespace(user_ns)
api.add_namespace(email_ns)
api.add_namespace(book_ns)