while True:
    m = {0,1,2,3,4,5,6,7,8,9}
    n = input()
    n1 = ''.join(n)
    n2 = set(map(int,n1))
    s_new = m.difference(n2)
    print(sorted(s_new))

    print('Would you try again? Write yes or no')
    l = input('')
    if l == 'yes':
        continue
    else:
        break