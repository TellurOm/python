def count_case(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count

sample_string = 'The quick Brow Fox'
upper, lower = count_case(sample_string)
print(f'No. of Upper case characters : {upper}')
print(f'No. of Lower case Characters : {lower}')

def unique_elements(lst):
    return list(set(lst))

sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
unique_list = unique_elements(sample_list)
print('Unique List :', unique_list)

def is_perfect(n):
    if n < 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

# Example usage
print(is_perfect(6))  # True
print(is_perfect(28))  # True

def sort_hyphenated_words(s):
    words = s.split('-')
    words.sort()
    return '-'.join(words)

input_string = 'green-red-yellow-black-white'
sorted_words = sort_hyphenated_words(input_string)
print(sorted_words)

def positional_args(arg1, arg2):
    print(f'Argument 1: {arg1}, Argument 2: (arg2')

positional_args(10, 20)


def keyword_args(arg1, arg2):
    print(f'Argument 1: {arg1}, Argument 2: {arg2}')

keyword_args(arg2=20, arg1=10)

def mixed_args(arg1, arg2, arg3='default'):
    print(f'Positional Arg 1: {arg1}, Positional Arg 2: {arg2}, Keyword Arg: {arg3}')

mixed_args(10, 20, arg3='custom')

def default_arg(arg1, arg2=5):
    return arg1 + arg2

print(default_arg(10))  # Uses default for arg2
print(default_arg(10, 15))  # Overrides default

def variable_args(*args):
    return sum(args)

print(variable_args(1, 2, 3, 4))  # 10

def variable_keyword_args(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

variable_keyword_args(a=1, b=2, c=3)

def add(x: float, y: float) -> float:
    return x + y

def subtract(x: float, y: float) -> float:
    return x - y

if __name__ == "__main__":
    # Example usage
    print(add(5, 3))      # 8
    print(subtract(5, 3)) # 2

import math

print(math.ceil(5.2))       # 6
print(math.trunc(5.9))      # 5
print(math.floor(5.9))      # 5
print(math.factorial(5))    # 120
print(math.fabs(-5.5))      # 5.5
print(math.pow(2, 3))       # 8
print(math.fmod(5, 2))      # 1.0
print(math.fsum([1, 2, 3])) # 6.0
print(math.prod([1, 2, 3])) # 6
print(math.sqrt(16))        # 4.0

import random

print(random.random())      # Random float [0.0, 1.0)
print(random.randint(1, 10))# Random integer between 1 and 10
print(random.uniform(1, 10))# Random float between 1 and 10
print(random.choice(['apple', 'banana', 'cherry'])) # Random choice
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)        # Shuffle the list
print(lst)
print(random.randrange(1, 10, 2)) # Random odd number between 1 and 10

def remove_duplicates(lst):
    return list(set(lst))

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

def have_common_member(list1, list2):
    return any(item in list2 for item in list1)

print(have_common_member([1, 2, 3], [3, 4, 5]))  # True

def remove_even(lst):
    return [num for num in lst if num % 2 != 0]

print(remove_even([1, 2, 3, 4, 5, 6]))  # [1, 3, 5]

def second_smallest(lst):
    unique_sorted = sorted(set(lst))
    return unique_sorted[1] if len(unique_sorted) > 1 else None

print(second_smallest([3, 1, 2, 2, 5]))  # 2

def split_every_n(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

print(split_every_n([1, 2, 3, 4, 5, 6], 2))  # [[1, 2], [3, 4], [5, 6]]

def union_and_intersection(list1, list2):
    union = list(set(list1) | set(list2))
    intersection = list(set(list1) & set(list2))
    return union, intersection

print(union_and_intersection([1, 2, 3], [3, 4, 5]))

def is_palindrome(lst):
    return lst == lst[::-1]

print(is_palindrome([1, 2, 3, 2, 1]))  # True

def menu():
    lst = []
    while True:
        print("1. Insert\n2. Delete\n3. Access\n4. Update\n5. Traverse\n6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            item = input("Enter item to insert: ")
            lst.append(item)
        elif choice == '2':
            item = input("Enter item to delete: ")
            lst.remove(item)
        elif choice == '3':
            index = int(input("Enter index to access: "))
            print(lst[index])
        elif choice == '4':
            index = int(input("Enter index to update: "))
            item = input("Enter new item: ")
            lst[index] = item
        elif choice == '5':
            print(lst)
        elif choice == '6':
            break

nested_list = [[1, 2], [3, 4], [5, 6]]

# Accessing elements
print(nested_list[1][0])  # 3

# Adding an element
nested_list[0].append(5)
print(nested_list)  # [[1, 2, 5], [3, 4], [5, 6]]

# Deleting an element
del nested_list[1]
print(nested_list)  # [[1, 2, 5], [5, 6]]

a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# i. Print Complete list
print(a)

# ii. Print 4th element of list
print(a[3])

# iii. Print list from 0th to 4th index.
print(a[0:5])

# iv. Print list -7th to 3rd element
print(a[-7:4])

# v. Appending an element to list.
a.append(110)
print(a)

# vi. Sorting the element of list.
a.sort()
print(a)

# vii. Popping an element.
a.pop()
print(a)

# viii. Removing Specified element.
a.remove(20)
print(a)

# ix. Entering an element at specified index.
a.insert(1, 15)
print(a)

# x. Counting the occurrence of a specified element.
print(a.count(30))

# xi. Extending list.
a.extend([120, 130])
print(a)

# xii. Reversing the list.
a.reverse()
print(a)

def add_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]
result = add_matrices(matrix1, matrix2)
print(result)  # [[8, 10, 12], [14, 16, 18]]

l1 = [1, 'x', 4, 5.6, 'z', 9, 'a', 0, 4]
l2 = [x for x in l1 if isinstance(x, int)]
print(l2)  # [1, 9, 0, 4]

def tuple_sum(t1, t2):
    return tuple(a + b for a, b in zip(t1, t2))

t1 = (1, 2, 3, 4)
t2 = (3, 5, 2, 1)
result = tuple_sum(t1, t2)
print(result)  # (4, 7, 5, 5)

def tuples_to_lists(tuples):
    return [list(t) for t in tuples]

original = [(1, 2), (2, 3), (3, 4)]
result = tuples_to_lists(original)
print(result)  # [[1, 2], [2, 3], [3, 4]]

def remove_empty_tuples(tuples):
    return [t for t in tuples if t]

tuples = [(1, 2), (), (3, 4), (), (5,)]
result = remove_empty_tuples(tuples)
print(result)  # [(1, 2), (3, 4), (5,)]

def string_to_tuple(s):
    return tuple(s)

result = string_to_tuple("Hello")
print(result)  # ('H', 'e', 'l', 'l', 'o')

def product_of_tuple(t):
    product = 1
    for num in t:
        product *= num
    return product

t = (1, 2, 3, 4)
result = product_of_tuple(t)
print(result)  # 24

squares = [x**2 for x in range(1, 21)]
print(squares)

def remove_item(s, item):
    s.discard(item)
    return s

s = {1, 2, 3, 4}
print(remove_item(s, 2))  # {1, 3, 4}

def no_common_elements(set1, set2):
    return set1.isdisjoint(set2)

print(no_common_elements({1, 2, 3}, {4, 5, 6}))  # True

def unique_items(set1, set2):
    return set1.union(set2)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(unique_items(set1, set2))  # {1, 2, 3, 4, 5}

def set_to_string(s):
    return ''.join(str(item) for item in s)

s = {1, 2, 3}
print(set_to_string(s))  # '123'

def count_vowels(s):
    vowels = set('aeiouAEIOU')
    return sum(1 for char in s if char in vowels)

print(count_vowels("Hello World"))  # 3

cubes = {x**3 for x in range(2, 13, 2)}
print(cubes)  # {8, 64, 216, 1000, 512, 27}

def sort_dict_by_value(d, ascending=True):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=not ascending))

