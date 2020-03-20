dict1 = {}
dict2 = {}

print('Create dict1: ')
key = input('Key: ')
while key != 'end':
    value = input('Value: ')
    dict1[key] = value

    key = input('Key: ')

print('Create dict2: ')
key = input('Key: ')
while key != 'end':
    value = input('Value: ')
    dict2[key] = value

    key = input('Key: ')

dict3 = dict(dict1, **dict2)
for key in sorted(dict3.keys()):
    print(f"{key}: {dict3[key]}")

