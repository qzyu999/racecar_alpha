from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,
   SelectField

from wtforms import validators, ValidationError

######
from flask_wtf import FlaskForm,
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class DriverForm(Form):
    """Contact form."""
    name = StringField('Name Of Driver', [
        DataRequired()])
      crash_case = RadioField('Crash case',
         choices = [('S','Soft reset'),('H','Hard reset')])
      track_type = RadioField('Track type',
         choices = [('L','L-track'), ('O','O-track'), ('R','R-track')])
      car_model = RadioField('Car model',
         choices = [('VI','Value Iteration'), ('QL','Q-Learning'),
            ('SA','SARSA')])
    car_number = IntegerField("Car Number", [
         DataRequired(),
         NumberRange(min=0, max=99, message=('Input a number between 0-99.'))])
    submit = SubmitField('Race against the agents!')