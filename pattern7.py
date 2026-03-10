n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==(n+1)/2 and j==(n+1)/2:
            print(1,end=" ")
        else:
            print(0, end=" ")
    print()