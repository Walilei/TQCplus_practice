a = eval(input('a = '))
b = eval(input('b = '))
count = 0
sum = 0
if a > b:
    a, b = b, a

for i in range(a, b+1):
    if i % 4 == 0 or i % 9 == 0:
        print(f'{i:<4}', end='')
        count += 1
        sum += i
        if count % 10 == 0:
            print()

print()
print(count)
print(sum)


