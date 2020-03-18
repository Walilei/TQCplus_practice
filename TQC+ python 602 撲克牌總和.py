# TQC+ 程式語言Python 602 撲克牌總和
'''
請撰寫一程式，讓使用者輸入52張牌中的5張，計算並輸出其總和。
提示：J、Q、K以及A分別代表11、12、13以及1。
'''

poker = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
total = 0

for i in range(5):
    card = input('Enter a card rank: ')
    if card in poker:
        total += poker.get(card)
    else:
        total += int(card)

print(total)
