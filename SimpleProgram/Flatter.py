input_items = [1,2, (3, 4, {'a': 5, 'b': 6})]

def flatten(items):
    result = []
    for item in items:
        if isinstance(item, (list, tuple, set)):
            result.extend(flatten(item))
        elif isinstance(item, dict):
            result.extend(flatten(item.values()))
        else:
            result.append(item)
    return result
print(flatten(input_items))

def flatten_generator(items):
    for item in items:
        if isinstance(item, (list, tuple, set)):
            yield from flatten_generator(item)
        elif isinstance(item, dict):
            yield from flatten_generator(item.values())
        else:
            yield item
print(list(flatten_generator(input_items)))

def flatten_recursion(items):
    result = []
    for item in items:
        if isinstance(item, (list, tuple, set)):
            result += flatten_recursion(item)
        elif isinstance(item, dict):
            result += flatten_recursion(item.values())
        else:
            result.append(item)
    return result
print(flatten_recursion(input_items))

def factorial(n):
   return 1 if n <= 1 else n * factorial(n-1)

factorials = [factorial(i) for i in range(1, 6)]
print(factorials)