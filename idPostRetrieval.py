from pymongo import MongoClient
from termcolor import colored

def get_db_data():
    connection = MongoClient('localhost', 27017)
    db = connection.user2
    data = db.sara
    data_set = data.find()
    return data_set


def remake_data():
    data_list = get_db_data()
    for record in data_list:
        id_dict = record['id']['id']
        name_dict = record['name']['name']
        posts = record["posts"]
        posted_by = msg = des = nam = date = ' '
        post_data = []
        for x in posts:
            post_id = x["id"]
            if 'from' in x:
                posted_by = x["from"]["name"]
            if "message" in x:
                msg = x["message"]
            if "description" in x:
                des = x["description"]
            if "name" in x:
                nam = x["name"]
            if "created_time" in x :
                date = x["created_time"]

            post_details = {
                "post_id": post_id,
                "message": msg,
                "description": des,
                "name": nam,
                "posted_by": posted_by,
                "date": date

            }

            post_data.append(post_details)

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
        idPost = db.saraPosts  # IdAndPosts collection created
        result = idPost.insert_one(profile)


if __name__ == "__main__":
    get_db_data()
    remake_data()
    # create_db()