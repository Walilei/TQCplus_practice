# TQC+ 程式語言Python 608 最大最小值索引
'''
請撰寫一程式，讓使用者建立一個3*3的矩陣，其內容為從鍵盤輸入的整數（不重複），接著輸出矩陣最大值與最小值的索引。
'''

lst = [int(input('Enter an int: ')) for i in range(9)]

max_index = lst.index(max(lst))
print(f'Index of the largest number {max(lst)} is: ({max_index//3}, {max_index%3})')

min_index = lst.index(min(lst))
print(f'Index of the smallest number {min(lst)} is: ({min_index//3}, {min_index%3})')

