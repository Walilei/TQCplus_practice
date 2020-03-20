first = 0
second = 0
null = 0

for i in range(5):
    vote = int(input("Enter your vote: "))
    if vote == 1:
        first += 1
    elif vote == 2:
        second += 1
    else:
        null += 1
    print(f"Total votes of No.1: Nami = {first}")
    print(f"Total votes of No. 2: Chopper = {second}")
    print(f"Total null votes = {null}")

winner = ''
if first > second:
    winner = 'No.1 Nami'
elif second > first:
    winner = 'No.2 Chopper'
else:
    winner = 'No one'

print(f"=> {winner} won the election.")
