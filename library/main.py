from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Create database
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-database.db"
db.init_app(app)


# Set up table
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


# Create table
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    # Display all books in database
    all_books = Books.query.all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # Get data from form and add to database
        new_book = Books(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    else:
        return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    # Edit data on form submission
    if request.method == "POST":
        book_id = request.form["id"]
        update = Books.query.get(book_id)
        update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))
    # Display book info to edit
    book_id = request.args.get("id")
    book_selected = Books.query.get(book_id)
    return render_template("edit.html", book=book_selected)


@app.route("/delete")
def delete():
    # Delete entry from database
    book_id = request.args.get("id")
    book_delete = Books.query.get(book_id)
    db.session.delete(book_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
