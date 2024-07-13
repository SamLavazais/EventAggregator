from flask import Flask

app = Flask(__name__)


@app.route("/")
def test_scraping():  # put application's code here
    return "home"


if __name__ == '__main__':
    app.run()
