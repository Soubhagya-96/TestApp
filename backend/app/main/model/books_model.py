from .. import db, flask_bcrypt
from sqlalchemy import Column,Integer,String
from ..config import key
from .. import db

class Book(db.Model):
    """ Book Model for storing book related details """
    __tablename__ = "books"

    book_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    author = Column(String(50), unique=True, nullable=False)
    price = Column(Integer, nullable=False)
    
    def __repr__(self):
        return "<Book '{}'>".format(self.book_id)
