def fibo(x):
    lst = [0, 1]
    for i in range(2, x):
        num = lst[i-2] + lst[i-1]
        lst.append(num)
    for j in lst:
        print(j, end=' ')

x = int(input('Enter an int: '))
fibo(x)
