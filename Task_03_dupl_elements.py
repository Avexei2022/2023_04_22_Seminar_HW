from random import randint


def find_duplicate(list_num):
    list_set = sorted(set(list_num), key=list_num.index)
    list_tmp = list(map(lambda y: list(
        filter(lambda x: x == y, list_num)), list_set))
    count = sum(
        list(filter(lambda x: x > 1, list(map(lambda x: len(x), list_tmp)))))
    return (count, list_set)


list_num = [randint(1, 10) for i in range(10)]
count, list_uniq = find_duplicate(list_num)
print(f"\n{list_num}", end=" => ")
print(f"{count} элемента совпадают")
print(f"Список уникальных элементов {list_uniq}\n")
