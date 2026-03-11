n=4
new=0
for i in range (1,n+1):
    for j in range(0,n):
        new=new+1
        print(new,end=" ")
        if new==9:
            new=0
    print()


