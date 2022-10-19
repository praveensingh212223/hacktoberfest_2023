def Length(n):    
    length = 0;    
    while(n != 0):                    # calculating the length of the number
        length = length + 1;    
        n = n//10;    
    return length;    
     
#sumDigit()  
def sumdigit(num):    
    rem = sum = 0;    
    len = Length(num);     # checking the number is disarium or not
        
    while(num > 0):    
        rem = num;   
        sum = sum + (rem**len);    
        num = num//10;    
        len = len - 1;    
    return sum;    
      
result = 0;    
     

print("Disarium numbers between 1 and 100 are");    
for i in range(1, 101):           # printing disarium numbers
    result = sumdigit(i);    
        
    if(result == i):    
        print(i),   