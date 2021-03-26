from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField, SelectField, PasswordField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('username', validators = [DataRequired()])
    password = PasswordField('password', validators = [DataRequired()])
    standard = SelectField('standard', validators = [DataRequired()], choices = [('eighth', '8th'),
                                                                                ('nine', '9th'),
                                                                                ('ten', '10th'),
                                                                                ('eleven', '11th'),
                                                                                ('twelve', '12th')])
    section = SelectField('section', validators = [DataRequired()], choices = [('A', 'A'),
                                                                                ('B', 'B'),
                                                                                ('C', 'B'),
                                                                                ('D', 'D')])
    submit = SubmitField('submit')

class RegForm(FlaskForm):
    username = StringField('username', validators = [DataRequired()])
    password = PasswordField('password', validators = [DataRequired()])
    confirmpass = PasswordField('password', validators = [DataRequired(), EqualTo('password')])
    standard = SelectField('standard', validators = [DataRequired()], choices = [('eighth', '8th'),
                                                                                ('nine', '9th'),
                                                                                ('ten', '10th'),
                                                                                ('eleven', '11th'),
                                                                                ('twelve', '12th')])
    section = SelectField('section', validators = [DataRequired()], choices = [('A', 'A'),
                                                                                ('B', 'B'),
                                                                                ('C', 'B'),
                                                                                ('D', 'D')])
    submit = SubmitField('submit')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('Username already taken. Use a different one.')