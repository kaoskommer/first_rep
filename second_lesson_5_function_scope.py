x = 100

def change_var():
    x=5
    print(x)

change_var()
print(x)

#уровни видимости: локальный (на уровне функции), объемлющий (функция внутри функции), глобальный (объявленный раньше всех), системный
#если нет локальной переменной, будет выполняться поиск глобальной