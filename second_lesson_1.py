def square(value: int) -> int:
    return value ** 2
##print(square(2))

def calc_sum(a: int, b: int) -> int:
    return a+b

def main():
    a = 3
    b = 5
    calculated_sum = calc_sum(a, b)
    sq = square(calculated_sum)
    return sq ##return square(calc_sum(a:3, b:5)) - если убрать все строчки выше

print(main())



