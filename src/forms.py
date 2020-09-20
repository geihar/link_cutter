from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):
    link = StringField(
        render_kw={"placeholder": "Вставьте ссылку"}, validators=[DataRequired()]
    )
    submit = SubmitField()


