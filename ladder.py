n=int(input('enter the leder sige'))
for i in range (n):
    for row in range (6):
        for col in range (4):
            if row in {0,2} and col in{0,3} or row in {4} and col in{0,1,2,3}:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()           