def factor(num):
    factors = [i for i in range(1, num + 1) if num % i == 0]
    return factors

def gcd(a, b):
    while b:
        a, b = b, a % b
        return a
num1 = int(input("Enter the first value:"))
num2 = int(input("Enter the second "))

factor_num1 = factor(num1)
factor_num2 = factor(num2)

gcd_val = gcd(num1, num2)

print(f"Factors of {num1}: {factor_num1}")
print(f"Factors of {num2}: {factor_num2}")

print(f"GCD of {num1} and {num2} is: {gcd_val}")

