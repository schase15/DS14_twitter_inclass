# Add twitter routes


from flask import Blueprint, jsonify, request, render_template, flash, redirect
from twitoff_app.models import db, Tweet 
twitter_routes = Blueprint("twitter_routes", __name__)

# Present twitter data in an html user friendly page
@twitter_routes.route("/tweets")
def list_tweets_for_humans():
    twitter_records = Tweet.query.all()
    print(twitter_records)

    return render_template("tweets.html", message="Here's some tweets", books=twitter_records)

# Define new_twitter route
@twitter_routes.route("/tweets/new")
def new_tweet():
    return render_template("new_tweets.html")

@twitter_routes.route("/tweets/create", methods=["POST"])
def create_tweet():
    print("FORM DATA:", dict(request.form))

    new_tweet = Tweet(title=request.form["title"], author_id=request.form["author_name"])


    db.session.add(new_tweet)
    db.session.commit()

    return redirect("/tweets")



