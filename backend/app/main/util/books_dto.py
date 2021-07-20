from flask_restx import Namespace, fields


class BookDto:
    api = Namespace('book', description='Book Related Operations')
    book = api.model('book_details', {
        'name': fields.String(required=True, description='Book Name'),
        'author': fields.String(required=True, description='Author Name'),
        'price': fields.Integer(required=True, description='Book Price')
    })