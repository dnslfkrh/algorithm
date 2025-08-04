def solution(a, b, c):
    if a != b != c != a:
        return a + b + c
    elif a == b == c:
        return (a + b + c) * (pow(a, 2) + pow(b, 2) + pow(c, 2)) * (pow(a, 3) + pow(b, 3) + pow(c, 3))
    else:
        return (a + b + c) * (pow(a, 2) + pow(b, 2) + pow(c, 2)) 