year = 0

while True:
    year = int(input())
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            print(f"{year} is not a leap year.")
        else:
            print(f"{year} is a leap year.")
    elif year == -9999:
        break
    else:
        print(f"{year} is not a leap year.")

