from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, EmailField
# from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms import validators

# from .models import RoleModel


# def getroles():
#     return RoleModel.query.all()


# class UserEditForm(FlaskForm):
#     id = HiddenField('id', [validators.DataRequired()])
#     email = StringField('email', [validators.DataRequired()])
#     roles = QuerySelectMultipleField(
#         query_factory=getroles,
#         get_label='name'
#     )
#     submit = SubmitField('Save')


class ChangePasswordForm(FlaskForm):
    oldpassword = PasswordField('Old password', [validators.DataRequired()])
    newpassword = PasswordField('New password', [validators.DataRequired()])
    confirmpassword = PasswordField('Confirm password', [validators.DataRequired()])


class LoginForm(FlaskForm):
    email = StringField('Email', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    remember = BooleanField('Remember')


class RegisterForm(FlaskForm):
    email = EmailField('Email', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
