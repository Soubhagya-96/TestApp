import uuid
import datetime
import itertools
from app.main import db
from app.main.model.user_model import User

def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            email=data['email'],
            user_name=data['user_name']
        )

        db.session.add(new_user)
        db.session.flush()  
        generated_id = new_user.user_id  #generated id for user

        #insert data to relationship table
        for company in db.session.query(Company).all():
            for customer in db.session.query(Customer).all():
                new_relationship = Relationship(
                    user_id = generated_id,
                    company_id = company.company_id,
                    customer_id = customer.customer_id
                )
                db.session.add(new_relationship)
        db.session.commit()
        db.session.close()
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists.',
        }
        return response_object, 409


def get_all_users():    
    return User.query.all()

       
def validateUser(data):

    username = data['user_name']
    password = data['password']
    result = db.session.query(User.user_name).filter_by(user_name = username, password = password).first()
    if result: 
        response = {
            'status': 'success',
            'message': result[0]
        }
    else:
        response = {
            'status': 'fail',
            'message': 'User not found!'
        }
    return response