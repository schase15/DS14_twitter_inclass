# Entry point into a directory

# web_app/__init__.py

from flask import Flask

from twitoff_app.routes.home_routes import home_routes
from twitoff_app.routes.book_routes import book_routes


# Initialize our app
def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    return app

# Create instance of our app and return our app
if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
