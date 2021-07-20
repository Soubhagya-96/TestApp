import os
import sqlalchemy

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):

    DEBUG = True
    engine = sqlalchemy.create_engine('mysql://root@localhost', connect_args={'connect_timeout': 86400})
    engine.execute("CREATE DATABASE IF NOT EXISTS applesauce")
    engine.execute("USE applesauce")
    
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/applesauce'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    dev=DevelopmentConfig,
)

key = Config.SECRET_KEY