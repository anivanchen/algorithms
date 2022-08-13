def prime(n):
    sequence = []

    for i in range(2, n):
        isPrime = True
        
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
                break

        if i > 1 & isPrime == True:
            sequence.append(i)

    return sequence