# DS14_twitter_inclass

## Installation

TODO: clone the repo

## Setup

```sh

# Generates migrations directory
FLASK_APP=web_app flask db init 

# Run both when changing the schema:
# Creates the database
FLASK_APP=web_app flask db migrate 

# Creates the specific data
FLASK_APP=web_app flask db upgrade

# Running the web app will insert data into the tables
```

## Usage

```sh
# Run the app using Flask
FLASK_APP=web_app flask run
```
