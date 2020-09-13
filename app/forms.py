from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class emptyBlank(FlaskForm):
    url = StringField('Your url', validators=[DataRequired()])
    submit = SubmitField('Make it shorter')
    custom = StringField('Cusomize url')
