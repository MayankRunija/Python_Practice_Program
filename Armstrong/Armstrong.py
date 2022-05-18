def is_Armstrong(A):  
        
    N = order_1(A)  
    temp_1 = A  
    sum_1 = 0  
        
    while (temp_1 != 0):  
        R_1 = temp_1 % 10  
        sum_1 = sum_1 + power_1(R_1, N)  
        temp_1 = temp_1 // 10  
    
    # If the above condition is satisfied, it will return the result  
    return (sum_1 == A)  
    
# Driver code  
A = int(input("Please enter the number to be checked: "))  
print(is_Armstrong(A))
