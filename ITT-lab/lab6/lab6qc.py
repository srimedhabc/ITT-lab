p=1
while(p==1):
    size = int(input("Enter the number of elements in the list: "))
    l = []
    print("Enter the list:")
    for _ in range(size):
        l.append(input())
    s = sorted(l)
    print("The sorted list is:")
    print(s)
    flag=0
    while(flag == 0):
        p = int(input("Enter 1 to continue and 0 to exit : "))
        if(p!=1 and p!=0):
            print("Invalid entry")
        if(p==1 or p==0):
            flag=1