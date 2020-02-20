from pymongo import MongoClient
from termcolor import colored
import pandas as pd
from datetime import datetime


def get_db_data():
    connection = MongoClient('localhost', 27017)
    db = connection.user2
    data = db.IdAndPosts
    data_set = data.find()
    return data_set


def remake_data():
    data_list = get_db_data()
    for record in data_list:
        id_dict = record['id']
        name_dict = record['name']
        posts = record["posts"]
        posted_by = msg = des = nam = date = ' '
        post_data = []
        for x in posts:
            date = x["date"]
            date_split = date.split("T")
            new_date = date_split[0]
            date_object = datetime.strptime(new_date, '%Y-%m-%d').date()

            if date_object in pd.date_range("2019/01/01", "2020/03/01"):
                post_data.append(x)

        retrieved_data = {
            "id": id_dict,
            "name": name_dict,
            "posts": post_data
            }

        print(type(retrieved_data['posts']))
        print(colored('ID name and posts', 'blue'))
        print(retrieved_data)

        profile = retrieved_data
        print(type(profile))
        client = MongoClient('mongodb://localhost:27017')
        db = client.user2  # database user2 created
        idPost = db.IdAndPosts2019  # IdAndPosts collection created
        result = idPost.insert_one(profile)


if __name__ == "__main__":
    get_db_data()
    remake_data()
    # create_db()
