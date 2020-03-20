def compute(a, x, y):
    for i in range(y):
        for j in range(x):
            print(f'{a}', end='')
        print()


a = input('a = ')
x = eval(input('x = '))
y = eval((input('y = ')))
compute(a, x, y)
