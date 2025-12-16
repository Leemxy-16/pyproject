current_user = ['fay', 'Kay', 'Kelvin', 'Fati']
new_user = ['kay', 'fay', 'clara', 'felix', 'fati','kelvin']


for user in new_user:
    user = user.title()
    if user in current_user:
        print(f'{user.title()} is taken')
    else:
        print(f'{user.title()} is not taken')
