from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,SubmitField
from wtforms.validators import DataRequired,NumberRange


class editproduct(FlaskForm):
    editname = StringField('Product Name', validators=[DataRequired()])
    editnum = IntegerField('Quantity', validators=[NumberRange(min=1, max=1000000),DataRequired()])
    editsubmit = SubmitField('Save Changes')


class editlocation(FlaskForm):
    editname = StringField('Location Name', validators=[DataRequired()])
    editsubmit = SubmitField('Save Changes')


class deleteproduct(FlaskForm):
    submit = SubmitField('Delete')

class deletelocation(FlaskForm):
    submit = SubmitField('Delete')