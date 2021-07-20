from flask import request, abort
from flask_restx import Resource
from app.main import db
import requests

from ..util.books_dto import BookDto
from app.main.model.books_model import Book
from app.main.util.verify_token import *
from app.main.service.books_service import getAllBooks

api = BookDto.api
_name = BookDto.book

@api.route('/getBooks')
@api.response(404, 'No records found')
class AllBookDetails(Resource):
    # @token_required
    def get(self):
        return getAllBooks()