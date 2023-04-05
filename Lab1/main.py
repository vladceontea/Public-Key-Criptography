import time

'''
The euclidean algorithm computes the remainder between the two numbers and uses it to continue until one reaches 0, the other one being the gcd.
'''
def euclidean_gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    while b > 0:
        r = a % b
        a = b
        b = r

    return a


'''
The extended euclidean algorithm works similarly to the basic one, but also computes the values of u and v such that a*u + b*v = d (the gcd value).
'''
def extended_euclidean_gcd(a, b):
    u2 = 1
    u1 = 0
    v2 = 0
    v1 = 1
    if a == 0 or b == 0:
        return max(a, b)
    while b > 0:
        q = a // b
        r = a - q*b
        u = u2 - q*u1
        v = v2 - q*v1
        a = b
        b = r
        u2 = u1
        u1 = u
        v2 = v1
        v1 = v

    d = a
    u = u2
    v = v2
    return d


'''
The subtraction algorithm computes the difference between the two numbers until they are equal to one another, which is the gcd.
'''
def subtraction_gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    while a != b:
        if a >= b:
            a = a - b
        else:
            b = b - a

    return a


if __name__ == '__main__':
    tests = [
        (0, 9),
        (20, 15),
        (37, 43),
        (50, 70),
        (455, 240),
        (1000, 2000),
        (1001, 3001),
        (123456789, 235468791),
        (2 ** 10, 4 ** 2),
        (10 ** 10, 5 ** 20)
    ]
    for test in tests:
        a = test[0]
        b = test[1]

        print("a = " + str(a))
        print("b = " + str(b))

        print("Euclidean GCD")
        start = time.perf_counter_ns()
        gcd = euclidean_gcd(a, b)
        end = time.perf_counter_ns()
        print("Time: " + str(end-start) + " nanoseconds")
        print("GCD = " + str(gcd))

        print("Extended Euclidean GCD")
        start = time.perf_counter_ns()
        gcd = extended_euclidean_gcd(a, b)
        end = time.perf_counter_ns()
        print("Time: " + str(end-start ) + " nanoseconds")
        print("GCD = " + str(gcd))

        print("Subtraction GCD")
        start = time.perf_counter_ns()
        gcd = subtraction_gcd(a, b)
        end = time.perf_counter_ns()
        print("Time: " + str(end-start) + " nanoseconds")
        print("GCD = " + str(gcd))

        print("---------------")

