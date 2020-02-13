from enum import Enum
class converter (Enum):
	USD =1
	EUR= 2
	CZK = 3
	PLN = 4
while True:
    while True:
        try:
            x= float (input ('amount of money '))
            p = converter [input ('currency: ')]
            break
        except ValueError or NameError :
            print('Try again')
    if p == converter.USD:
        s = 24 * x
        print(f'{s}')
    elif p == converter.EUR:
        s = 32 * x
        print(f'{s}')
    elif p == converter.CZK:
        s = 2.5 * x
        print(f'{s}')
    else:
        p == 8 * x
        print(f'{s}')
    print('Would you try again? Write yes or no')
    l = input('')
    if l == 'yes':
        continue
    else:
        break