x = eval(input('Int: '))

for i in range(x):
    print(' '*(x - 1 - i) + '*' * (2 * (i+1) - 1))

