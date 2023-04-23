from random import randint

list_num = [randint(1, 10) for i in range(10)]
print(*list_num, sep=', ',end = ' -> ')
list_new = filter(lambda x: x > 5, list_num)
print(*list_new, sep=', ')
