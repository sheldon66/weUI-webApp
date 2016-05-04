from flask_wtf import Form
from wtforms import StringField, DateField, IntegerField, \
    SelectField, PasswordField
from wtforms.validators import DataRequired, Length


class AddProfileForm(Form):


    name = StringField('name', validators=[DataRequired()])
    ID_number = IntegerField('ID',
                        validators = [DataRequired(), Length(min=18, max=18)])
    phone_number = IntegerField('phone',
                        validators = [DataRequired(), Length(min=11, max=11)])
    work = StringField('work', validators=[DataRequired()])
    degree = StringField('degree', validators=[DataRequired()])
