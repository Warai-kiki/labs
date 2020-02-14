while True:
    days = range(1, 32)
    mounths = range(1, 13)
    years = range(1901, 2020)
    while True:
        try:
            d, m, y = int(input('day:')), \
                      int(input('mounth:')), \
                      int(input('year:'))
            break
        except ValueError or NameError:
            print ('it must be digits')
    if y%4 != 0 :
        if 1<=m<=13 :
            if m!=12 and n!=31:
                if m==2:
                    if 1<=n<28 :
                        print (f'Day after {n+1}/{m}')
                    elif n==28 :
                        print(f'Day after 01/{m+1}')
                    else:
                        print ('Error2')
                elif m==4 or m==6 or m==9 or m==11 :
                    if 1<=n<30 :
                        print(f'Day after {n + 1}/{m}')
                    elif n==30 :
                        print(f'Day after 01/{m+1}')
                    else:
                        print ('Error3')
                else:
                    if 1<=n<31 :
                        print(f'Day after {n + 1}/{m}')
                    elif n==31 :
                        print(f'Day after 01/{m+1}')
                    else:
                        print ('Error4')
            else:
                print ('Day after 1/1')

            if m != 1 and n != 1 :
                if m == 2:
                    if 1 < n <= 28:
                        print(f'Day before {n - 1}/{m}')
                    elif n == 1:
                        print(f'Day before 31/{m - 1}')
                    else:
                        print('Error2')
                elif m == 4 or m == 6 or m == 9 or m == 11:
                    if 1 < n <= 30:
                        print(f'Day before {n - 1}/{m}')
                    elif n == 1:
                        print(f'Day before 31/{m - 1}')
                    else:
                        print('Error3')
                else:
                    if 1 < n <= 31:
                        print(f'Day before {n - 1}/{m}')
                    elif n == 1:
                        print(f'Day before 30/{m - 1}')
                    else:
                        print('Error4')
            else:
                print('Day before 31/12')

        else:
            print ('Error1')
    else:
        if

    print ('Would you try again? Write yes or no')
    l= input('')
    if l=='yes' :
        continue
    else:
        break