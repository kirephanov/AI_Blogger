from flask import Flask, render_template, redirect
import random
import post_generator as pg

app = Flask(__name__)

posts = []


@app.route("/")
def index():
    global posts

    page_posts = posts

    return render_template('index.html', page_posts=page_posts)


@app.route("/create-post")
def create_post():
    global posts
    post = ''

    post_length = random.randint(5, 25)
    post += ' '.join(pg.generate_text(post_length))
    posts.insert(0, post)

    return redirect('/')


@app.route("/delete-posts")
def delete_posts():
    global posts

    posts.clear()

    return redirect('/')