import os
import unittest
import requests

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_cors import CORS
from flask_restx import Resource
from flask import request

from app import blueprint
from app.main import create_app, db
from app.main.model.user_model import User
from app.main.model.books_model import Book


app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
CORS(app)
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

# code snippet to populate database with initial values
@app.before_first_request
def create_tables():
    db.create_all()
    if len(User.query.all()) == 0:
        new_user = User(
            email = 'soubhagyasahoo065@gmail.com',
            user_name = 'Soubhagya Sahoo',
            user_type = 'mail'
        )
        db.session.add(new_user)
        db.session.commit()

        new_user2 = User(
            user_name = 'Nalita Palai',
            password = 'mamalita03',
            user_type = 'normal'
        )
        db.session.add(new_user2)
        db.session.commit()

    if len(Book.query.all()) == 0:
        new_book = Book(
            name = 'The Room on the Roof',
            author = 'Ruskin Bond',
            price = 200
        )
        db.session.add(new_book)
        db.session.commit()


@manager.command
def run():
    app.run(host="0.0.0.0", port=5000, debug=True)

@manager.command
def runprod():
    app.run(host="0.0.0.0", port=5001, debug=False)


if __name__ == '__main__':
    manager.run()