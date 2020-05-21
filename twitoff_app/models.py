# web_app/models.py

# Models are used to create the data that is inserted into the tables in the database
# Each Class becomes a table, each attribute on the class becomes a column header
# Each instance of the class becomes a row - the app creates these and inserts them into the correct table in the database

# Imports
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# create objects of SQLAlchemy and Migrate classes from flask
db = SQLAlchemy()

migrate = Migrate()

# Create models - classes with attributes to store data
# Define what type of data can be stored in the column
# Set primary and any other keys

class Book(db.Model):
    #__table_name__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    author_id = db.Column(db.String(128))

class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    screen_name = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String)
    location = db.Column(db.String)
    followers_count = db.Column(db.Integer)
    #latest_tweet_id = db.Column(db.BigInteger)

# Set a user.id as a foreign key
# Create an embedding attribute, we will need this when using the Basilica api
class Tweet(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey("user.id"))
    full_text = db.Column(db.String(500))
    embedding = db.Column(db.PickleType)

    # Creates a relationship between the User and their tweets. So that you can call tweets.user and get user info
    # or call user.tweets to get tweet info
    user = db.relationship("User", backref=db.backref("tweets", lazy=True))


# Converts our database records into json format so the website can read them
def parse_records(database_records):
    """
    A helper method for converting a list of database record objects into a list of dictionaries, so they can be returned as JSON

    Param: database_records (a list of db.Model instances)

    Example: parse_records(User.query.all())

    Returns: a list of dictionaries, each corresponding to a record, like...
        [
            {"id": 1, "title": "Book 1"},
            {"id": 2, "title": "Book 2"},
            {"id": 3, "title": "Book 3"},
        ]
    """
    parsed_records = []
    for record in database_records:
        print(record)
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)
    return parsed_records
