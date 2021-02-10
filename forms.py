from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange, URL


pet_species = ['dog', 'cat', 'porcupine'] 

class AddPetForm(FlaskForm):
    """Add pet form."""
    name = StringField("Pet Name", validators=[
                       InputRequired(message="Pet Name can't be blank")])
    species = SelectField("Species", choices=[(s, s) for s in pet_species], validators=[
                       InputRequired(message="Species can't be blank")])
    photo_url = StringField("Photo", validators=[URL(require_tld=False, message="Must be a URL"), Optional()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30, message="Age must be between 0-30"), Optional()])
    notes = StringField("About me", validators=[Optional()])


class EditPetForm(FlaskForm):
    """Edit pet form."""
    photo_url = StringField("Photo", validators=[Optional(), URL()])
    notes = StringField("About me", validators=[Optional()])
    available = BooleanField("Pet available?")