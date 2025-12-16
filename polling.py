fav_lang = {
    'shamsu':'django',
    'kaseem':'python',
    'sadiya': 'qbasic',
    'khadija':'java'
}
pollers = ['khadija' ,'yasir','shamsu','yusra','kaseem']

for polls in pollers:
    
    #for lang in fav_lang:
    if polls in fav_lang:
        print(f'{polls.title()} has taken a  polls of {fav_lang[polls].title()} language')
    else:
        print(f'{polls.title()} please take a poll')