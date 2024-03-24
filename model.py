"""Expenses Tracker Model"""
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class User(db.Model):
    """Users"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    # shows left over money for the month after expenses whether it be negative or positive
    balance = db.Column(db.Integer)
    

    # relationships
    # a user can have more than one income
    user_incomes = db.relationship("Income", back_populates="user")
    # a user can have multiple expenses
    user_expenses = db.relationship("Expense", back_populates="user")
    # a user can have more than one savings (normal, HYSA, 401(?))
    user_savings = db.relationship("Savings", back_populates="user")

    # add password hashing functions
    # or OAuth since using google calendar

    def __repr__(self):
        return f"<User user_id={self.user_id} username={self.username}>"


class Income(db.Model):
    """User's Income"""

    __tablename__ = "incomes"

    income_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    source = db.Column(db.String, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    # ex) weekly, biweekly, monthly income
    reoccuring = db.Column(db.String)

    user = db.relationship("User", back_populates="user_incomes")

    def __repr__(self):
        return f'<Income income_id={self.income_id} source={self.source}>'
    

class Expense(db.Model):
    """User's Expenses"""

    __tablename__ = "expenses"

    expense_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    name = db.Column(db.String, nullable=False)
    due_date = db.Column(db.Date)
    # monthly expenses, rent, car notes, internet and electric bills etc
    reoccuring = db.Column(db.String, default="no")

    user = db.relationship("User", back_populates="user_expenses")


    def __repr__(self):
        return f'<Expense expense_id={self.expense_id} name={self.name}>'



class Savings(db.Model):
    """User's Savings accounts or saving for purchases"""

    __tablename__ = "savings"

    savings_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    name = db.Column(db.String, nullable=False)
    balance = db.Column(db.Integer)

    user = db.relationship("User", back_populates="user_savings")

    def __repr__(self):
        return f'<Savings savings_id={self.savings_id} name={self.name}>'




def connect_to_db(app, db_name):
    """Connect to database."""

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{db_name}"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)