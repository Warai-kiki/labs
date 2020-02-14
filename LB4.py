while True:
    while True:
        try:
            t = int(input('input minutes '))
            break
        except ValueError or NameError:
            print ('it must be digits')

    if 0 < t <= 60:
        if t % 6 == 1 or t % 6 == 2 or t % 6 == 3:
            print('green')
        elif t % 6 == 4:
            print('yellow')
        else:
            print('red')
    else:
        print('Wrong minute')
    print('Would you try again? Write yes or no')
    l = input('')
    if l == 'yes':
        continue
    else:
        break