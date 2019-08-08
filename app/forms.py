from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class QueryForm(FlaskForm):
    location = StringField('Location', validators=[DataRequired()])
    food_type = StringField('Food Type')
    price_range = IntegerField('Price Range')
    submit = SubmitField('Find me a place to eat!')
    #lucky = SubmitField('I don\'t care about money! Find a place to eat!')
    
