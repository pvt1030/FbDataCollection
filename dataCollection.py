import json
import facebook
from pymongo import MongoClient


def get_api_data():

    access_token = "EAANHHQ2b32kBAFalLtf6AUW8OimBVbqU2t1FgWJlitKiGoehoZBYZCAMCmzNmTzLmO41nax7DRnARfjIbJfZAZCaI5pW9oKCPftJRzElDpx7yUkL40rTsemJ5Y0ZCxvkJ28ZCERcx54zkagsWxcf9LRG0KpffKFoLqZBeuoz1XGrDHYfKkddoRDZCPecqvRGENkZD"
    graph = facebook.GraphAPI(access_token=access_token)

    # total_set = {}
    # total_groups = []
    # total = graph.get_object('me', fields='id,'
    #                                       'name,'
    #                                       'friends,'
    #                                       'groups,'
    #                                       'likes{name,id,created_time,category,about},'
    #                                       'photos{from,name,picture,tags}, '
    #                                       'movies{name,id,description,genre}')
    # print(type(total))
    # total_json = json.dumps(total, indent=4)
    # print(total_json)

    # ID = total.get(id)
    # name = total.get('name')
    # friends = total.get('friends')
    # likes = total.get('likes')
    # groups = total.get('groups')
    # photos= total.get('photos')
    # movies = total.get('movies')
    #
    # print(likes)
    #
    # a = {
    #     'id': ID,
    #     'name': name,
    #     'friends': friends,
    #     'groups': groups,
    #     'likes': likes,
    #     'photos': photos,
    #     'movies': movies
    # }
    # print(a)

    # for element, value in total.items():
    #     print(element, ":", value)
    #     print(type(value))
    #     g = value.get('data')
    #
    #     while k<len(total):
    #         for i in g:
    #             a[k].append(i)
    #             k+=1
    #
    #         print(type(a[k]))
    # while 'next' in a.values():
    #     total1 = graph.get_connections("me",
    #                              'likes?fields=name,id,created_time,category,about&after=' + likes['paging']['cursors']['after'],
    #                              'photos?fields=from,name,picture,tags&after=' + photos['paging']['cursors']['after'],
    #                              'movies?fields=name,id,description,genre&after=' + movies['paging']['cursors']['after'],
    #                              'groups?after=' + groups['paging']['cursors']['after'],)
    #
    #
    #     print(json.dumps(totall, indent=4))
    #








####groups data#######

    total_groups = []
    groups = graph.get_connections('me', 'groups')
    groups_json = json.dumps(groups)
    g = groups.get('data')
    for i in g:
        total_groups.append(i)
    while 'next' in groups_json:

        groups = graph.get_connections("me", 'groups?after=' + groups['paging']['cursors']['after'])

        g = groups.get('data')
        for i in g:
            total_groups.append(i)

        groups_json = json.dumps(groups)
        total_groups_json = json.dumps(total_groups, indent=4)
        print(total_groups_json)

    total_likes = []
    likes = graph.get_connections('me', 'likes?fields=name,id,created_time,category,about')
    likes_json = json.dumps(likes)

    g = likes.get('data')
    for i in g:
        total_likes.append(i)

    while 'next' in likes_json:

        likes = graph.get_connections("me", 'likes?fields=name,id,created_time,category,about&after=' + likes['paging']['cursors']['after'])

        g = likes.get('data')
        for i in g:
            total_likes.append(i)

        likes_json = json.dumps(likes)
        total_likes_json = json.dumps(total_likes, indent=4)
        print(total_likes_json)

    total_photos = []
    photos = graph.get_connections('me', 'photos?fields=from,name,picture,tags')
    photos_json = json.dumps(photos)

    g = photos.get('data')
    for i in g:
        total_photos.append(i)

    while 'next' in photos_json:

        photos = graph.get_connections("me", 'photos?fields=from,name,picture,tags&after=' +
                                       photos['paging']['cursors']['after'])

        g = photos.get('data')
        for i in g:
            total_photos.append(i)

        photos_json = json.dumps(photos)
        total_photos_json = json.dumps(total_photos, indent=4)
        print(total_photos_json)

    total_movies = []
    movies = graph.get_connections('me', 'movies?fields=name,id,description,genre')
    movies_json = json.dumps(movies)
    g = movies.get('data')
    for i in g:
        total_movies.append(i)
    while 'next' in movies_json:

        movies = graph.get_connections("me", 'movies?fields=name,id,description,genre&after=' +
                                       movies['paging']['cursors']['after'])

        g = movies.get('data')
        for i in g:
            total_movies.append(i)

        movies_json = json.dumps(movies)
        total_movies_json=json.dumps(total_movies, indent=4)
        print(total_movies_json)

    # data = graph.get_connections("me", '?fields=id,name,friends')
    id = graph.get_object('me',fields='id')
    name = graph.get_object('me',fields='name')

    profile = {"id": id,
               "name": name,
               "groups": total_groups,
               "likes": total_likes,
               "photos": total_photos,
               "movies": total_movies
               }

    df = json.dumps(profile, indent=4)
    print(profile)
    print(df)

    return profile


