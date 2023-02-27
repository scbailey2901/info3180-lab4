from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class UploadForm(FlaskForm):
    image= FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], "Images only!")])