pw = input('Enter password: ')
count = 0

for i in range(len(pw)):
    if pw[i].isupper():
        count += 1

if count > 0 and len(pw) >= 8 and pw.isalnum() == True:
    print('Valid password')
else:
    print('Invalid password')

