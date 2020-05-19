# Entry point into a directory

# web_app/__init__.py

from flask import Flask
from twitoff_app.models import db, migrate
from twitoff_app.routes.home_routes import home_routes
from twitoff_app.routes.book_routes import book_routes
from twitoff_app.routes.twitter_routes import twitter_routes


# DATABASE_URI = "sqlite:///twitoff_app_99.db" # using relative filepath
DATABASE_URI = "sqlite:////Users/stevenchase/Desktop/Steven/Computer_Science/Lambda/DS14_twitter_inclass/twitoff_development_14.db" # using absolute filepath on Mac (recommended)

# Initialize our app
def create_app():
    app = Flask(__name__)

# Configure the database
    app.config["SQLALCHEMY_DATABASE_URI"] =DATABASE_URI
    db.init_app(app)
    migrate.init_app(app, db)

# Configure routes
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    app.register_blueprint(twitter_routes)

    return app

# Create instance of our app and return our app
if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)

