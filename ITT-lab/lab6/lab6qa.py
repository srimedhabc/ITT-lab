p=1
while(p==1):
    def isPalindrome(s):
        return s==s[::-1]
    s = input("Enter the string: ")
    ans = isPalindrome(s)
    if ans:
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