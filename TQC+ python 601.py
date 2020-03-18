# TQC+ 程式語言Python 601 偶數索引值加總
'''
請撰寫一程式，利用一維串列存放使用者輸入的12個正整數（範圍1~99）。顯示這些數字，接著將串列索引為偶數的數字相加並輸出結果。
提示：輸出每一個數字欄寬設定為3，每3個一列，靠右對齊。
'''

lst = [int(input('Enter int between 1 to 99: ')) for i in range(12)]
total = 0
count = 0

for i in lst:
    print(f'{i:3}', end='')
    count += 1
    if lst.index(i) % 2 == 0:
        total += i
    if count % 3 == 0:
        print()
print(total)
