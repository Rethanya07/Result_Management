from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class StudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    register_number = StringField('Register Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Add Student')

class MarkForm(FlaskForm):
    register_number = StringField('Register Number', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    grade = StringField('Grade', validators=[DataRequired()])
    submit = SubmitField('Add Mark')
