height = 0
weight = 0

while True:
    height = eval(input('Height: '))
    if height == -9999:break
    weight = eval(input('Weight: '))
    if weight == -9999: break

    BMI = round(weight/((height/100)**2), 2)
    state = ''

    if BMI < 18.5:
        state = 'under weight'
    elif 18.5 <= BMI < 25:
        state = 'normal'
    elif 25.0 <= BMI < 30:
        state = 'over weight'
    elif 30 <= BMI:
        state = 'fat'

    print(f'BMI: {BMI}')
    print(f'State: {state}')
