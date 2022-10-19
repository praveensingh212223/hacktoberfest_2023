# co-prime numbers:
# Co prime numbers are those numbers that have only one common factor, namely 1. 
#That means a pair of numbers are said to be co prime when they have their highest common factor as 1. 
#Eg 15 and 8



#this program checks if given two numbers are co-prime or not

def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p
def is_coprime(x, y):
    return gcd(x, y) == 1

a=int(input("Enter the first number\n"))
b=int(input("Enter the second number\n"))
if(is_coprime(a,b)==1):
    print("The numbers are coprime")
else:
    print("The numbers are not coprime")