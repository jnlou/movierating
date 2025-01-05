

def login(user, user_profiles):
   pw = input('Enter your password: ').strip()
   # Sees if the username the user entered is in the 'user_profiles['Admin']' dictionary first
   for sign, pwrd in user_profiles['Admin'].items():
      # If the username is found, it checks to see if the value of that username is found as well
      if user == sign and pw == pwrd:
         return True

   # If an admin name wasn't found, it goes through to see if the username is in the 'user_profiles' dictionary
   for log, password in user_profiles.items():
      # If the username is found, it checks to see if the value of that username is found as well
      if user == log and pw == password:
        return True
   # If no name was found anywhere, it returns false and displays that the sign in was unsuccessful     
   print('Sign in unsuccessful')
   return False



def show_accounts(user_profiles):
   print('Admins:')
   for admins in user_profiles['Admin']:
      print(admins)
   print('Users:')
   for name in user_profiles:
      if name != 'Admin':
         print(name)
      

def add_acount(user_profiles) -> None:
   role = input('Will this account be an admin ("y" for yes, anything else for no)?: ').lower().strip()
   if role != 'y':
        name = input('Enter username: ').title().strip()
        pw = input('Enter password: ').strip()
        user_profiles[name] = pw
   else:
      admin_name = input('Enter username: ').title().strip()
      admin_pw = input('Enter password: ').strip()
      user_profiles['Admin'][admin_name] = admin_pw


def remove_acount(user: str, user_profiles) -> None | str:
   if user in user_profiles['Admin']:
      while True:
        try:
            remove = input("Enter a user you'd like to remove: ").title().strip()
            if remove not in user_profiles and remove not in user_profiles['Admin']:
               print('Username not found, try again')
            elif remove == user:
               if user in user_profiles['Admin']:
                  del user_profiles['Admin'][user]
                  # Just used to signify that the user deleted their own account
                  return 'Self'
               else:
                  del user_profiles[user]
                  # Just used to signify that the user deleted their own account
                  return 'Self'
            else:
                if remove in user_profiles['Admin']:
                   del user_profiles['Admin'][remove]
                else:
                   del user_profiles[remove]
            break
        except ValueError:
           print('Invalid input, try again')
           
   elif user in user_profiles:
      while True:
        try:
           delete = input("Enter a user you'd like to remove: ").title().strip()
           if delete not in user_profiles:
              print('Username not found, try again')
           else:
            del user_profiles[delete]
           break
        except ValueError:
           print('Invalid input, try again')

           
   
   


def update_account(user, user_profiles):
   print('1. Change password')
   print('2. Change username')
   while True:
        try:
            select = int(input('Enter an option: ').strip())
            if select != 1 and select != 2:
               print('Invalid option, try again')
            else:
               break
            if select == 1:
               pw = input('Enter a new password: ').strip()
               if user in user_profiles['Admin']:
                user_profiles['Admin'][user] = pw
               else:
                  user_profiles[user] = pw
            elif select == 2:
               new_name = input('Enter a new username: ').strip()
               if user in user_profiles['Admin']:
                  user_profiles['Admin'][new_name] = user_profiles['Admin'].pop(user)
               else:
                  user_profiles[new_name] = user_profiles.pop(user)
        except ValueError:
           print('Invalid input, try again')

               
   
   


def show_ratings(user, user_ratings):
    print('Current rated shows/movies:')
    for entertain, rating in user_ratings[user].items():
       print(f'{entertain}: {rating}')