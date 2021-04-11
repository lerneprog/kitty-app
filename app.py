from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# Katzenbilder Liste
images = [
    "https://kurse.lerneprogrammieren.de/wp-content/uploads/katze1.jpg",
	"https://kurse.lerneprogrammieren.de/wp-content/uploads/katze2.jpg",
	"https://kurse.lerneprogrammieren.de/wp-content/uploads/katze3.jpg",
	"https://kurse.lerneprogrammieren.de/wp-content/uploads/katze4.jpg",
	"https://kurse.lerneprogrammieren.de/wp-content/uploads/katze5.jpg",
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
