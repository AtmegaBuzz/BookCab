from flask_wtf import FlaskForm
from wtforms import (
    EmailField,
    PasswordField,
    StringField,
    SubmitField
)
from wtforms.validators import DataRequired,Length,Email


class RegisterForm(FlaskForm):
    
    name =  StringField('Name',validators=[DataRequired(),Length(5)])
    phone_number = StringField("Phone Number",validators=[DataRequired(),Length(12)])
    email = EmailField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired(),Length(8)])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = EmailField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired(),Length(8)])
    submit = SubmitField("Register")
