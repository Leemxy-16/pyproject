user_avail = ['admin', 'kay', 'fay']
user_new= ['friday','trio','admin','kay','fay']
for user_name in user_new:
    if user_name in user_avail:
        if user_name == 'admin':
            print(f'hello {user_name.title()}, would you like to see a status report?')
        else:
             print(f'hello {user_name.title()}, thank you for logging in again.')
            
    else:
        print(f'{user_name.title()},need to logging')