import pandas as pd
import json
import copy

from webscraping.scraping import scrape_has, scrape_firah, scrape_cnsa
from webscraping.timer import Timer


@Timer(text="Data (events) were scraped in : {:.2f} seconds.")
def scrape_data():
    data_scraped = []
    data_scraped += scrape_has()
    data_scraped += scrape_firah()
    data_scraped += scrape_cnsa()

    # implémentation manuelle de l'id (pré-ORM)
    for i, record in enumerate(data_scraped, start=1):
        record['deleted_at'] = None
        record['unread'] = True
        record['id'] = i
    return data_scraped


def save_new_records_only(data_to_store, current_data):
    new_data = copy.deepcopy(current_data)
    # print("data to store avant update : ")
    # print(data_to_store[0])
    for record in data_to_store:
        if record["url"] not in [r["url"] for r in current_data]:
            print("record qui va être sauvegardé : ")
            print(record)
            record["id"] = new_data[-1]["id"] + 1
            new_data.append(record)
    print("new data après update : ")
    print(new_data)

    return new_data


def save_to_json(data_to_store, app_root_path):
    # lire le fichier json
    current_data = read_from_json(app_root_path)
    if current_data:
        # checker le fichier json pour chaque élément des data récupérées
        # et si la data est new, l'ajouter aux data
        new_data = save_new_records_only(data_to_store, current_data)
    else:
        new_data = data_to_store

    # sauvegarder à nouveau le fichier json
    df = pd.DataFrame(new_data, columns=['id', 'title', 'date', 'url', 'source', 'unread', 'deleted_at'])
    df.to_json(path_or_buf=f"{app_root_path}/data.json",
               orient="records")


def read_from_json(app_root_path):
    f = open(f"{app_root_path}\\data.json")
    data_read = json.load(f)
    f.close()
    return data_read


# if __name__ == '__main__':
#     save_to_json()
#     data = read_from_json()
#     print(data)

# from sqlalchemy import create_engine, URL
# url_object = URL.create(
#     "mysql+pymysql",
#     "root",
#     password="j2d8m2s3!",
#     host="http://127.0.0.1:3306",
#     database="sys"
# )
# engine = create_engine(url_object)
# df.to_sql(name='people', con=engine, schema="eventsscraping", if_exists="append")
