# First way using for loop
even_numbers = []
odd_numbers = []
for i in range(1, 11):
    if i%2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print(f"Even numbers: {even_numbers}, Odd numbers: {odd_numbers}")

# Second way with list comprehension
even_num = [x for x in range(1, 11) if x%2 == 0]
odd_num = [x for x in range(1,11) if x%2 != 0]
print(f"Even numbers: {even_num}, Odd numbers: {odd_num}")

# Third way using lambda function
numbers = list(range(1, 11))
even_n = list(filter(lambda x: x%2 ==0, numbers))
odd_n = list(filter(lambda x: x%2 != 0, numbers))
print(f"Even numbers: {even_n}, Odd numbers: {odd_n}")

# Fourth way using while loop
even_nu = []
odd_nu = []
i = 1
while i <= 10:
    if i%2 == 0:
        even_nu.append(i)
    else:
        odd_nu.append(i)
    i += 1
print(f"Even numbers: {even_nu}, Odd numbers: {odd_nu}")

# Fifth way using map function
numbers = list(range(1, 11))
even_nu = list(map(lambda x: x if x%2 == 0 else None, numbers))
odd_nu = list(map(lambda x: x if x%2 != 0 else None, numbers))
even_nu = [x for x in even_nu if x is not None]
odd_nu = [x for x in odd_nu if x is not None]
print(f"Even numbers: {even_nu}, Odd numbers: {odd_nu}")

# using functions and generators
def my_function():
    for i in range(1, 11):
        yield i

def even_function(even_num):
    for i in even_num:
        if i%2 == 0:
            yield i

def odd_function(odd_num):
    for j in odd_num:
        if j%2 != 0:
            yield j

e_numbers = list(even_function(my_function()))
print(f"Even numbers: {e_numbers}")
o_numbers = list(odd_function(my_function()))
print(f"Odd numbers: {o_numbers}")
