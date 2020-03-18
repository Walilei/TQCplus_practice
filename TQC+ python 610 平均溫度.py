# TQC+ 程式語言Python 610 平均溫度
'''
請撰寫一程式，讓使用者輸入四週各三天的溫度，接著計算並輸出這四週的平均溫度及最高、最低溫度。
提示1：平均溫度輸出到小數點後第二位。
提示2：最高溫度及最低溫度的輸出，如為31時，則輸出31，如為31.1時，則輸出31.1。
'''

lst = []

for i in range(4):
    print(f'Week {i+1}:')
    for j in range(3):
        print(f'Day {j+1}:', end='')
        user = eval(input())
        print(user)
        lst.append(user)

print(f'Average: {sum(lst)/len(lst):.2f}')
print(f'Highest: {max(lst)}')
print(f'Lowest: {min(lst)}')

