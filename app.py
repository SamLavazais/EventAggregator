from flask import Flask

from webscraping.data_handling import read_from_json

app = Flask(__name__)


@app.route('/coucou')
def hello_world():  # put application's code here
    return app.root_path


@app.route('/events')
def get_all_events():  # put application's code here
    return read_from_json(app.root_path)


if __name__ == '__main__':
    app.run()
