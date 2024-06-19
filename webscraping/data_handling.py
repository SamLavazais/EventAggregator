import pandas as pd
import json

from webscraping.scraping import scrape_has


def scrape_data():
    data_scraped = []
    data_scraped += scrape_has()
    return data_scraped


def save_to_json(data_to_store, app_root_path):
    df = pd.DataFrame(data_to_store, columns=['id', 'Title', 'Date', 'Url'])
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
