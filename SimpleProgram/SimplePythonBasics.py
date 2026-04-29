x = 123
#for i in x: Error: 'int' object is not iterable

# length of a string passing len function as an argument to another function
def length(a, b):
    return a(b)
print(length(len, "python"))  # Output: 6

list = (1, 2, 3, 4, 5)
# list.append((6, 7, 8, 9, 10))  # Error: 'tuple' object has no attribute 'append'
print(len(list))  # Output: 5

str = "python"
print(str.find("ph"))  # Output: 0

lst = ['python', 'java', 'c++']
lst.reverse()
print(lst)  # Output: ['c++', 'java', 'python']

n = {1,1,20,30,20}
print(n)  # Output: {1, 20, 30} (duplicates are removed in a set)

a = {1,2,3,4}
b = {3,4}
print(a.difference(b))  # Output: {1, 2} (elements in a but not in b)
print(a.intersection(b))  # Output: {3, 4} (elements common to both a and b)
print(a.union(b))  # Output: {1, 2, 3, 4} (all unique elements from both a and b)
print(a.symmetric_difference(b))  # Output: {1, 2} (elements in either a or b but not in both)
print(a.issubset(b))  # Output: False (a is not a subset of b)
print(a.issuperset(b))  # Output: True (a is a superset of b)
print(a.isdisjoint(b))  # Output: False (a and b have common elements)
print(a.add(5))  # Output: None (adds 5 to the set a)
print(a.remove(5))  # Output: None (removes 5 from the set a)
# print(len(a+b)) # Output: Error: unsupported operand type(s) for +: 'set' and 'set' (sets cannot be concatenated using the + operator)

print(22%3)  # Output: 1 (the remainder of 22 divided by 3)
print(22//3)  # Output: 7 (the quotient of 22 divided by 3, rounded down to the nearest whole number)

c = "xyyzxyzxzxyy".count("yy",2)
print(c)  # Output: 1 (the substring "yy" appears once in "xyyzxyzxzxyy" starting at index 2)

for i in range(0, 1_1):
    print(i, end=" ") # Output: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 (numbers from 0 to 10)

print(type(type(int)))  # Output: <class 'type'> (the type of the type of int is 'type')

tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple[tuple.index(5)]) # Output: 5 (the element at the index of 5)

L = [1, 3, 5, 7, 9]
print(L.pop(3)) # Output: 7 (removes and returns the element at index 3)
print(L) # Output: [1, 3, 5, 9] (the list after removing the element at index 3)

tup = (5, ' python ', 3.14)
a , b , c = tup
print(b)  # Output: ' python ' (the second element of the tuple)

t1 = (1,2,3)
t2 = (4,5,6)
print(t1 + t2)  # Output: (1, 2, 3, 4, 5, 6) (concatenation of two tuples)

st = "python___developers"
new_st = ' '
for s in st:
    if s == '_':
        continue
    new_st += s
print(new_st)  # Output: "pythondevelopers" (removes all underscores from the string)

s = 0
for i in range(10, 1, -1):
    s -= i
print(s)  # Output: -54 (subtracts numbers from 10 down to 2 from s)

for c in range(ord('a'), ord('z') + 1):
    print(c, end=' ')  # Output: 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 (ASCII values of lowercase letters a to z)
    print(chr(c), end=' ')  # Output: a b c d e f g h i j k l m n o p q r s t u v w x y z (characters corresponding to ASCII values 97 to 122)

li1 = [5, 2.3, '6']
# li1.sort() # Error: '<' not supported between instances of 'str' and 'float' (cannot compare a string with a float for sorting)

li2 = [5, 2.3, 6]
print(sorted(li2))  # Output: [2.3, 5, 6] (returns a new sorted list without modifying the original list)

exp = 2 ** 2 ** 3 ** 1
print(exp)  # Output: 256 (exponentiation is right-associative)
print(2*2*2*2*2*2*2*2)  # Output: 256 (2 multiplied by itself 8 times is 256)

