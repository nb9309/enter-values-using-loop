n = int(input('enter number of values u want: '))

if n<=0:
    print('{} is invalid'.format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val = input('enter {} value = '.format(i))
        lst.append(val)
    else:
        print(lst)
