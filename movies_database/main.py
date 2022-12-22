from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.environ["API_KEY"]
SEARCH_URL = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query="

app = Flask(__name__)
app.config['SECRET_KEY'] = superdupersecretkey
Bootstrap(app)

# Create database
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db.init_app(app)


# Set up table
class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


# Set up add form
class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


# Set up rating form
class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")


# Create table
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    all_movies = Movies.query.order_by(Movies.rating.desc()).all()
    # Assign rank to movies based on rating
    for movie in all_movies:
        movie.ranking = all_movies.index(movie) + 1
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    # Create form object
    form = RateMovieForm()
    # Get movie id and entry from database
    movie_id = request.args.get("id")
    movie = Movies.query.get(movie_id)
    # Edit data
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete():
    # Delete entry from database
    movie_id = request.args.get("id")
    movie_delete = Movies.query.get(movie_id)
    db.session.delete(movie_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    # Create form object
    form = AddMovieForm()
    if request.method == "POST":
        title = form.title.data
        movie_url = f"{SEARCH_URL}/{title}"
        movie_details = requests.get(url=movie_url).json()["results"]
        return render_template("select.html", titles=movie_details)
    return render_template("add.html", form=form)


@app.route("/find")
def find():
    movie_id = request.args.get("id")
    if movie_id:
        # Send request to API for movie details
        details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
        movie_details = requests.get(url=details_url).json()
        image_url = f"https://image.tmdb.org/t/p/original{movie_details['poster_path']}"
        # Create new movie object
        new_movie = Movies(
            title=movie_details["title"],
            year=movie_details["release_date"].split("-")[0],
            description=movie_details["overview"],
            rating=0,
            ranking=0,
            review="",
            img_url=image_url,
        )
        # Save new movie to database
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
