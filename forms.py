from flask_wtf import Form 
from wtforms import StringField , IntegerField
from wtforms.validators import DataRequired

class RemoveForm (Form):

	empid = IntegerField('id', validators=[DataRequired()])


class NewempForm(Form):
	first_name = StringField('fn',validators=[DataRequired()])
	last_name = StringField('ln',validators=[DataRequired()])
	career_level = StringField('cl',validators=[DataRequired()])
	#age = IntgerField()