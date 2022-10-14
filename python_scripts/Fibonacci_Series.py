# Python program to display the Fibonacci sequence

def recursion_fibo(n):
   if n <= 1:
       return n
   else:
       return(recursion_fibo(n-1) + recursion_fibo(n-2))

no_of_terms = int (input("Enter the no of terms you want in fibonacci seq:"))

# check if the number of terms is valid
if no_of_terms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(no_of_terms):
       print(recursion_fibo(i))
