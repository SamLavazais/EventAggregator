import pandas as pd
import json
import copy

from webscraping.scraping import scrape_has


def scrape_data():
    data_scraped = []
    data_scraped += scrape_has()
    return data_scraped


def save_new_records_only(data_to_store, current_data):
    new_data = copy.deepcopy(current_data)
    for record in data_to_store:
        if record["url"] not in [r["url"] for r in current_data]:
            new_data.append({
                "id": new_data[-1]["id"] + 1,
                "title": record["title"],
                "url": record["url"],
                "date": record["date"]
            })
    return new_data


def save_to_json(data_to_store, app_root_path):
    # lire le fichier json
    current_data = read_from_json(app_root_path)

    # checker le fichier json pour chaque élément des data récupérées
    # et si la data est new, l'ajouter aux data
    new_data = save_new_records_only(data_to_store, current_data)

    # sauvegarder à nouveau le fichier json
    df = pd.DataFrame(new_data, columns=['id', 'title', 'date', 'url'])
    df.to_json(path_or_buf=f"{app_root_path}/data.json",
               orient="records")


def read_from_json(app_root_path):
    f = open(f"{app_root_path}\\data.json")
    data_read = json.load(f)
    f.close()
    return data_read


if __name__ == '__main__':
    save_to_json()
    data = read_from_json()
    print(data)

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
