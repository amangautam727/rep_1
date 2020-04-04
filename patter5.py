num=int(input("enter the size "))
for h in range(num,0,-1):
        print((" "*(num-h))+('*'+' ')*(h))
for h in range(num):
        print((" "*(num-h-1))+('*'+' ')*(h+1))
