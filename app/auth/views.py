from functools import wraps
from flask import Blueprint, redirect, url_for, flash, render_template
from flask_login import current_user, login_required, logout_user

from .forms import RegisterForm
from .models import UserModel
from app import login_manager


auth = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates')


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return UserModel.query.get(user_id)


def role_required(*role):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if role[0] not in [i.name for i in current_user.roles]:
                flash('You do not have permission to this page.')
                return redirect(url_for('main.index'))
            return f(*args, **kwargs)
        return wrapped
    return wrapper


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    title = "Sign-up"
    form = RegisterForm()
    if form.validate_on_submit():
        user = UserModel.query.filter_by(email=form.email.data).first()  # if this returns a user, then the email already exists in database

        if user:
            flash('Email address already exists')
            return render_template('auth.signup.html', title=title, form=form)

        if len(form.password.data) < 8:  # if a user is found, we want to redirect back to signup page so user can try again
            flash('password lenght must be more 7 symbols')
            return render_template('auth.signup.html', title=title, form=form)

        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        new_user = UserModel(email=form.email.data, password=form.password.data)

        # add the new user to the database
        new_user.save_to_db()
        return redirect(url_for('index'))

    return render_template('auth.signup.html', title=title, form=form)
