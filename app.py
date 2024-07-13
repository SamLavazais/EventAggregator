# import datetime
# import logging
#
import pandas as pd
from flask import Flask, request
# from flask_apscheduler import APScheduler
# from flask_cors import CORS
# from webscraping.data_handling import read_from_json, save_to_json, scrape_data
# from webscraping.date_parser import date_parser
# from webscraping.scraping import scrape_drees
# from webscraping.timer import Timer
#
app = Flask(__name__)
# CORS(app)


@app.route("/")
def test_scraping():  # put application's code here
    return "home"


#
# logging.basicConfig(
#     filename=f'{app.root_path}/log/record.log',
#     level=logging.INFO,
#     format=f'%(asctime)s %(levelname)s %(name)s %('f'threadName)s : %(message)s'
# )
#
# scheduler = APScheduler()
# scheduler.init_app(app)
# scheduler.start()


# @scheduler.task('cron', id='do_job_2', hour="8", minute='30')
# @Timer(
#     text="Database was updated in : {:.2f} seconds.",
#     logger=app.logger.info
# )
# def update_database():
#     data_to_store = scrape_data()
#     print("data to store après scraping : ")
#     print(data_to_store[0:3])
#     save_to_json(data_to_store, app.root_path)
#     # app.logger.info('data successfully updated.')


@app.get("/test_scraping")
def test_scraping():  # put application's code here
    return "test scraping done."
    # return scrape_drees()


@app.route('/manual_update', methods=['POST'])
def update():  # put application's code here
    return "update done"
    # update_database()
    # return "données mises à jour"


@app.get('/events')
def get_all_events():  # put application's code here
    return 'List all events'
    # data = read_from_json(app.root_path)
    # if request.args.get("deleted", default=False):
    #     return [record for record in data if record['deleted_at'] is not None]
    # else:
    #     return [record for record in data if record['deleted_at'] is None]


@app.post('/events')
def post_event():
    return "new event created"
    # data = request.form
    # new_record = {
    #     'title': data['title'],
    #     'date': data['date'],
    #     'url': data['url'],
    #     'source': data['source'],
    #     'unread': True,
    #     'deleted_at': None
    # }
    # current_data = read_from_json(app.root_path)
    # new_record["id"] = current_data[-1]["id"] + 1
    # new_data = current_data.append(new_record)
    # df = pd.DataFrame(new_data, columns=['id', 'title', 'date', 'url', 'source', 'unread', 'deleted_at'])
    # df.to_json(path_or_buf=f"{app.root_path}/data.json",
    #            orient="records")
    # return new_record


@app.get('/events/<event_id>')
def get_one_event(event_id):
    return "here is one event"
    # # récupérer l'event concerné
    # events = read_from_json(app.root_path)
    #
    # for event in events:
    #     if event['id'] == int(event_id):
    #         return event


@app.patch('/events/<event_id>')
def edit_event(event_id):
    return "one event edited"
    # request_data = request.form
    #
    # events = read_from_json(app.root_path)
    #
    # for event in events:
    #     if event['id'] == int(event_id):
    #         for key in request_data.keys():
    #             new_data = date_parser(request_data[key], "user") if key == "date" else request_data[key]
    #             event[key] = new_data if request_data[key] else False
    #         # sauvegarder les données
    #         df = pd.DataFrame(events, columns=['id', 'title', 'date', 'url', 'source', 'unread', 'deleted_at'])
    #         df.to_json(path_or_buf=f"{app.root_path}/data.json",
    #                    orient="records")
    #
    #         return event


@app.delete('/events/<event_id>')
def delete_event(event_id):
    return "deleted."
    # # récupérer l'event concerné
    # events = read_from_json(app.root_path)
    # # updater la date de suppression
    # for event in events:
    #     if event['id'] == int(event_id):
    #         # delete l'event s'il ne l'est pas déjà OU restaure l'event s'il avait été deleted
    #         if event['deleted_at']:
    #             event['deleted_at'] = None
    #         else:
    #             event['deleted_at'] = datetime.datetime.now().isoformat()
    #         # sauvegarder les données
    #         df = pd.DataFrame(events, columns=['id', 'title', 'date', 'url', 'source', 'unread', 'deleted_at'])
    #         df.to_json(path_or_buf=f"{app.root_path}/data.json",
    #                    orient="records")
    #
    #         return event


if __name__ == '__main__':
    app.run()
