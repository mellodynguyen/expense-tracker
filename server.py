"""Expense Tracker Server"""

import json
import os
from urllib.parse import quote_plus, urlencode

from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, render_template, request, session, redirect, jsonify
from model import connect_to_db, db, User, Income, Expense, Savings
import datetime

app = Flask(__name__)
app.secret_key = "APP_SECRET_KEY"

#app will need to load the configuration from .env file
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

# helper function for subtracting/adding income and expenses(?) // crud 

@app.route('/')
def home():
    """View Homepage."""

    return render_template("home.html", session=session.get('user'), 
                           pretty=json.dumps(session.get('user'), indent=4))

# need routes for create account/OAuth
oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
)


# when users visit the login route, they'll be redirected to Auth0 to begin
# authentication flow
@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )


#this route is responsible for saving the session after users finish logging in with Auth0
@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("/")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://" + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("home", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )


@app.route('/dashboard')
def dashboard():
    """View the Dashboard"""
    # this will have the budget tracker (forms)

    return render_template("dashboard.html")


# re-visit this after doing budget page
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



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)