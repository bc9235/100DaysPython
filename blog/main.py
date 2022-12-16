from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

posts = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
content = []
for item in posts:
    post = Post(id=item["id"], title=item["title"], subtitle=item["subtitle"], body=item["body"])
    content.append(post)


@app.route('/')
def home():
    return render_template("index.html", content=content)


@app.route('/post/<int:id>')
def post(id):
    post = content[id]
    return render_template("post.html", content=post)


if __name__ == "__main__":
    app.run(debug=True)