# False = "True" # Output: Error: cannot assign to False (cannot assign a string to the boolean value False)
print(True == False) # Output: False (True is not equal to False)

str2 = "developers"
count = str2.count('e', -7)
print(count)  # Output: 2 (the substring 'e' appears twice in "developers" starting from index -7)
print(str2.find('e', -7))  # Output: 1 (the index of the first occurrence of 'e' in "developers" starting from index -7)

di1 = {1: 'one', 2: 'two', 3: 'three'}
print(di1.get(2, 1))  # Output: 'two' (returns the value for key 2, or 1 if the key is not found)
print(di1.get(4, 1))  # Output: 1 (returns the default value 1 since key 4 is not found in the dictionary)

dict1 = { }
dict1[2] = 1
dict1[1] = [2, 3, 4]
print(dict1[1][1])  # Output: 3 (the second element of the list associated with key 1)

dict2 = {'B': 5, 'A': 10, 'C': 1}
print(sorted(dict2))  # Output: ['A', 'B', 'C'] (returns a sorted list of the dictionary's keys)
print(sorted(dict2.values()))  # Output: [1, 5, 10] (returns a sorted list of the dictionary's values)
print(sorted(dict2.items()))  # Output: [('A', 10), ('B', 5), ('C', 1)] (returns a sorted list of the dictionary's key-value pairs)

set = {1, 2, "python", 2.4, 5}
print(set)  # Output: {1, 2, 'python', 2.4, 5} (a set containing unique elements of different types)
# print(set[2]) # Output: Error: 'set' object is not subscriptable (cannot access elements of a set by index)

#print(b<a) # Output: False (sets cannot be compared using < operator)

set1 = {1, 2, 3}
# set1.update(3) # Output: Error: 'int' object is not iterable (update method expects an iterable, but an integer was provided)

list1 = [1, 2, 3, 4, 5]
list1[2:3] = []
print(list1)  # Output: [1, 2, 4, 5] (removes the element at index 2 by assigning an empty list to that slice)

m = [[1, 2], [4, 5, 6]]
for i in range(0, 2):
    print(m[i][1])  # Output: 2, 5 (the second element of each sublist in the matrix m)

str_a = "python"
str_b = str_a.split("t")
print(str_b)  # Output: ['py', 'hon'] (splits the string 'python' at the character 't')

i = 1
while True:
    if i%7 == 0:
        break
    print(i, end=" ") # Output: 1, 2, 3, 4, 5, 6 (prints numbers from 1 to 6 until it reaches a number that is divisible by 7, at which point it breaks out of the loop)
    i += 1

list2 = [1, 2, 3, 4, 5]
print(list2.remove(3))  # Output: None (removes the first occurrence of 3 from the list, but does not return the removed element)
print(list2)  # Output: [1, 2, 4, 5] (the list after removing the element 3)

list3 = [True, "python"]
#for x in list3:
#    x.upper()  # Output: Error: 'bool' object has no attribute 'upper' (cannot call upper method on a boolean value)
print(list3)  # Output: [True, 'python'] (the original list remains unchanged since the upper method was not successfully called on the string element)

x = 0
y = 1
while x*y < 10:
    print(x, end=" ") # Output: 0, 4, 8 (prints multiples of 4 until the product with y is no longer less than 10)
    x += 4

xy = 'Python'
print(xy.startswith('p'))  # Output: False (the string 'Python' does not start with lowercase 'p')
print(xy.startswith('P'))  # Output: True (the string 'Python' starts with uppercase 'P')

def func(a, b=[]):
    for i in range(a):
        b.append(i*i)
    print(b)
func(3, [1,2,3])  # Output: [1, 2, 3, 0, 1, 4] (appends the squares of numbers from 0 to 2 to the provided list b)

# walrus operator
while (data := input("Enter Input : ")) != 'exit':
    print("I am great")

print(2*"2") # Output: '22' (the string '2' repeated twice)
# print(2+"2") # Output: Error: unsupported operand type(s) for +: 'int' and 'str' (cannot add an integer and a string together)
