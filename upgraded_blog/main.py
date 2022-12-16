from flask import Flask, render_template
import requests

app = Flask(__name__)

posts = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()


@app.route("/")
def home():
    return render_template("index.html", content=posts)


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def post(index):
    requested_post = None
    for entry in posts:
        if entry["id"] == index:
            requested_post = entry
    return render_template("post.html", content=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
