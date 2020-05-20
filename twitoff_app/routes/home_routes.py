# twitoff_app/routes/home_routes.py

from flask import Blueprint, render_template

# Define home routes
home_routes = Blueprint("home_routes", __name__)

# Decorating the home routes object
# Adding routes to our bluepront object we called home_routes

# When the user visits the home page
@home_routes.route("/")
def index():
    return render_template('prediction_form.html')

# When user visits /hello
@home_routes.route("/hello")
def hello():
    x = 2 + 2
    return f"Hello World! {x}"

# When the user visits /about
@home_routes.route("/about")
def about():
    return "About me"

    