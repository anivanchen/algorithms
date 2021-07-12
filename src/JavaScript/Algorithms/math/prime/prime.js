function prime(n) {
    const sequence = []

    for (let i = 2; i <= n; i++) {
        var isPrime = true;

        for (let j = 2; j < i; j++) {
            if (i % j == 0) {
                isPrime = false;
                break;
            }
        }

        if (i > 1 && isPrime == true) {
            sequence.push(i);
        }
    }
    return sequence
}