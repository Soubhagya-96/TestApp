import uuid
import datetime
import itertools
from app.main import db
from app.main.model.books_model import Book

def getAllBooks():

    book_obj_list = []
    book_obj = {}

    # print(Book.query.all())
    id_list = db.session.query(Book.book_id).all()
    for b_id in id_list:
        book_obj['book_name'] = db.session.query(Book.name).filter_by(book_id=b_id).first()[0]
        book_obj['book_author'] = db.session.query(Book.author).filter_by(book_id=b_id).first()[0]
        book_obj['book_price'] = db.session.query(Book.price).filter_by(book_id=b_id).first()[0]

        if book_obj != {}:
            book_obj_list.append(book_obj)
            book_obj = {}

    return book_obj_list

def addNewBook():
    book = Book.query.filter_by(name = data['name']).first()
    if not book:
        new_book = Book(
            name = data['name'],
            author = data['author'],
            price = data['price']
        )

        db.session.add(new_user)
        db.session.commit()
        db.session.close()

        response_object = {
            'status': 'success',
            'message': 'successfully added new book details'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Book details already exists'
        }
        return response_object, 409

def deleteBook(data):
    book_name = data['name']
    Book.query.filter_by(name=book_name).delete()
    db.session.commit()
    db.session.close()

    response_object = {
        'status': 'success',
        'message': 'Book details successfully deleted'
    }
    return response_object, 200