from flask import Flask, make_response

from webscraping.scraping_HAS import scrape_has

app = Flask(__name__)


@app.route('/events')
def hello_world():  # put application's code here
    return scrape_has()


if __name__ == '__main__':
    app.run()
