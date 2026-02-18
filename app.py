from flask import Flask, render_template, redirect, url_for
from database import init_db, create_demo_user
from xp_engine import add_xp, current_level_progress
import sqlite3
from database import DB_NAME

app = Flask(__name__)

init_db()
create_demo_user()


def get_demo_user():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", ("demo",))
    user = cursor.fetchone()
    conn.close()
    return user


@app.route("/")
def home():
    user = get_demo_user()

    if not user:
        return "No user found."

    total_xp = user[2]
    progress = current_level_progress(total_xp)

    return render_template("index.html", progress=progress)


@app.route("/add/<track>/<int:xp>")
def add(track, xp):
    add_xp(1, xp, track)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
