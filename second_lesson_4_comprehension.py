#1 простой вариант выведения четных чисел
from tomlkit import key_value

# integer = [0,1,2,3,4,5,6,7,8,9]
#
# new_list = [] #говорим, что это будет новый список
#
# for num in integer:
#     if num % 2 == 0:
#         new_list.append(num) #добавить значение внутрь нового списка

# print(new_list)

#2 более сложный питоновский путь выведения только четных чисел

# integers = [0,1,2,3,4,5,6,7,8,9]
#
# my_gen = [num for num in integers if num % 2 == 0]
# #если нужно вывести только уникальные значения из списка выше, то используем {} вместо []
# #
#
# print(my_gen)

#3 объединение двух списков
keys = ["a", "b", "c", "d"]
values = [1,2,3,4,5,6,7]

key_value = {k: v for k, v in zip(keys, values)}
print(key_value)
















