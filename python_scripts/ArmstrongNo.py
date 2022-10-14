# Python program to check whether
# the number is Armstrong number or not

def power(x, y):
	
	if y == 0:
		return 1
	if y % 2 == 0:
		return power(x, y // 2) * power(x, y // 2)
		
	return x * power(x, y // 2) * power(x, y // 2)

def order(x):

	n = 0
	while (x != 0):
		n = n + 1
		x = x // 10
		
	return n

# Function to check whether the given
# number is Armstrong number or not
def isArmstrong(x):
	
	n = order(x)
	temp = x
	sum = 0
	
	while (temp != 0):
		r = temp % 10
		sum = sum + power(r, n)
		temp = temp // 10

	return (sum == x)

# Driver code
x = int(input("Enter the no to be checked:"))
print(isArmstrong(x))
