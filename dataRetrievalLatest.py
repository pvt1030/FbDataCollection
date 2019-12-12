from pymongo import MongoClient



def get_db_data():
    connection = MongoClient('localhost', 27017)
    db = connection.user
    data = db.profile
    data_set = data.find()
    print(data_set)
    return data_set


def remake_data():
    data_list = get_db_data()
    for record in data_list:
        name_dict = record['name']['name']
        id_dict = record['id']['id']

        groups = record["groups"]
        no_of_groups = 0
        for x in groups:
            no_of_groups += 1
        # print(f'no.of groups: {no_of_groups}')

        likes = record["likes"]
        no_of_likes = 0
        for y in likes:
            no_of_likes += 1
        # print(f'total no.of likes : {no_of_likes}')

        liked_movies = []
        for x in likes:
            if x["category"] == "movie":
                movies_liked = x["name"]
                liked_movies.append(movies_liked)
                # print(movies_liked)

        photos = record["photos"]
        no_of_photos = 0
        for m in photos:
            no_of_photos += 1
        # print(f'total no.of photos :{no_of_photos}')

        uploaded_photos = 0
        being_tagged_photos = 0
        for x in photos:
            person_posted = x["from"]["name"]

            tags = x["tags"]["data"]

            for y in tags:
                tagged_user = y["name"]
                if person_posted == tagged_user:
                    uploaded_photos += 1
                being_tagged_photos = no_of_photos - uploaded_photos
        # print(f'user uploaded no.of photos: {uploaded_photos}')
        # print(f'no.of times user being tagged in other photos : {being_tagged_photos}')

        movies = record["movies"]
        movies_interested = []
        for x in movies:
            movie_name = x["name"]
            movies_interested.append(movie_name)
            if "genre" in movies:
                movie_genre = x["genre"]
                print(f'movie genre: {movie_genre}')
                print(f' {movie_name}')

        friends = record["friends"]
        no_of_friends = friends.get('friends').get('summary').get('total_count')

        retrieved_data = {
            "id": id_dict,
            "name": name_dict,
            "friends": no_of_friends,
            "photos": no_of_photos,
            "groups": no_of_groups,
            "likes": no_of_likes,
            "uploaded_photos": uploaded_photos,
            "tagged_photos": being_tagged_photos
        }

        print(type(retrieved_data['name']))
        print(f'retrieved data {retrieved_data}')

        profile = retrieved_data
        print(type(profile))
        client = MongoClient('mongodb://localhost:27017')
        db = client.userdata  # new database user created
        users = db.profiledata  # collection created
        result = users.insert_one(profile)


if __name__ == "__main__":
    get_db_data()
    remake_data()
    # create_db()
