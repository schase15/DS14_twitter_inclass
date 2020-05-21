# Entry point into a directory
# Tells the website to run the app
# Define app, tell it the routes to use
# all the supporting code is on other pages that this refers to

# twitoff_app/__init__.py
import os
from dotenv import load_dotenv
from flask import Flask
from twitoff_app.models import db, migrate

# Import all of the routes we have created so the app can run them
from twitoff_app.routes.home_routes import home_routes
from twitoff_app.routes.book_routes import book_routes
from twitoff_app.routes.twitter_routes import twitter_routes
from twitoff_app.routes.stats_routes import stats_routes

load_dotenv()

# Set a path to the database we will be using to store the data
# Do not need to create the page, it will be created automatically by the app

# Fine when running locally
DATABASE_URI =  os.getenv("DATABASE_URI")



# Set up for heroku web app to work
# DATABASE_URI = 

SECRET_KEY = os.getenv("SECRET_KEY", default="super secret") 

# Initialize our app
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY

# Configure the database
    app.config["SQLALCHEMY_DATABASE_URI"] =DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)

# Configure routes - register each route we have with the app
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    app.register_blueprint(twitter_routes)
    app.register_blueprint(stats_routes)
    return app

# Create instance of our app and return our app
if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)

