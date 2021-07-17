function lcm(n, i) {
    if (n > i) { greater = n } else { greater = i }
    while (true) {
        if (greater % n === 0 && greater % i === 0) { return greater }
        greater++
    }
}