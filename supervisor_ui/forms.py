# supervisor_ui/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, FileField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])

class ResolveForm(FlaskForm):
    answer = TextAreaField("Answer", validators=[DataRequired(), Length(min=1, max=5000)])
    attachment = FileField("Attachment (optional)")
