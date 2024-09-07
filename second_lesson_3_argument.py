#1позиционные аргументы - передают в порядке, указанном в функции

# def positional_args(a,b,c):
#     print(f"a = {a}, b= {b}, c = {c}")
#
# positional_args(2,1,2)


#2 именованные аргументы - будут выводиться c тем значением, какое будет указано при выводе в print. если аргумент с не указать, он примет значение some

# def named_args(a, b, c = "some"):
#     print(f"a = {a}, b= {b}, c = {c}")
#
# named_args(b=210, a=5)
# named_args(b=10, c='aaa', a=5)


#3 случаи, когда кол-во позиционных аргументов не определено, будут упакованы в кортеж, т.е в порядке, указанном при вызове функции
# def func_args(*args):
#     for num in args:
#         print (num)
#     print(f"args = {args}")
#
# func_args("aa", 3, [1,2,3])

# #4 случаи, когда кол-во именованных аргументов не определено, будут укомплектованы в словарь (hashmap)
# def func_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
#     print(f"kwargs = {kwargs}")
#
# func_kwargs(a=1, b=2, some=10, c=76)

#5 случаи, когда именованные и позиционные выводятся вместе
# def any_of_any(*args, **kwargs):
#     print(f"args = {args}")
#     print(f"kwargs = {kwargs}")
#
# any_of_any(1,2,3,4, money=2)


#6 распаковка значения при передаче в функцию
#
# d = {"host": "127.0.0.1", "port": 6435, "topic_name": "smth"}
#
# def func_unpack(host: str,
#                 port: int,
#                 **kwargs):
#     print(f"Config: host: {host}, port: {port}")
#
# func_unpack(**d)

#7 вывод именованного аргумента через * в условии функции
# def example (name: str, *, age: int) -> tuple:
#     return name, age
#
# print(example("Pavel", age=32))
