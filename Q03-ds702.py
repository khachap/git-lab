def GCD(a, b):   
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd
a = int(input("Enter a :"))
b = int(input("Enter b :"))
result = GCD(a, b)
print("GCD of", a, "and", b, "is:", result)