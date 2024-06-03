from scraping_HAS import scrape_has
import pandas as pd
from sqlalchemy import create_engine, URL


if __name__ == '__main__':
    data_has = scrape_has()

    data = data_has + []

    df = pd.DataFrame(data_has, columns=['id', 'Title', 'Date', 'Url'])
    df.to_json(path_or_buf="./data_HAS.json",
               orient="records")


# url_object = URL.create(
#     "mysql+pymysql",
#     "root",
#     password="j2d8m2s3!",
#     host="http://127.0.0.1:3306",
#     database="sys"
# )
# engine = create_engine(url_object)
# df.to_sql(name='people', con=engine, schema="eventsscraping", if_exists="append")
