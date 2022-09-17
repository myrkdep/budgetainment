from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_httpauth import HTTPBasicAuth
from pathlib import Path
from config import *

#init app
app = Flask(__name__)
database_url = f'mysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_URL}:3306/{DATABASE_NAME}'
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)
ma = Marshmallow(app)
auth = HTTPTokenAuth('Bearer')
token_serializer = Serializer(app.config['SECRET_KEY'], expires_in=3600)

#databasemodels
class Member(db.Model):
    email = db.Column(db.String(200), primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    role = db.Column(db.String(8), nullable=False)
    active = db.Column(db.SmallInteger, nullable=False)

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password
        self.role = 'user'
        self.active = 0


#auth setup
@auth.get_user_roles
def get_user_roles(email):
    return Member.query.get(email).type

#routes
@app.route('/api/health', methods=['GET'])
def health():
    return {'msg': 'Ok'}

@app.route('/api/signup', methods=['POST'])
def signup():
    pass

@app.route('/api/activate', methods=['POST'])
def activate():
    pass

@auth.login_required(role=['admin', 'user'])
@app.route('/api/login', methods=['POST'])
def login():
    pass

@auth.login_required(role=['admin', 'user'])
@app.post('/api/add-sent', methods=['POST'])
def add_sent():
    pass

@auth.login_required(role=['admin', 'user'])
@app.post('/api/add-recived', methods=['POST'])
def add_recived():
    pass

@auth.login_required(role=['admin', 'user'])
@app.route('/api/add-debt', methods=['POST'])
def add_dept():
    pass

@auth.login_required(role=['admin', 'user'])
@app.route('/api/delete-debt', methods=['DELETE'])
def delete_debt():
    pass

@auth.login_required(role=['admin', 'user'])
@app.route('/api/add-demand', methods=['POST'])
def add_demand():
    pass

@auth.login_required(role=['admin', 'user'])
@app.route('/api/delete-demand', methods=['DELETE'])
def delete_demand():
    pass

@auth.login_required(role=['admin', 'user'])
@app.route('/api/depts', methods=['GET'])
def depts():
    pass

@auth.login_required(role=['admin', 'user'])
@app.route('/api/demands', methods=['GET'])
def demands():
    pass

@auth.login_required(role=['admin', 'user'])
@app.route('/api/report', methods=['GET'])
def report():
    pass

if __name__ == '__main__':
    app.run(debug=False)