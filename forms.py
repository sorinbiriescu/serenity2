from flask_wtf import Form
from wtforms import SelectField, StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired

from models import Jobs

class FilterSearch(Form):
    search_term = SelectField("Search Term", choices=Jobs.get_search_term_choices())
    table_item_action = SelectField("Table Item Action", choices=[('Applied','Applied'),('Interested','Interested'),('Not Interested','Not Interested'),('Clear status','Clear status')])

class SignupForm(Form):
    name = StringField('name', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    submit = SubmitField("Sign up")

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])
    submit = SubmitField("Sign In")