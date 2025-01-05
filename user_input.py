
def add_user_rating(user, user_ratings, entertainment):
    try:
        while True:
            choose = input('Wanna rate a movie or tv?: ').lower()
            if choose != 'movie' and choose != 'tv':
                print('Must be "tv" or "movie"')
            else:
                if choose == 'tv':
                    print(', '.join(list(i for i in entertainment['Tv'] if i not in user_ratings[user])))
                    while True:
                        tv = input('Which tv series would you like to rate?: ').title()
                        if tv not in entertainment['Tv']:
                            print('Not found, try again')
                        else:
                            tv_rating = float(input(f'Enter a rating between 1 and 10 for {tv}: '))
                            if tv_rating < 1:
                                user_ratings[user][tv] = 1.0
                            elif tv_rating > 10:
                                user_ratings[user][tv] = 10.0
                            else:
                                user_ratings[user][tv] = tv_rating
                        break
                break
            if choose == 'movie':
                print(', '.join(list(i for i in entertainment['Movies'] if i not in user_ratings[user])))
                while True:
                    movie = input('Which movie would you like to rate?: ').title()
                    if movie not in entertainment['Movies']:
                        print('Movie not found, try again')
                    else:
                        movie_rating = float(input(f'Enter a rating between 1 and 10 for {movie}: '))
                        if movie_rating < 1:
                            user_ratings[user][movie] = 1.0
                        elif movie_rating > 10:
                            user_ratings[user][movie] = 10.0
                        else:
                            user_ratings[user][movie] = movie_rating
                    break
    except ValueError:
        print('Numbers only')
