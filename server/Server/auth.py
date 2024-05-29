import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from Server.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        birthdate = request.form['birthdate']
        email = request.form['email']
        phone = request.form['phone']
        db = get_db()

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password, firstname, lastname, birthdate, email, phone) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (username, generate_password_hash(password), firstname, lastname, birthdate, email, phone),
                )
                db.commit() 
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return 'OK' #redirect(url_for("auth.login"))

        # flash(error)
    if error is None:
        return 'OK'
    return error

@bp.route('/login', methods=('GET', 'POST'))
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return 'SESSION OK' #redirect(url_for('index'))

        # flash(error)

    if error is None:
        return 'OK'
    return error

# @bp.route('/update', methods=('GET', 'POST'))
# def login():
#     error = None
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         db = get_db()
#         user = db.execute(
#             'SELECT * FROM user WHERE username = ?', (username,)
#         ).fetchone()

#         if user is None:
#             error = 'Incorrect username.'
#         elif not check_password_hash(user['password'], password):
#             error = 'Incorrect password.'

#         if error is None:
#             session.clear()
#             session['user_id'] = user['id']
#             return 'SESSION OK' #redirect(url_for('index'))

#         # flash(error)

#     if error is None:
#         return 'OK'
#     return error


# def none_func(e):
#     print(e)
#     pass

# def init_command(app):
#     app.teardown_appcontext(none_func)
#     app.cli.add_command(login)
#     app.cli.add_command(register)
