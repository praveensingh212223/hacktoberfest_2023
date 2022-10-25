num=int(input("Enter a number:"))
temp=num
count=0
while(num>0):
    n = num % 10
    count = count * 10 + n
    num=num//10
if(temp==count):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
