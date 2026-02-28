from flask import Flask, render_template, redirect, url_for
import sqlite3
from database import init_db, create_demo_user, DB_NAME
from xp_engine import add_xp, current_level_progress
from mission_engine import generate_missions

app = Flask(__name__)

init_db()
create_demo_user()


def get_user():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = 1")
    user = cursor.fetchone()
    conn.close()
    return user


@app.route("/")
def home():
    user = get_user()
    print("CURRENT USER XP:", user[3])  # DEBUG LINE

    total_xp = user[2]
    progress = current_level_progress(total_xp)

    print("HOME XP DISPLAY:", total_xp)

    return render_template("index.html", progress=progress)


@app.route("/add/<track>/<int:xp>")
def add(track, xp):
    add_xp(1, xp)  
    return redirect("/")


@app.route("/missions/<track>")
def missions(track):
    user = get_user()
    total_xp = user[2]
    progress = current_level_progress(total_xp)

    generated = generate_missions(track, progress["level"])

    return render_template(
        "missions.html",
        missions=generated,
        track=track,
        progress=progress
    )


if __name__ == "__main__":
    app.run(debug=True)