# TQC+ 程式語言Python 609 矩陣相加
'''
請撰寫一程式，讓使用者建立兩個2*2的矩陣，其內容為從鍵盤輸入的整數，接著輸出這兩個矩陣的內容以及它們相加的結果。
'''

print('Enter matrix 1:')
a11 = int(input('[1, 1]:'))
a12 = int(input('[1, 2]:'))
a21 = int(input('[2, 1]:'))
a22 = int(input('[2, 2]:'))
print('Enter matrix 2:')
b11 = int(input('[1, 1]:'))
b12 = int(input('[1, 2]:'))
b21 = int(input('[2, 1]:'))
b22 = int(input('[2, 2]:'))

print('Matrix 1:')
print(f'**{a11} {a12}**\n**{a21} {a22}**')
print('Matrix 2:')
print(f'**{b11} {b12}**\n**{b21} {b22}**')
print('Sum of 2 matrices:')
print(f'**{a11+b11} {a12+b12}**\n**{a21+b21} {a22+b22}**')
