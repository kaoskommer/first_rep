from typing import Callable

from collections.abc import Callable


def calc_sum(a: int, b: int) -> int: # -> int - is a "type_hint" which is used for outputting specific type of data. e.g. using 0.5 won't work because it's "float" not "int"
    """this function's used for addition"""
    return a+b

def calc_sub(a: int, b: int) -> int:
    """this function's used for subtraction""" ##doc_string - can be used to output info about function with print
    return a-b

# №1 print below output type of calc_sub
# print(type(calc_sub))
# print(calc_sub.__doc__)
# print(calc_sub.__name__)

# №2 assigning a for calc_sub to calculate
# a = calc_sub
# print(a(10, 5))

# №3 making a list out of our functions above
# my_list = [calc_sub, calc_sum]
#
# for func in my_list:
#     print(func(15,10))

# №4 function is an argument of another function
# def some_func(func: Callable, a: int, b:int) -> None:
#     print(func(a,b))
#
# some_func(func=calc_sum, a=10, b=5)
# some_func(func=calc_sub, a=10, b=5)















