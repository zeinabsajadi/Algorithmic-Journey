def factorial_range(a, b):
    if a > b:
        return 1
    if a == b:
        return a
    if b == a + 1:
        return a * b
    mid = (a + b) // 2
    return factorial_range(a, mid) * factorial_range(mid + 1, b)

def factorial(n):
    return factorial_range(1, n)
