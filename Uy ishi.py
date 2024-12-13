# oddiy iteratorlar
# 1
# class SimpleIterator:
#     def __init__(self):
#         self.current = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current > 10:
#             raise StopIteration
#         else:
#             value = self.current
#             self.current += 1
#             return value
#
# iterator = SimpleIterator()
# for number in iterator:
#     print(number)
from email.generator import Generator

# ------------------------------------
# 2
# my_list = [10, 20, 30, 40, 50]
# iterator = iter(my_list)
#
# for item in iterator:
#     print(item)

# ---------------------------------------
# 3
# class ReverseListIterator:
#     def __init__(self, some_list):
#         self.list = some_list
#         self.index = len(some_list) - 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < 0:
#             raise StopIteration
#         value = self.list[self.index]
#         self.index -= 1
#         return value
#
#
# my_list = [1, 2, 3, 4, 5]
# reverse_iterator = ReverseListIterator(my_list)
# for item in reverse_iterator:
#     print(item)

# -----------------------------------------
# 4
# text = "Python"
# char_iterator = iter(text)
#
# for char in char_iterator:
#     print(char)

# ----------------------------------------------
# 5
# class EvenNumbers:
#     def __init__(self, numbers):
#         self.numbers = numbers
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.index < len(self.numbers):
#             value = self.numbers[self.index]
#             self.index += 1
#             if value % 2 == 0:
#                 return value
#         raise StopIteration
#
# numbers = [1, 2, 3, 4, 5, 6]
# even_iterator = EvenNumbers(numbers)
# for even in even_iterator:
#     print(even)

# ----------------------------------------------------------------
# 6
# numbers = [1, 2, 3, 4, 5]
# iterator = iter(numbers)
# total = sum(iterator)
# print("Sum:", total)

# -------------------------------------------
# 7
# numbers = [1, 2, 3, 4, 5]
# target = 4
# iterator = iter(numbers)
#
# found = False
# for num in iterator:
#     if num == target:
#         found = True
#         break
#
# print(f"{target} found:", found)

# ---------------------------------------------
# Generators
# 1
# def my_range(start, end):
#     current = start
#     while current < end:
#         yield current
#         current += 1
#
# for number in my_range(1, 10):
#     print(number)

# -----------------------------
# 2
# def word_lengths(sentence):
#     for word in sentence.split():
#         yield len(word)
#
#
# for length in word_lengths("Python programming is fun"):
#     print(length)

# --------------------------
# 3
# def odd_numbers(limit):
#     for number in range(1, limit + 1, 2):
#         yield number
#
# for odd in odd_numbers(10):
#     print(odd)

# --------------------------------
# 4
# def even_numbers(limit):
#     for number in range(2, limit + 1, 2):
#         yield number
#
# for even in even_numbers(10):
#     print(even)

# -----------------------------------------
# 5
# def infinite_sequence():
#     num = 1
#     while True:
#         yield num
#         num += 1
#
# gen = infinite_sequence()
# for _ in range(10):
#     print(next(gen))

# -----------------------------------------------------
# 6
# def square_numbers(limit):
#     for number in range(1, limit + 1):
#         yield number ** 2
#
# for square in square_numbers(5):
#     print(square)

# ---------------------------------------------------
# 7
# def sum_generator(numbers):
#     yield sum(numbers)
#
# numbers = [1, 2, 3, 4, 5]
# for total in sum_generator(numbers):
#     print("Sum:", total)

# -----------------------------------
# 8
# def positive_numbers(numbers):
#     for num in numbers:
#         if num > 0:
#             yield num
#
# nums = [-3, -2, 0, 1, 4, -1]
# for positive in positive_numbers(nums):
#     print(positive)

# -------------------------------
# 9
# import random
#
#
# def random_numbers(limit, count):
#     for _ in range(count):
#         yield random.randint(1, limit)
#
#
# for rand in random_numbers(100, 5):
#     print(rand)

# ----------------------------------------------------
# 10
# def primes(n):
#     def is_prime(num):
#         if num < 2:
#             return False
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True
#
#     count = 0
#     current = 2
#     while count < n:
#         if is_prime(current):
#             yield current
#             count += 1
#         current += 1
#
# for prime in primes(5):
#     print(prime)

# ------------------------------------------------
# 11
# def reverse_string(text):
#     for char in reversed(text):
#         yield char
#
# for char in reverse_string("Python"):
#     print(char, end="")

# -----------------------------------------------------
# 12
# def product_up_to(n):
#     product = 1
#     for num in range(1, n + 1):
#         product *= num
#         yield product
#
# for product in product_up_to(5):
#     print(product)