def create_db():
    profile = get_api_data()
    print(type(profile))
    client =MongoClient('mongodb://localhost:27017')
    db = client.user  # new database fbdb created
    users = db.profile  # collection created
    print(users)

    result = users.insert_one(profile)
    print(result)

# def extract_required_data():
#     new_profile = get_api_data()
#     print(new_profile)
#     df = json.dumps(new_profile, indent=4)
#     print(df)
#
#     id = new_profile.get('id').get('id')
#     print(f'id : {id}')
#
#     name = new_profile.get('name').get('name')
#     print(f'name : {name}')
#
#     no_of_friends = new_profile.get('friends').get('summary').get('total_count')
#     print(f'no_of_friends : {no_of_friends}')
#
#     groups = new_profile.get('groups')
#     no_of_groups = 0
#     for x in groups:
#         no_of_groups += 1
#     print(f'no.of groups: {no_of_groups}')
#
#     likes = new_profile.get('likes')
#     liked_movies = []
#     for x in likes:
#         if x["category"] == "movie":
#             movies_liked = x["name"]
#             liked_movies.append(movies_liked)
#             print(movies_liked)
#
#     no_of_likes = 0
#     for y in likes:
#         no_of_likes += 1
#     print(f'total no.of likes : {no_of_likes}')
#
#     photos = new_profile.get('photos')
#
#     uploaded_photos = 0
#     being_tagged_photos = 0
#     for x in photos:
#         person_posted = x["from"]["name"]
#             # x["from"].get("name")
#         tags = x["tags"]["data"]
#             # x["tags"].get('data')
#
#         for y in tags:
#             tagged_user = y["name"]
#
#             if person_posted == name:
#                 uploaded_photos += 1
#             elif person_posted != name and tagged_user == name:
#                 being_tagged_photos += 1
#
#     print(f'user uploaded no.of photos: {uploaded_photos}')
#     print(f'no.of times user being tagged in other photos : {being_tagged_photos}')
#
#     movies = new_profile.get('movies').data
#     print('movies interested')
#     movies_interested = []
#     for x in movies:
#         movie_name = x.name
#         movies_interested.append(movie_name)
#         if "genre" in movies:
#             movie_genre = x.genre
#             print(f'movie genre: {movie_genre}')
#         print(f' {movie_name}')
#
#     model_data = {
#         "id": id,
#         "name": name,
#         "no_of_friends": no_of_friends,
#         "no_of_groups": no_of_groups,
#         "no_of_likes": no_of_likes,
#         "no_of_uploaded photos": uploaded_photos,
#         "no_of tagged_photos": being_tagged_photos,
#         "liked_movies": liked_movies,
#         "movies_interested": movies_interested
#     }
#
#     print(type(model_data))
#     print(model_data)
#     client =MongoClient('mongodb://localhost:27017')
#     db = client.extraxcteddata  # new database fbdb created
#     modeldata = db.model_data  # collection created
#
#     result = modeldata.insert_one(model_data)
#     print(result)


if __name__ == "__main__":
    get_api_data()
    create_db()
    # extract_required_data()
