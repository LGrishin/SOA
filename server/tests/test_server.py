import pytest
import sys
from Server import create_app

sys.path.insert(0, '../Server')

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        'TESTING': True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

client_1 = {
    'username' : 'leha228',
    'password' : 'ya_umnii',
    'firstname' : 'Alexey',
    'lastname' : 'Ivanov',
    'birthdate' : '1990-01-01',
    'email' : 'lehahahahahh@yandex.ru',
    'phone' : '+79999999999',
}

client_2 = {
    'username' : 'pupa',
    'password' : '1111',
    'firstname' : 'Pupa',
    'lastname' : 'Lupa',
    'birthdate' : '2010-04-01',
    'email' : 'tmp@mail.com',
    'phone' : '+79991111111',
}

def test_hello_world(client):
    response = client.get('/hello')
    assert b'Hello, World!' in response.data

def test_register_get(client):
    response = client.get('/auth/register')
    assert b'OK' in response.data

def test_register_post(client):
    response = client.post('/auth/register', data=client_1)
    assert b'OK' in response.data
    response = client.post('/auth/register', data=client_1)
    assert b'User leha228 is already registered.' in response.data

def test_login_post(client):
    response = client.post('/auth/login', data={'username' : 'allax', 'password': 'akbar'})
    assert b'Incorrect username.' in response.data
    response = client.post('/auth/login', data={'username' : 'leha228', 'password': 'ya_umnii'})
    assert b'OK' in response.data
    response = client.post('/auth/login', data={'username' : 'leha228', 'password': 'ya_umnii'})
    assert b'SESSION OK' in response.data
    response = client.post('/auth/login', data={'username' : 'leha228', 'password': 'ya_tupoi'})
    assert b'Incorrect password.' in response.data

def test_login_get(client):
    response = client.get('/auth/login')
    assert b'OK' in response.data

