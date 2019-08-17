from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class QueryForm(FlaskForm):
    location = StringField('Location', validators=[DataRequired()])
    food_type = StringField('Food Type', validators=[DataRequired()])
    submit = SubmitField('Find me a place to eat!')
    
