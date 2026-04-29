# Generators are a special type of iterable that allow you to iterate over a sequence of values 
# without storing the entire sequence in memory at once. They are defined using functions and 
# the `yield` statement.
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
print(list(count_up_to(5)))  # Output: [1, 2, 3, 4, 5]

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(10))) # Output: [0, 1, 1, 2, 3, 5, 8, 21, 34]

def square_generator(n):
    for i in range(n):
        yield i ** 2

print(list(square_generator(5)))  # Output: [0, 1, 4, 9, 16]

# Real Time Data Stream Simulation
import time
def real_time_data_stream():
    for i in range(5):
        yield f"Data point {i}"
        time.sleep(1)  # Simulate delay in data generation
for data in real_time_data_stream():
    print(data)  # Output: Data point 0, Data point 1, ..., Data point 4 (with a delay of 1 second between each)