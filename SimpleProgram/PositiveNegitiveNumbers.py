# Positive numbers and Negitive numbers
def classify_numbers(numbers):
    positive_numbers = []
    negitive_numbers = []
    for num in numbers:
        if num > 0:
            positive_numbers.append(num)
        elif num < 0:
            negitive_numbers.append(num)
        else:
            continue
    return positive_numbers, negitive_numbers
print(classify_numbers([-1, 0, 1, 2, -2, 3, -3]))

# Second way with list comprehension
positive_numbers = [num for num in [-1, 0, 1, 2, -2, 3, -3] if num > 0]
negitive_numbers = [num for num in [-1, 0, 1, 2, -2, 3, -3] if num < 0]
print(f"Positive numbers: {positive_numbers}, Negitive numbers: {negitive_numbers}")

# Fabonacci numbers
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
print(list(fibonacci(10)))

# Factorial numbers
def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)
factorials = [factorial(i) for i in range(1, 6)]
print(f"Factorials: {factorials}")
