from flask_wtf import Form
from flask_wtf.file import FileField
from wtforms import SelectField
from wtforms import TextAreaField
from wtforms import TextField
from wtforms import validators
from catalog.models import Catagory

class CreateCatalogItemForm(Form):
    name = TextField('Name', validators=[validators.DataRequired()])
    author = TextField('Author')
    description = TextAreaField('Description')
    catagory_id = SelectField('Catagory', coerce=int)
    image = FileField('Image File')
