"""Expense Tracker Server"""

from flask import Flask, render_template, request, session, redirect, jsonify
from model import connect_to_db, db, User, Income, Expense, Savings
import os
import datetime

app = Flask(__name__)

# add google calendar keys

# helper function for subtracting/adding income and expenses(?)

@app.route('/')
def home():
    """View Homepage."""

    return render_template("homepage.html")

# need routes for create account/OAuth

# need routes for log in/returning users

@app.route('/dashboard')
def dashboard():
    """View the Dashboard"""
    # this will have the budget tracker (forms)

    return render_template("dashboard.html")

@app.route('/calendar')
def calendar():
    """View the Calendar"""

    return render_template("calendar.html")


# need routes to create income
    # edit/delete income
    # take from income

# route to create expenses
    # edit/delete expenses

# route to create savings
    # edit/delete savings
