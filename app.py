from flask import Flask, render_template
from database import init_db, create_demo_user

app = Flask(__name__)

init_db()
create_demo_user()

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
