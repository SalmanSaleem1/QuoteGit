from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, TextField
from wtforms.validators import Email, DataRequired


class RegisterForm(FlaskForm):
    name = StringField('Name', [validators.required(DataRequired), validators.Length(min=2, max=25)])
    username = StringField('User Name', [validators.required(DataRequired), validators.Length(min=2, max=25)])
    email = StringField('Email', [validators.required(DataRequired), validators.Email()])
    password = PasswordField('Password', [validators.required(DataRequired)])
    confirm_password = PasswordField('Confirm Password',
                                     [validators.required(DataRequired), validators.EqualTo('password')])
    submit = SubmitField('Login')


class LoginForm(FlaskForm):
    email = StringField('Email', [validators.required(DataRequired), validators.Email()])
    password = PasswordField('Password', [validators.required(DataRequired)])
    submit = SubmitField('Login')
