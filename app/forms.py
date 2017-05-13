from flask.ext.wtf import Form
from wtforms import PasswordField,TextAreaField,StringField,validators

class LoginForm(Form):
    login = StringField('login', [validators.Length(min=4 , max = 25)])
    password = PasswordField('password',[validators.required(),validators.Length(min = 4, max = 25)])
