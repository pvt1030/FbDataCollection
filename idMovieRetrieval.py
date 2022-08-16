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
        movies = record["movies"]


        movies_interested = []
        for x in movies:
            movie_name = x["name"]
            movies_interested.append(movie_name)
            if "genre" in movies:
                movie_genre = x["genre"]
                print(f'movie genre: {movie_genre}')
                print(f' {movie_name}')

        retrieved_data = {
            "id": id_dict,
            "name": name_dict,
            "movies": movies_interested
            }
        print(type(retrieved_data['name']))
        print(colored('ID name and movie','blue'))
        print(retrieved_data)

        profile = retrieved_data
        print(type(profile))
        client = MongoClient('mongodb://localhost:27017')
        db = client.user2  # new database userdata created
        idMovie = db.IdAndMovie  # collection created
        result = idMovie.insert_one(profile)


if __name__ == "__main__":
    get_db_data()
    remake_data()
    # create_db()
