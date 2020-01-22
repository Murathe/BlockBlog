from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import Required, Email, EqualTo
from ..models import User

class SignUpForm(FlaskForm):
    first_name = StringField('First Name', validators=[Required()])
    last_name = StringField('Last Name', validators=[Required()])
    username = StringField('Username', validators=[Required()])
    email = StringField('Email Address', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required(), EqualTo('password_confirm', message='Password does not match')])
    password_confirm = PasswordField('Confirm your password', validators=[Required()])
    submit = SubmitField('Sign Up')

    # verify username existence/taken
    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('Username not available')

    # Verify email validity on db
    def validate_email(self, data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('Email already registered')

class LoginForm(FlaskForm):
    email = StringField('Email Address', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')