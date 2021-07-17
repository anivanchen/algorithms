function isPowerOfTwo(n) {
    return (Math.log(n)/Math.log(2)) % 1 === 0;
}