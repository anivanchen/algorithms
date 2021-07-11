def factorial(n):
    if n < 0: 
        return 0
    elif n == 0 or n == 1: 
        return 1

    factorial = 1
    
    while (n > 1):
        factorial *= n
        n -= 1

    return factorial