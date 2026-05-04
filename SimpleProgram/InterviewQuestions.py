# This code defines a function `sum` that takes a variable number of arguments and returns their sum.
def sum(*args):
    if args:
        start = type(args[0])()
        for i in args:
            start += i
        return start
    return 0

print(sum(10, 20))
print(sum([1,2,3,4], [5,6,7,8],[9,1,2,3]))
print(sum("Hello", "World!"))
print(sum(12.1, 13.1))

# It also defines a function `count_occurrences` that counts the number of occurrences of a substring in a given string.
str1 = "fereesmadhavierefeffMadhaViMwrtigMadhaviMwertyui"
def count_occurrences(string, substring):
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count
print(count_occurrences(str1.lower(), "Madhavi".lower()))

# common prefix for a list of strings
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

print(longest_common_prefix(["flower","flow","flightr"]))
print(longest_common_prefix(["dog","racecar","car"]))

# Is prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
            break
    return True

prime_numbers = [x for x in range(1, 51) if is_prime(x)]
print(prime_numbers)
print("Twin prime number: ", [(p, p+2) for p in prime_numbers if p+2 in prime_numbers])
#print("Prime numbers pair: ", [(prime_numbers[i], prime_numbers[i+1]) for i in range(len(prime_numbers)-1)])

# pairs
nums = [1, 2, 3, 4, 5, 6]
def pairs_numbers(nums):
    pairs = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == 7:
                pairs.append((nums[i], nums[j]))
    return pairs
print(pairs_numbers(nums))
print("Pairs using list comprehension: ", [(nums[i], nums[j]) for i in range(len(nums)) for j in range(i+1, len(nums)) if nums[i] + nums[j] == 7])
shuffle_numbers = nums[2:] + nums[:2]
print("Shuffle numbers two steps: ", shuffle_numbers)

# Large number, second largest number, and third largest number, and smallest number
numbers = [10, 20, 10, 30, 20, 40]
def find_largest_numbers(nums):
    largest = second_largest = third_largest = smallest = nums[0]

    for num in nums:
        if num > largest:
            third_largest = second_largest
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            third_largest = second_largest
            second_largest = num
        elif second_largest > num > third_largest:
            third_largest = num
        
        if num < smallest:
            smallest = num
            
    return largest, second_largest, third_largest, smallest
largest, second_largest, third_largest, smallest = find_largest_numbers(numbers)
print(f"Largest: {largest}, Second Largest: {second_largest}, Third Largest: {third_largest}, Smallest: {smallest}")

# Give string and count the number of occurrences of each character in the string
def count_characters(s):
    char_count = {}
    for char in s:
        if char.isspace():
            continue
        elif char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
input_string = "hello world"
character_counts = count_characters(input_string.lower())
print("Character counts:", character_counts)

# Count the number of occurrences of each word in a given string
def count_words(s):
    word_count = {}
    words = s.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
input_string = "hello world hello"
word_counts = count_words(input_string.lower())
print("Word counts:", word_counts)

# Number of occurrences of a number in a given number
def count_occurrences_in_number(num):
    digit_count = {}
    if num < 0:
        num = -num
    while num > 0:
        digit = num%10
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1
        num //= 10
    return digit_count

print(count_occurrences_in_number(123321))

def unique_difference(my_list):
    result = []
    for i in range(len(my_list)):
        count = 0
        for j in range(len(my_list)):
            if my_list[i] == my_list[j]:
                count += 1
    if count == 1:
        result.append(my_list[i])

print(unique_difference([1, 2, 3, 4, 5, 2, 3, 4]))

