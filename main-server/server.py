from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.exc import IntegrityError

from werkzeug.exceptions import Forbidden, Conflict, NotFound, InternalServerError

import os
import jwt
import hashlib

import grpc
import post_api_pb2, post_api_pb2_grpc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_LOCATION')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

jwt_secret_key = ''

secret_file_path = os.environ.get('SECRETS_PATH') + '/jwt_secret_key'
with open(secret_file_path, 'r') as file:
    jwt_secret_key = file.readlines()[0]

db = SQLAlchemy(app)

channel = grpc.insecure_channel(os.environ.get('POST_SERV_ADDR'))
post_serv = post_api_pb2_grpc.PostsStub(channel)


def get_uid_by_jwt(token):
    try:
        username = jwt.decode(token, jwt_secret_key, algorithms=['HS256'])['username']
    except:
        raise Forbidden('Invalid jwt token')

    user = User.query.filter_by(username=username).first()

    if not user:
        raise NotFound('User not found')
    return user.id


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

@app.route('/add-post', methods=['POST'])
def add_post():
    token = request.form['token']
    user_id = get_uid_by_jwt(token)
    content = request.form['content']
    
    # return jsonify({'message': 'The new post has been successfully added', 'user_id': user_id, 'content': content})
    grpc_request = post_api_pb2.AddPostRequest(user_id=user_id, content=content)
    
    response = post_serv.AddPost(grpc_request)

    return jsonify({'message': 'The new post has been successfully added', 'post_id': response.post_id})

@app.route('/update-post', methods=['PUT'])
def update_post():
    token = request.form['token']
    post_id = request.form['post_id']
    user_id = get_uid_by_jwt(token)
    new_content = request.form['content']

    grpc_request = post_api_pb2.AddPostRequest(user_id=user_id, post_id=post_id, new_content=new_content)
    
    response = post_serv.UpdatePost(grpc_request)
    if response.success:
        return jsonify({'message': 'The post has been successfully updated'})
    return InternalServerError('error during update')

@app.route('/delete-post', methods=['DELETE'])
def delete_post():
    token = request.form['token']
    post_id = request.form['post_id']
    user_id = get_uid_by_jwt(token)

    grpc_request = post_api_pb2.DeletePostRequest(user_id=user_id, post_id=post_id)
    response = post_serv.DeletePost(grpc_request)
    if response.success:
        return jsonify({'message': 'The post was successfully deleted'})
    return InternalServerError('Error during delete')


@app.route('/get-post', methods=['GET'])
def get_post():
    token = request.form['token']
    post_id = request.form['post_id']
    get_uid_by_jwt(token)

    grpc_request = post_api_pb2.GetPostRequest(post_id=post_id)

    response = post_serv.GetPost(grpc_request)
    if not response.success:
        return InternalServerError('Error processing the request')
    content = response.content
    return jsonify({'message': 'The data was successfully received', 'content': content})

@app.route('/get-posts', methods=['GET'])
def get_posts():
    token = request.form['token']
    offset = request.form['offset']
    number_of_posts = request.form['number_of_posts']
    get_uid_by_jwt(token)

    grpc_request = post_api_pb2.AddPostRequest(offset=offset, number_of_posts=number_of_posts)
    
    result = []
    response = post_serv.GetPosts(grpc_request)
    for post in response:
        if not post.success:
            return InternalServerError('Error processing the request')
        result.append(post.content)
    return jsonify({'posts': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# python3 -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/post-api.proto
# curl -d 'username=lavr&password=123' http://127.0.0.1:5000/register
# curl -d 'username=lavr&password=123' http://127.0.0.1:5000/login
# curl -X PUT -d 'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImxhdnIifQ.s4rvWjGTbOTO_vcElQl1ka6umxRfBhg_95Zn7TwbYrY&email=0000' http://127.0.0.1:5000/update