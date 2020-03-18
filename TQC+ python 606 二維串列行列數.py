# TQC+ 程式語言Python 606 二維串列行列數
'''
請撰寫一程式，讓使用者輸入兩個正整數rows、cols，分別表示二維串列lst 的「第一個維度大小」與「第二個維度大小」。
串列元素[row][col]所儲存的數字，其規則為：row、col 的交點值 = 第二個維度的索引col – 第一個維度的索引row。
接著以該串列作為參數呼叫函式compute()輸出串列。
提示：欄寬為4。
'''

rows = int(input('Enter rows: '))
cols = int(input('Enter cols: '))

for i in range(rows):
    for j in range(cols):
        print(f'{j-i:4}', end=' ')
    print()

