function fibonacci(n) {
    const sequence = [1];

    let currentValue = 1;
    let previousValue = 0;
    
    if (n === 1) {
        return sequence;
    }

    let iterationCounter = n - 1;

    while (iterationCounter) {
        currentValue += previousValue;
        previousValue = currentValue - previousValue;

        sequence.push(currentValue);

        iterationCounter -= 1;
    }
    
    return sequence;
}