from pymongo import MongoClient
from termcolor import colored

def get_db_data():
    connection = MongoClient('localhost', 27017)
    db = connection.user2
    data = db.profilemod
    data_set = data.find()
    return data_set


def remake_data():
    data_list = get_db_data()
    for record in data_list:
        id_dict = record['id']['id']
        name_dict = record['name']['name']
        posts = record["posts"]
        profile_picture_id = record["profile_picture"]["id"]
        profile_picture_url = record["profile_picture"]["picture"]["data"]["url"]

        photo_array = []
        full_picture = ''
        for x in posts:
            post_id = x["id"]
            if 'full_picture'in x:
                full_picture = x["full_picture"]
            if 'from' in x:
                posted_by = x["from"]["name"]
            if "created_time" in x:
                date = x["created_time"]

            photo_details = {
                "post_id": post_id,
                "full_picture": full_picture,
                "posted_by": posted_by,
                "date": date
            }

            photo_array.append(photo_details)

        retrieved_data = {
            "id": id_dict,
            "name": name_dict,
            "photos": photo_array,
            "profile_picture_id": profile_picture_id,
            "profile_picture_url": profile_picture_url

            }

        print(colored('ID name and photos uploaded', 'blue'))
        print(retrieved_data)

        profile = retrieved_data
        print(type(profile))
        client = MongoClient('mongodb://localhost:27017')
        db = client.user2  # new database user2  created
        idPost = db.IdAndPhoto  # collection IdAndPhotos created
        result = idPost.insert_one(profile)


if __name__ == "__main__":
    get_db_data()
    remake_data()
    # create_db()
