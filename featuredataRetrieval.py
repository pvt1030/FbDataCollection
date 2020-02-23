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

        friends = record["friends"]
        if 'friends' in friends:
            no_of_friends = friends["friends"]["summary"]["total_count"]

        groups = record["groups"]
        no_of_groups = 0
        for x in groups:
            no_of_groups += 1
        print(f'no.of groups: {no_of_groups}')

        likes = record["likes"]
        no_of_likes = 0
        for y in likes:
            no_of_likes += 1
        # print(f'total no.of likes : {no_of_likes}')

        posts = record["posts"]
        no_of_photos = 0
        for m in posts:
            if 'full_picture'in m:
                no_of_photos += 1

        print(colored('total no.of photos', 'red'))
        print(no_of_photos)

        gender = record["gender"]["gender"]

        languages = record["languages"]
        no_of_languages = 0
        for n in languages:
            no_of_languages += 1

        albums = record["albums"]["data"]
        no_of_albums = 0
        for n in albums:
            no_of_albums += 1
        print(colored('total no.of albums', 'red'))
        print(no_of_albums)

        no_of_favorite_teams = 0
        favorite_teams = record["favorite_teams"]
        if 'favorite_teams' in favorite_teams:
            for n in favorite_teams['favorite_teams']:
                no_of_favorite_teams += 1
        print(colored('total no.of favorite teams', 'red'))
        print(no_of_favorite_teams)

        no_of_favorite_athletes = 0
        favorite_athletes = record["favorite_athletes"]
        if 'favorite_athletes' in favorite_athletes:
            for n in favorite_athletes['favorite_athletes']:
                no_of_favorite_athletes += 1
        print(colored('total no.of favorite athletes', 'red'))
        print(no_of_favorite_athletes)

        music = record["music"]["data"]
        no_of_interested_music = 0
        for n in music:
            no_of_interested_music += 1
        print(colored('total no.of music liked', 'red'))
        print(no_of_interested_music)

        birthday = record["birthday"]
        if birthday:
            displayed_birthday = True
        else:
            displayed_birthday = False
        print(colored('birthday', 'red'))
        print(birthday)

        quotes = record["quotes"]
        if 'quotes' in quotes:
            quotes_displayed = True
        else:
            quotes_displayed = False


        posts = record["posts"]
        no_of_posts = 0
        no_of_posts_with_description = 0
        no_of_posts_without_description = 0

        for m in posts:
            no_of_posts += 1
            if 'message' in m:
                no_of_posts_with_description += 1
            else:
                no_of_posts_without_description += 1

        retrieved_data = {
            "id": id_dict,
            "name": name_dict,
            "friends": no_of_friends,
            "groups": no_of_groups,
            "likes": no_of_likes,
            "photos": no_of_photos,
            "gender": gender,
            "no_of_languages": no_of_languages,
            "no_of_albums": no_of_albums,
            "no_of_favorite_teams": no_of_favorite_teams,
            "no_of_favorite_athletes": no_of_favorite_athletes,
            "no_of_interested_music": no_of_interested_music,
            "birthday": displayed_birthday,
            "quotes": quotes_displayed,
            "no_of_posts": no_of_posts,
            "no_of_posts_with_description": no_of_posts_with_description,
            "no_of_posts_without_description":  no_of_posts_without_description

        }

        print(type(retrieved_data['name']))
        print(colored('retrieved data', 'green'))
        print(retrieved_data)

        profile = retrieved_data
        print(type(profile))
        client = MongoClient('mongodb://localhost:27017')
        db = client.user2  # new database user2created
        users = db.featureSelection  # featureSelection collection created
        result = users.insert_one(profile)


if __name__ == "__main__":
    get_db_data()
    remake_data()
    #create_db()
