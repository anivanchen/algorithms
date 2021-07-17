function gcf(n, i) {
    if (!i) {return n;}
    return gcf(i, n % i);
}