import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'loan.db'
CSRF_ENABLED = True
SECRET_KEY = 'Rhq9rze7UifLEf'
DATABASE_PATH = os.path.join(basedir, DATABASE)

SQLALCHEMY_DATABASE_URI ='sqlite:///' + DATABASE_PATH
