# 1
def f1(n):
    if n == 0:
        return 1
    return n * f1(n - 1)

# 2
def f2(a, b):
    s = 0
    for i in range(a, b + 1):
        if not i % 2:
            s += i
    return s

# 3
def f3(lst):
    s = sorted(lst)
    return (s[0] + s[-1]) / 2

# 4
def f4(t):
    r = ""
    for i in t:
        r = i + r
    return t == r

# 5
def f5(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
