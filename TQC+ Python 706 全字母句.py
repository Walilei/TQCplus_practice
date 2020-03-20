n = int(input('Enter nums: '))
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in range(n):
    data = input('Data = ').lower()
    bool = True
    for j in alphabet:
        if j not in data:
            bool = False
    print(bool)
