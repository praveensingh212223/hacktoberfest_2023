num=int(input("Enter a number:"))
t=num
c=0
while(num>0):
    hb=num%10
    c=c*10+hb
    num=num//10
if(t==c):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
