from .. import db, flask_bcrypt
from sqlalchemy import Column,Integer,String
from ..config import key
from .. import db

class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=True)
    user_name = Column(String(50), unique=False, nullable=False)
    password = Column(String(64), unique=False, nullable=True)
    user_type = Column(String(32), unique=False, nullable=False)
     
    def __repr__(self):
        return "<User '{}'>".format(self.user_name)
