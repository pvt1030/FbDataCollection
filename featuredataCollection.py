import json
import facebook
from pymongo import MongoClient
from termcolor import colored


def get_api_data():
    access_token = "EAACTmfIkNE4BAM2pdSOqWiDFIAU6Lr4Kp7Y0LdWjVDQGHJ84EwCZB3RhnquZBbgCsQX7hFCWoGrOhLOqNWPmLvBRfOm50oRY0R5FTC83UvUs0TjL74YNzOR3xfDP172IhbBrLcqyrpgemc5swPCaO55SRVllOxLqZCaXE5kO871ZCd8UDPEKc4ReDg0w2ZAZCU5DlyZCIW2oa2jHjDGtzwjrwc3GvsLIzbAROW7QEuDOAZDZD"
    graph = facebook.GraphAPI(access_token=access_token)

    # groups data#######
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
        print(colored('total_groups_json','red'))
        print(total_groups_json)

    # likes data#####
    total_likes = []
    likes = graph.get_connections('me', 'likes?fields=name,id,created_time,category,about')
    likes_json = json.dumps(likes)
    g = likes.get('data')
    for i in g:
        total_likes.append(i)
    while 'next' in likes_json:
        likes = graph.get_connections("me", 'likes?fields=name,id,created_time,category,about&after=' +
                                      likes['paging']['cursors']['after'])
        g = likes.get('data')
        for i in g:
            total_likes.append(i)
        likes_json = json.dumps(likes)
        total_likes_json = json.dumps(total_likes, indent=4)
        print(colored('total_likes_json', 'red'))
        print(total_likes_json)

    # # photos data#####
    total_photos = []
    # photos = graph.get_connections('me', 'photos?fields=id,album,created-time,link,from,name,picture,name_tags,image')
    # photos_json = json.dumps(photos)
    # g = photos.get('data')
    # for i in g:
    #     total_photos.append(i)
    # while 'next' in photos_json:
    #     photos = graph.get_connections("me", 'photos?fields=id,album,created-time,link,from,name,name_tags,'
    #                                          'picture,image&after=' + photos['paging']['cursors']['after'])
    #     g = photos.get('data')
    #     for i in g:
    #         total_photos.append(i)
    #     photos_json = json.dumps(photos)
    #     total_photos_json = json.dumps(total_photos, indent=4)
    #     print(colored('total_photos_json', 'red'))
    #     print(total_photos_json)

    # movies data#####
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
        total_movies_json = json.dumps(total_movies, indent=4)
        print(colored('total_movies_json', 'red'))
        print(total_movies_json)

    # data = graph.get_connections("me", '?fields=id,name,friends')

    # posts data####
    total_posts = []
    posts = graph.get_connections('me', 'posts?fields=id,message,'
                                        'created_time,description,from,full_picture,'
                                        'link,message_tags,name', limit=50)
    posts_json = json.dumps(posts)
    g = posts.get('data')
    for i in g:
        total_posts.append(i)
    while 'next' in posts_json:
        posts = graph.get_connections("me", 'posts?fields=id,message,created_time,description,'
                                            'from,full_picture,link,message_tags,name&next=' +
                                      posts['paging']['next'], limit=100)
        g = posts.get('data')
        for i in g:
            total_posts.append(i)
        posts_json = json.dumps(posts)
        total_posts_json = json.dumps(total_posts, indent=4)
        print(colored('total_posts_json', 'red'))
        print(total_posts_json)

    # albums####
    total_albums = []
    albums = graph.get_connections('me', 'albums?fields=id,message,created_time')
    albums_json = json.dumps(albums)
    g = albums.get('data')
    for i in g:
        total_albums.append(i)
    while 'next' in albums_json:
        albums = graph.get_connections("me", 'albums?fields=id,message,created_time&after=' + albums['paging']['cursors']['after'])
        g = posts.get('data')
        for i in g:
            total_albums.append(i)
        albums_json = json.dumps(albums)
        total_albums_json = json.dumps(total_albums, indent=4)
        print(colored('total_albums_json', 'red'))
        print(total_albums_json)

    # music####
    total_music = []
    music = graph.get_connections('me', 'music?fields=id,name,created_time')
    music_json = json.dumps(music)
    g = music.get('data')
    for i in g:
        total_music.append(i)
    while 'next' in music_json:
        music = graph.get_connections("me", 'music?fields=id,name,created_time&after=' + music['paging']['cursors']
                                      ['after'])
        g = music.get('data')
        for i in g:
            total_music.append(i)
        music_json = json.dumps(music)
        total_music_json = json.dumps(total_music, indent=4)
        print(colored('total_music_json', 'red'))
        print(total_music_json)

    # books####
    total_books = []
    books = graph.get_connections('me', 'books?fields=id,name,created_time')
    books_json = json.dumps(books)
    g = books.get('data')
    for i in g:
        total_books.append(i)
    while 'next' in books_json:
        books = graph.get_connections("me",
                                      'books?fields=id,name,created_time&after=' + books['paging']['cursors']['after'])
        g = books.get('data')
        for i in g:
            total_books.append(i)
        books_json = json.dumps(books)
        total_books_json = json.dumps(total_books, indent=4)
        print(colored('total_books_json', 'red'))
        print(total_books_json)



    id = graph.get_object('me', fields='id')
    name = graph.get_object('me', fields='name')
    friends = graph.get_object('me', fields='friends')
    gender = graph.get_object('me', fields='gender')
    languages = graph.get_object('me', fields='languages')
    birthday = graph.get_object('me', fields='birthday')
    quotes = graph.get_object('me', fields='quotes')
    profile_picture = graph.get_object('me', fields='picture')
    favorite_teams = graph.get_object('me', fields='favorite_teams')
    favorite_athletes = graph.get_object('me', fields='favorite_athletes')


    profile = {"id": id,
               "name": name,
               "friends": friends,
               "groups": total_groups,
               "likes": total_likes,
               "photos": total_photos,
               "movies": total_movies,
               "gender": gender,
               "posts": total_posts,
               "languages": languages,
               "albums": albums,
               "favorite_teams": favorite_teams,
               "favorite_athletes": favorite_athletes,
               "music": music,
               "birthday": birthday,
               "quotes": quotes,
               "profile_picture": profile_picture,


               }
    df = json.dumps(profile, indent=4)
    print(profile)
    print(df)
    return profile


def create_db():
    profile = get_api_data()
    print(type(profile))
    client = MongoClient('mongodb://localhost:27017')
    db = client.user2  # new database user created
    user2 = db.sara  # collection created
    print(user2)
    result = user2.insert_one(profile)

    print(result.inserted_id)


if __name__ == "__main__":
    get_api_data()
    create_db()
    # extract_required_data()
