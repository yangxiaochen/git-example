from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "welcome to Bizza Platform"


if __name__ == "__main__":
    app.run()