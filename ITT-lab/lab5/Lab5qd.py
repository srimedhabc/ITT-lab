p=1
while(p==1):
    n = int(input("Enter the no. of elements in list: "))
    l = []
    print('Enter elements of the list: ')
    for i in range(n):
        l.append(int(input()))
# reversing the list using l[::-1]
# comparing reversed list with user entered list
    if l == l[::-1]:
        print("It is a palindrome")
    else:
        print("Not a palindrome")
    flag=0
    while(flag == 0):
        p = int(input("Enter 1 to continue and 0 to exit : "))
        if(p!=1 and p!=0):
            print("Invalid entry")
        if(p==1 or p==0):
            flag=1
