#define function for greatest common divisor
def gcd(a,b):

    if a==0:
        return b
    return gcd(b%a,a)

def coprime(a,b):
    if gcd(a,b)==1:
        return True
    else:
        return False

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

if coprime(a,b):

    print("Given numbers are co-prime numbers")
else:
    print("Given numbers are not co-prime numbers")

##Test Output:
##Enter first number: 4
##Enter second number: 6
##Given numbers are not co-prime numbers
