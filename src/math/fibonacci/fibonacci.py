def fibonacci(n):
    sequence = [1]

    currentValue = 1
    previousValue = 0

    if (n == 1):
        return sequence
    
    iterationCounter = n - 1

    while (iterationCounter):
        currentValue += previousValue
        previousValue = currentValue - previousValue

        sequence.append(currentValue)

        iterationCounter -= 1

    return sequence