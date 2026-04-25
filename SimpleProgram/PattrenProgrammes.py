# Pattern Programs in Python
# ***Pattern 1: Right-Angled Triangle of Stars***
for i in range(1, 6):
    print('*' * i)
# Output: i = 1 -> *
#         i = 2 -> **
#         i = 3 -> ***
#         i = 4 -> ****
#         i = 5 -> *****

print()  # Print a blank line for separation

# ***Pattern 2: Inverted Right-Angled Triangle of Stars***
for i in range(5, 0, -1):
    print('*' * i)
# Output: i = 5 -> *****
#         i = 4 -> ****
#         i = 3 -> ***
#         i = 2 -> **
#         i = 1 -> *

print()  # Print a blank line for separation

# ***Pattern 3: Pyramid of Stars***
for i in range(1, 6):
    print(' ' * (5 - i) + '*' * (2*i - 1))
# Output: i = 1 -> ' '*(5-1) + '*'*(2*1 -1) -> ' '*4 + '*'*(2-1) -> '    ' + '*'      ->     *
#         i = 2 -> ' '*(5-2) + '*'*(2*2 -1) -> ' '*3 + '*'*(4-1) -> '   ' + '***'     ->    ***
#         i = 3 -> ' '*(5-3) + '*'*(2*3 -1) -> ' '*2 + '*'*(6-1) -> '  ' + '*****'    ->   *****
#         i = 4 -> ' '*(5-4) + '*'*(2*4 -1) -> ' '*1 + '*'*(8-1) -> ' ' + '*******'   ->  *******
#         i = 5 -> ' '*(5-5) + '*'*(2*5 -1) -> ' '*0 + '*'*(10-1) -> '' + '*********' -> *********

print()  # Print a blank line for separation

# ***Pattern 4: Right-Aligned Triangle of Stars***
for i in range(1, 6):
    print(' ' * (5 - i) + '*' * i)
# Output: i = 1 -> ' '*(5-1) + '*'*1 -> ' '*4 + '*'     ->     *
#         i = 2 -> ' '*(5-2) + '*'*2 -> ' '*3 + '**'    ->    **
#         i = 3 -> ' '*(5-3) + '*'*3 -> ' '*2 + '***'   ->   ***
#         i = 4 -> ' '*(5-4) + '*'*4 -> ' '*1 + '****'  ->  ****
#         i = 5 -> ' '*(5-5) + '*'*5 -> ' '*0 + '*****' -> *****

print()  # Print a blank line for separation

# ***Pattern 5: Inverted Right-Aligned Triangle of Stars***
for i in range(5, 0, -1):
    print(' ' * (5 - i) + '*' * i)
# Output: i = 5 -> ' '*(5-5) + '*'*5 -> ' '*0 + '*****' -> *****
#         i = 4 -> ' '*(5-4) + '*'*4 -> ' '*1 + '****'  ->  ****
#         i = 3 -> ' '*(5-3) + '*'*3 -> ' '*2 + '***'   ->   ***
#         i = 2 -> ' '*(5-2) + '*'*2 -> ' '*3 + '**'    ->    **
#         i = 1 -> ' '*(5-1) + '*'*1 -> ' '*4 + '*'     ->     *

# ***Pattern 5: Diamond of Stars***
for i in range(1, 6):
    print(' ' * (5 - i) + '*' * (2*i - 1))
for i in range(4, 0, -1):
    print(' ' * (5 - i) + '*' * (2*i - 1))
# Output: i = 1 -> ' '*(5-1) + '*'*(2*1 -1) -> ' '*4 + '*'                            ->     *
#         i = 2 -> ' '*(5-2) + '*'*(2*2 -1) -> ' '*3 + '*'*(4-1) -> '   ' + '***'     ->    ***
#         i = 3 -> ' '*(5-3) + '*'*(2*3 -1) -> ' '*2 + '*'*(6-1) -> '  ' + '*****'    ->   *****
#         i = 4 -> ' '*(5-4) + '*'*(2*4 -1) -> ' '*1 + '*'*(8-1) -> ' ' + '*******'   ->  *******
#         i = 5 -> ' '*(5-5) + '*'*(2*5 -1) -> ' '*0 + '*'*(10-1) -> '' + '*********' -> *********
#         i = 4 -> ' '*(5-4) + '*'*(2*4 -1) -> ' '*1 + '*'*(8-1) -> ' ' + '*******'   ->  *******
#         i = 3 -> ' '*(5-3) + '*'*(2*3 -1) -> ' '*2 + '*'*(6-1) -> '  ' + '*****'    ->   *****
#         i = 2 -> ' '*(5-2) + '*'*(2*2 -1) -> ' '*3 + '*'*(4-1) -> '   ' + '***'     ->    ***
#         i = 1 -> ' '*(5-1) + '*'*(2*1 -1) -> ' '*4 + '*'                            ->     *

