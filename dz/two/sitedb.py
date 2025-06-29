import sqlite3
import os
from flask import Flask, render_template, flash, request, g

from dz.two.fdatabase import FDataBase

# конфигурация
DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = '5cf814f79d3a9b95e9113383f41814a07fbd0b05'


app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, "flsk.db")))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource("sq_db.sql", "r") as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', menu=dbase.get_menu())


@app.route("/add_post", methods=["POST", "GET"])
def add_post():
    db = get_db()
    dbase = FDataBase(db)

    return render_template('add_post.html', menu=dbase.get_menu())


@app.route("/about")
def about():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('about.html', menu=dbase.get_menu())


@app.route("/psychology")
def psychology():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('psychology.html', menu=dbase.get_menu())

@app.route("/contact")
def contact():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('contact.html', menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run()

