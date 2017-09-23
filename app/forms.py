from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class SearchForm(Form):
    search_term = StringField('search_term', validators=[DataRequired()])
