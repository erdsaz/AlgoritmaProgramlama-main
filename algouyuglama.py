def sumTen(a):
    if a<1:
        return 1
    return a + sumTen(a-1)
