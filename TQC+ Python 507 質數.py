def compute(x):
    count = 0
    for i in range(1, x):
        if x % i == 0:
            count += 1

    if count != 1:
        print('Not Prime')
    else:
        print('Prime')

x = int(input('Enter an int: '))
compute(x)
