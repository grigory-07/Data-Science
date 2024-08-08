def factor(num):
    if num == 0:
        return []
    factors = [i for i in range(1, num + 1) if num % i == 0]
    return factors
num1 = int(input("Enter the First value: "))
num2 = int(input("Enter the Second value: "))
a = num1
b = num2
while num2 != 0:
    temp = num2
    num2 = num1 % num2
    num1 = temp
gcd = num1
factors_a = factor(a)
factors_b = factor(b)
factors_gcd = factor(gcd)

print(f"Factors of {a}: {factors_a}")
print(f"Factors of {b}: {factors_b}")
print(f"GCD of {a} and {b} = {gcd}")
