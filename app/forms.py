from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, FloatField, SelectField
from wtforms.validators import DataRequired, ValidationError
# CUSTOM VALIDATORS

def custom_username_validator(form, field):
    if len(field.data) == 0:
        raise ValidationError('Please enter a value.')

def custom_password_validator(form, field):
    if len(field.data) == 0:
        raise ValidationError('Please enter a value.')
    
# FORM

class LoginForm(FlaskForm):
    username = StringField('username', validators=[custom_username_validator])
    password = PasswordField('password', validators=[custom_password_validator])
    submit = SubmitField('Login')

class AddExpenseForm(FlaskForm):
    def __init__(self, category_choices, payment_method_choices):
        super().__init__()
        
        self.category_choices = category_choices
        self.payment_method_choices = payment_method_choices

    amount = FloatField('Amount', validators=[DataRequired()])
    date = DateField('Date')
    category = SelectField('Category', choices=[])
    payment_method = SelectField('Payment Method', choices=[])
    submit = SubmitField('Add New')

class AddCategoryForm(FlaskForm):
    name = StringField('Category', validators=[DataRequired()])
    submit = SubmitField('Add')

class AddPaymentMethodForm(FlaskForm):
    name = StringField('Payment Method', validators=[DataRequired()])
    submit = SubmitField('Add')