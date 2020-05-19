# web_app/routes/book_routes.py

from flask import Blueprint, jsonify, request, render_template, flash, redirect
from twitoff_app.models import db, Book
book_routes = Blueprint("book_routes", __name__)

# The data in jason format - computer friendly
@book_routes.route("/books.json")
def list_books():
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
    ]
    return jsonify(books)

# Present books data in an html user friendly page
@book_routes.route("/books")
def list_books_for_humans():
    # books = [
    #     {"id": 1, "title": "Book 1"},
    #     {"id": 2, "title": "Book 2"},
    #     {"id": 3, "title": "Book 3"},
    # ]

    book_records = Book.query.all()
    print(book_records)

    return render_template("books.html", message="Here's some books", books=book_records)

# Define new_books route
@book_routes.route("/books/new")
def new_book():
    return render_template("new_book.html")

@book_routes.route("/books/create", methods=["POST"])
def create_book():
    print("FORM DATA:", dict(request.form))

    new_book = Book(title=request.form["title"], author_id=request.form["author_name"])


    db.session.add(new_book)
    db.session.commit()

 #return jsonify({
    #    "message": "BOOK CREATED OK",
    #    "book": dict(request.form)
    #})
    flash(f"Book '{new_book.title}' created successfully!", "success")
    return redirect("/books")
