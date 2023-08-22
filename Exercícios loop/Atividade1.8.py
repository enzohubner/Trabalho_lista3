import sympy

total = 0
for i in range(1, 51):
    if sympy.isprime(i):
        total = total + 1
print(total)       