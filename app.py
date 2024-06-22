import logging
from flask import Flask
from flask_apscheduler import APScheduler
from webscraping.data_handling import read_from_json, save_to_json, scrape_data
from webscraping.scraping import scrape_cnsa
from webscraping.timer import Timer

app = Flask(__name__)

logging.basicConfig(
    filename=f'{app.root_path}/log/record.log',
    level=logging.INFO,
    format=f'%(asctime)s %(levelname)s %(name)s %('f'threadName)s : %(message)s'
)

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


@scheduler.task('cron', id='do_job_2', hour="8", minute='30')
@Timer(
    text="Database was updated in : {:.2f} seconds.",
    logger=app.logger.info
)
def update_database():
    data_to_store = scrape_data()
    print("data to store après scraping : ")
    print(data_to_store[0])
    save_to_json(data_to_store, app.root_path)
    app.logger.info('data successfully updated.')


@app.route('/test_scraping')
def test_scraping():  # put application's code here
    return scrape_cnsa()


@app.route('/manual_update')
def update():  # put application's code here
    update_database()
    return "données mises à jour"


@app.route('/events')
def get_all_events():  # put application's code here
    return read_from_json(app.root_path)


if __name__ == '__main__':
    app.run(host="localhost", port=5001)
