from flask import Flask, render_template, redirect, url_for
import random
import post_generator as pg

app = Flask(__name__)

titles = []
posts = []


@app.route("/")
def index():
    global posts

    page_posts = posts

    return render_template('index.html', page_posts=page_posts)


@app.route("/create-post")
def createPost():
    global posts
    post = ''
    post_length = random.randint(5, 25)
    post += ' '.join(pg.generate_text(post_length))
    posts.insert(0, post)

    return redirect('/')