import random


def recommendation(entertainment, user, user_ratings):
    try:
        if len(user_ratings[user]) > 0:
            highest_rated = max(user_ratings[user], key=user_ratings[user].get)
            fav_genre = ''
            fav_tvs = []
            fav_movies = []
            if highest_rated in entertainment['Tv']:
                fav_tv_genre = entertainment['Tv'][highest_rated]['genre']
                fav_genre = fav_tv_genre
                
                # Going inside "entertainment" TV's dictionary with tv series name ('title') being the key and its dictionary ('data') being the value
                for title, data in entertainment['Tv'].items():
                    if data['genre'] == fav_tv_genre:
                        if title not in user_ratings[user]:
                            fav_tvs.append(title)
                recommend_tv = random.choices(fav_tvs)

            elif highest_rated in entertainment['Movies']:
                fav_movie_genre = entertainment['Movies'][highest_rated]['genre']
                fav_genre = fav_movie_genre

                # Going inside "entertainment" Movies's dictionary with the movie name ('name') being the key and its dictionary ('info') being the value
                for name, info in entertainment['Movies'].items():
                    if info['genre'] == fav_movie_genre:
                        if name not in user_ratings[user]:
                            fav_movies.append(name)
                recommend_movie = random.choices(fav_movies)

            if len(fav_tvs) < 1 and len(fav_movies) >= 1:
                print(f'Since you enjoy {fav_genre} the most, you should try these movies: ')
                print(', '.join(recommend_movie))

            elif len(fav_tvs) >= 1 and len(fav_movies) < 1:
                print(f'Since you enjoy {fav_genre} the most, you should try these tv shows:')
                print(', '.join(recommend_tv))

            else:
                print(f'Since you enjoy {fav_genre} the most, you should try these movies:')
                print(', '.join(recommend_movie))
                print('You should also try these tv shows:')
                print(', '.join(recommend_tv))
                print(f'Since you enjoy {fav_genre} the most, you should try:')
        else:
            genres = []
            for details in entertainment['Tv'].values():
                if details['genre'] not in genres:
                    genres.append(details['genre'])
            print(', '.join(genres))

            while True:
                favorite = input("What's your favorite genre?: ")
                if favorite in genres:
                    tv_shows = []
                    movies = []
                    print(f'Since your favorite genre is {favorite}, you should try these tv shows:')
                    for tv, desc in entertainment['Tv'].items():
                        if desc['genre'] == favorite:
                            tv_shows.append(tv)
                    print(', '.join(tv_shows))
                    
                    print('You should also try these movies:')
                    for movie, information in entertainment['Movies'].items():
                        if information['genre'] == favorite:
                            movies.append(movie)
                    print(', '.join(movies))
                    break
                else:
                    print('Not found in display of genres')
    except ValueError:
        print('Invalid input, try again')
    


