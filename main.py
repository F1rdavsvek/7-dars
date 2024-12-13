# user = ['Toxir', 'Sobir', 'Bakir', 'Jalil']
# iter_user = iter(user)
# print(next(iter_user))
# print(next(iter_user))
# print(next(iter_user))
# print(next(iter_user))
# print(next(iter_user))
# from collections.abc import Iterable

# for users in user:
#     print(users)

# user = ['Toxir', 'Sobir', 'Bakir', 'Jalil']
#
# class customIterator:
#     def __init__(self, user: Iterable):
#         self.__user = user
#         self.__index = -1
#
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.__index += 1
#         if self.__index >= len(self.__user):
#             raise StopIteration("Element qolmadi!!!")
#         return self.__user[self.__index]
#
# a = customIterator(user)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# def custome_generator():
#     yield 'salom'
# 1-usul
# print(list(custome_generator()))
# 2-usul
# for user in custome_generator():
#     print(user)
#
# def generate_number():
#     for i in range(1000000):
#         yield i
# print(generate_number().__sizeof__())
# nums =[i for i in range(1000000)]
# print(nums.__sizeof__())

