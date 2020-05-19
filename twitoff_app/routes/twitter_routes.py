# Add twitter route for inclass app

# web_app/routes/twitter_routes.py

from flask import Blueprint, render_template, jsonify
from twitoff_app.services.twitter_service import api as twitter_api
# from twitoff_app.models import 

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>")
def get_user(screen_name=None):
    print(screen_name)
    user = twitter_api.get_user(screen_name)
    statuses = twitter_api.user_timeline(screen_name, tweet_mode="extended", count=150, exclude_replies=True, include_rts=False)
    
    ## Looked at data in json format to make sure it worked
    # return jsonify({
    #     "user": user._json,
    #     "tweets": [s._json for s in statuses]
    # })

# get existing user 
