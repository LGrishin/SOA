from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.exc import IntegrityError

from werkzeug.exceptions import Forbidden, Conflict, NotFound

import os
import jwt
import hashlib


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_LOCATION')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

jwt_secret_key = ''

secret_file_path = os.environ.get('SECRETS_PATH') + '/jwt_secret_key'
with open(secret_file_path, 'r') as file:
    jwt_secret_key = file.readlines()[0]

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
 
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    birth_date = db.Column(db.Date, nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(50), nullable=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    try:
        hashed_pwd = hashlib.md5(password.encode('utf-8')).hexdigest()
        user = User(username, hashed_pwd)
        db.session.add(user)
        db.session.commit()
        # session['user_id'] = user.id
        return jsonify({'message': 'User regitred successfully'})
    
    except IntegrityError:
        raise Conflict('User already exists')
        
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
        
    hashed_pwd = hashlib.md5(password.encode('utf-8')).hexdigest()
    
    user = User.query.filter_by(username=username, password=hashed_pwd).first()
    token = jwt.encode({'username': username}, jwt_secret_key, algorithm='HS256')
    
    if user:
        # session['user_id'] = user.id
        return jsonify({'message': 'login successful', 'token' : token, 'username': username})
    else:
        raise Forbidden('Invalid username or password')

@app.route('/update', methods=['PUT'])
def update_user_data():
    token = request.form['token']
    try:
        username = jwt.decode(token, jwt_secret_key, algorithms=['HS256'])['username']
    except:
        return Forbidden('Invalid jwt token')

    user = User.query.filter_by(username=username).first()

    if not user:
        return NotFound('User not found')

    data = request.form
    if 'first_name' in data:
        user.first_name = data['first_name']
    if 'last_name' in data:
        user.last_name = data['last_name']
    if 'password' in data:
        user.password = data['password']
    if 'birth_date' in data:
        user.birth_date = data['birth_date']
    if 'phone' in data:
        user.phone = data['phone']
    if 'email' in data:
        user.email = data['email']

    db.session.commit()
    return jsonify({'message': 'User data updated successfully'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


# curl -d 'username=lavr&password=123' http://127.0.0.1:5000/register
# curl -d 'username=lavr&password=123' http://127.0.0.1:5000/login
# curl -X PUT -d 'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImxhdnIifQ.s4rvWjGTbOTO_vcElQl1ka6umxRfBhg_95Zn7TwbYrY&email=0000' http://127.0.0.1:5000/update