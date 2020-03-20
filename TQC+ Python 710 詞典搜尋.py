id = {}
key = input('Key: ')

while key != 'end':
    data = input('Value: ')
    id[key] = data

    key = input('Key: ')

search = input('Search key: ')
if search in id:
    print('True')
else:
    print('False')

