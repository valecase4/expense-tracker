from . import db
from flask_login import UserMixin

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    def __repr__(self) -> str:
        return f'<User {self.username}>'
    
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    category = db.Column(db.String(255), nullable=False)
    payment_method = db.Column(db.String(255), nullable=False)

    def __init__(self, amount, date, category, payment_method) -> None:
        self.amount = amount
        self.date = date
        self.category = category
        self.payment_method = payment_method

    def __repr__(self) -> str:
        return f'Expense nr. {self.id} - {self.amount} - {self.date} - {self.category} - {self.payment_method}'
        

    
