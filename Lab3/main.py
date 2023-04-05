import math


def fermat(n, B):
    k = 0
    t = 0
    s = 0
    ok = 1
    while ok:
        # iterate for values of k = 1, 2, 3, ...
        k = k + 1
        t0 = int(math.sqrt(n * k))
        # we find the integer value of the square root
        for t in range(t0 + 1, t0 + B + 1):
            x = t * t - k * n
            s = int(math.sqrt(x))
            if (s * s) == x:
                # once we find a suitable s we end the loops
                ok = 0
                break

    # n = 1/k * (t-s) * (t+s)
    # we check which factor can be divided by the final k value
    if (t - s) / k == (t - s) // k:
        return (t - s) // k, t + s
    else:
        return t - s, (t + s) // k


if __name__ == "__main__":

    print("Generalized Fermat's Algorithm")
    n = int(input("Enter an odd composite number: "))
    B = int(input("Enter an the bound value: "))

    f1, f2 = fermat(n, B)

    if f1 == 1 or f2 == 1:
        print("The chosen number is prime")
    else:
        print("The two factors are: " + str(f1) + " and " + str(f2))
