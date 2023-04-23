from random import randint


def sequences(list_num):
    length = len(list_num)
    for i in range(length):
        list_tmp = [list_num[i]]
        for j in range(i, length):
            if list_num[j] > list_tmp[-1]:
                list_tmp.append(list_num[j])
                print(list_tmp)


list_num = [randint(1, 10) for i in range(10)]
print(list_num, ' => ')
sequences(list_num)
