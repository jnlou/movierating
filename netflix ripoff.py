import user_input, movie, account
# sample data, much more to fill in
entertainment = {
     "Tv": {
        'The Walking Dead' : {
         "genre": "Action",
         "director": "Frank Darabont",
         "rating": 4.5
                       },
       'Sweet Home' : {
        'genre' : 'Horror',
        'director' : 'Lee Eung-bok',
        'rating' : 3.0
                     }
           },
     'Movies' : {
          "To All The Boys I've Loved Before": {
           'genre' : 'Comedy',
           'director' : 'Susan Johnson',
           'rating' : 4.2
                   },
          "Rush Hour": {
            "genre": "Comedy",
            "director": "Brett Ratner",
            "rating": 3.8
               },
                }
    }

def main() -> None:
    user_profiles = {
        'Admin' : {'Jay' : 'jayjay1'},
        'Kyra' : 'Kd1$'
    }
    user_ratings = {
        "Jay": {
            "Rush Hour": 4.0,
            "Sweet Home": 3.5,
                },
        "Kyra": {
             "The Walking Dead": 5.0,
                },
                    }
    while True:
        sign = input('Sign In or Sign Up?: ').title().strip()
        if sign == 'Sign Up':
            account.add_acount(user_profiles)
        if sign == 'Sign In':
            while True:
                user = input('Enter username: ').title().strip()
                if user in user_profiles or user in user_profiles['Admin']:
                    if account.login(user, user_profiles):
                        print(f'Hello {user}!')
                        while True:
                            choices = ['A', 'B', 'C', 'D', 'E', 'F']
                            print('''
                                    A. Rate something
                                    B. Get recommendations
                                    C. Manage accounts
                                    D. Display all accounts
                                    E. Log out
                                    F. Exit
                                  ''' )
                            choice = input('Select an option: ').upper().strip()
                            if choice not in choices:
                                print('Invalid input, must be a letter representing one of the displayed options')
                            else:
                                match(choice):

                                    case 'A':
                                        user_input.add_user_rating(user, user_ratings, entertainment)

                                    case 'B':
                                        movie.recommendation(entertainment, user, user_ratings)

                                    case 'C':
                                            print('Account Management')
                                            print('--------')
                                            account_choices = ['A', 'B', 'C', 'D']
                                            print('''
                                                  A. Add account
                                                  B. Remove account
                                                  C. Update account
                                                  D. Show current ratings
                                                  ''')
                                            option = input('Select an option: ').upper().strip()
                                            if option not in account_choices:
                                                print('Invalid input, must be a letter representing one of the displayed options')
                                            elif option == 'A':
                                                account.add_acount(user_profiles)
                                            elif option == 'B':
                                               if account.remove_acount(user, user_profiles) == 'Self':
                                                   print("The current account has been deleted")
                                                   print("Returning to main menu...")
                                                   print()
                                                   break
                                               else:
                                                   print('Account successfully deleted')
                                            elif option == 'C':
                                                account.update_account(user, user_profiles)
                                            elif option == 'D':
                                                account.show_ratings(user, user_ratings)

                                    case 'D':
                                        account.show_accounts(user_profiles)

                                    case 'E':
                                        print('Signing out..')
                                        break
                                    
                                    case 'F':
                                        print('Exiting..')
                                        exit()
                                

                else:
                    print('Username not found, try again')


if __name__ == '__main__':
    main()