print()  # Print a blank line for separation

# ***Pattern 6: Hollow Square of Stars***
for i in range(1, 6):
    if i == 1 or i == 5:
        print('*' * 5)
    else:
        print('*' + ' ' * 3 + '*')
# Output: i = 1 -> ***** (first row of stars)
#         i = 2 -> *   * (second row with spaces in between)
#         i = 3 -> *   * (third row with spaces in between)
#         i = 4 -> *   * (fourth row with spaces in between)
#         i = 5 -> ***** (fifth row of stars)

print()  # Print a blank line for separation

# ***Pattern 7: Hollow Right-Angled Triangle of Stars***
for i in range(1, 6):
    if i == 1:
        print('*')
    elif i == 5:
        print('*' * 5)
    else:
        print('*' + ' ' * (i - 2) + '*')
# Output: i = 1 -> * (first row with a single star)
#         i = 2 -> * * (second row with a space in between)
#         i = 3 -> *   * (third row with two spaces in between)
#         i = 4 -> *    * (fourth row with three spaces in between)
#         i = 5 -> ***** (fifth row with five stars)

print()  # Print a blank line for separation

# ***Pattern 8: Hollow Pyramid of Stars***
for i in range(1, 6):
    if i == 1:
        print(' ' * (5 - i) + '*')
    elif i == 5:
        print('*' * 9)
    else:
        print(' ' * (5 - i) + '*' + ' ' * (2*i - 3) + '*')
# Output: i = 1 -> ' '*(5-1) + '*' -> ' '*4 + '*'                                       ->     *
#         i = 2 -> ' '*(5-2) + '*' + ' '*(2*2 - 3) + '*' -> ' '*3 + '*' + ' ' + '*'     ->    * *
#         i = 3 -> ' '*(5-3) + '*' + ' '*(2*3 - 3) + '*' -> ' '*2 + '*' + ' '*(3) + '*' ->   *   *
#         i = 4 -> ' '*(5-4) + '*' + ' '*(2*4 - 3) + '*' -> ' '*1 + '*' + ' '*(5) + '*' ->  *     *
#         i = 5 -> '*' * 9                                                              -> ********* (fifth row with nine stars)

print()  # Print a blank line for separation

# ***Pattern 9: Hollow Diamond of Stars***
for i in range(1, 6):
    if i == 1:
        print(' ' * (5 - i) + '*')
    elif i == 5:
        print('*' * 9)
    else:
        print(' ' * (5 - i) + '*' + ' ' * (2*i - 3) + '*')
for i in range(4, 0, -1):
    if i == 1:
        print(' ' * (5 - i) + '*')
    elif i == 5:
        print('*' * 9)
    else:
        print(' ' * (5 - i) + '*' + ' ' * (2*i - 3) + '*')

# Output: i = 1 -> ' '*(5-1) + '*' -> ' '*4 + '*'                                       ->     *
#         i = 2 -> ' '*(5-2) + '*' + ' '*(2*2 - 3) + '*' -> ' '*3 + '*' + ' ' + '*'     ->    * *
#         i = 3 -> ' '*(5-3) + '*' + ' '*(2*3 - 3) + '*' -> ' '*2 + '*' + ' '*(3) + '*' ->   *   *
#         i = 4 -> ' '*(5-4) + '*' + ' '*(2*4 - 3) + '*' -> ' '*1 + '*' + ' '*(5) + '*' ->  *     *
#         i = 5 -> '*' * 9  (fifth row with nine stars)                                 -> *********
#         i = 4 -> ' '*(5-4) + '*' + ' '*(2*4 - 3) + '*' -> ' '*1 + '*' + ' '*(5) + '*' ->  *     *
#         i = 3 -> ' '*(5-3) + '*' + ' '*(2*3 - 3) + '*' -> ' '*2 + '*' + ' '*(3) + '*' ->   *   *
#         i = 2 -> ' '*(5-2) + '*' + ' '*(2*2 - 3) + '*' -> ' '*3 + '*' + ' ' + '*'     ->    * *
#         i = 1 -> ' '*(5-1) + '*' -> ' '*4 + '*'                                       ->     *