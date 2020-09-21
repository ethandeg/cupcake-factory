"""Forms for our demo cupcake app."""
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, Email


class AddCupcakeForm(FlaskForm):
    """Form for adding snacks."""

    flavor = StringField("Flavor", validators=[InputRequired()])
    rating = FloatField("Rating", validators=[InputRequired()])
    size = StringField("Size", validators=[InputRequired()])
    image = StringField("Image URL")


