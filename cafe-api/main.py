from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

API_KEY = "TopSecretAPIKey"

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        """Convert data to dictionary"""
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def random():
    """Pick a random cafe from database"""
    cafes = db.session.query(Cafe).all()
    random_cafe = choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def all_cafes():
    """Return all cafes in database"""
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[entry.to_dict() for entry in cafes])


@app.route("/search")
def search():
    """Search cafes in an area"""
    location = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=location).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


@app.route("/add", methods=["POST"])
def post_new_cafe():
    """Add cafe to the database"""
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    """Update price of coffee for cafe in database"""
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(response={"Error": "Not found.  Cafe does not exist in database."}), 404


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    user_key = request.args.get("api_key")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        if user_key == API_KEY:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Cafe deleted."}), 200
        else:
            return jsonify(response={"error": "That's not allowed, make sure you have the correct api_key."}), 403
    else:
        return jsonify(response={"error": "Cafe does not exist in database."}), 404


if __name__ == '__main__':
    app.run(debug=True)
