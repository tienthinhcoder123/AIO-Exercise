def factorial(n):
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def approx_sin(x, n):
    sin_x = 0
    for i in range(n):
        sin_x += (-1) ** (i) * ((x) ** (2 * i + 1)) / factorial(2 * i + 1)
    return sin_x

def approx_cos(x, n):
    cos_x = 0
    for i in range(n):
        cos_x += (-1) ** (i) * (x ** (2 * i)) / factorial(2 * i)
    return cos_x

def approx_sinh(x, n):
    sinh_x = 0
    for i in range(n):
        sinh_x += x ** (2 * i + 1) / factorial(2 * i + 1)
    return sinh_x

def approx_cosh(x, n):
    cosh_x = 0
    for i in range(n):
        cosh_x += x ** (2 * i) / factorial(2 * i)
    return cosh_x

if __name__ == "__main__":
    print(approx_sin(x=3.14, n=10))
    print(approx_cos(x=3.14, n=10))
    print(approx_sinh(x=3.14, n=10))
    print(approx_cosh(x=3.14, n=10))