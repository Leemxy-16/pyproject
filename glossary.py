words = {
    'hello': 'a greeting in english',
    'code': 'a series of program written',
    'coder': ' a person who write program',
    'use': 'to use something'
}
for word in words:
    if word in words:
        meaning = words[word]
        print(f'{word.title()} Meaning : {meaning}')