d = {'a': 1, 'b': 3, 'c': 2}
print(sort_dict_by_value(d))  # Ascending
print(sort_dict_by_value(d, ascending=False))  # Descending

def remove_duplicates_dict(d):
    return {k: v for k, v in d.items() if v not in d.values()}

d = {'a': 1, 'b': 1, 'c': 2}
print(remove_duplicates_dict(d))  # {'c': 2}

def combine_dicts(d1, d2):
    for key in d2:
        if key in d1:
            d1[key] += d2[key]
        else:
            d1[key] = d2[key]
    return d1

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
print(combine_dicts(d1, d2))  # {'a': 1, 'b': 5, 'c': 4}

def char_count(s):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

print(char_count("hello world"))

def match_dicts(d1, d2):
    return {k: v for k, v in d1.items() if k in d2 and d1[k] == d2[k]}

d1 = {'a': 1, 'b': 2}
d2 = {'b': 2, 'c': 3}
print(match_dicts(d1, d2))  # {'b': 2}

def convert_prices_to_pounds(prices):
    return {item: round(price * 0.73, 2) for item, price in prices.items()}

old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
print(convert_prices_to_pounds(old_price))

def even_age_dict(original_dict):
    return {k: v for k, v in original_dict.items() if v % 2 == 0}

original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
print(even_age_dict(original_dict))
