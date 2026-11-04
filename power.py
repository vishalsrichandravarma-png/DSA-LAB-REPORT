def power(P, n):
    if n == 0:
        return 1
    return P * power(P, n - 1)

# Driver Code
P = int(input("Enter base (P): "))
n = int(input("Enter exponent (n): "))

print("Result =", power(P, n))