def Fibonacci(n):
   if n <= 1:
       return n
   else:
       return(Fibonacci(n-1) + Fibonacci(n-2))


terms=int (input('Enter the number of terms'))

if terms<=0:
    print("Enter a valid no of terms :")
else :
    print("Fibonacci sequence is :")
    for i in range(terms):
        print(Fibonacci(i))