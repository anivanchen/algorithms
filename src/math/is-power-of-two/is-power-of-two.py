def isPowerOfTwo(n):
    import math
    return (math.ceil(math.log10(n) / math.log10(2)) == math.floor(math.log10(n) / math.log10(2)))