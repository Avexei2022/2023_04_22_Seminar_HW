from get_number_int import get_number


def create_matrix():
    row_01 = ["1", "", "", ""]
    row_02 = ["2", "", "", ""]
    row_03 = ["3", "", "", ""]
    matrix = [["", "1", "2", "3"], row_01, row_02, row_03]
    return matrix


def print_matrix(matrix):
    print('')
    for i in range(0, 4):
        print(*matrix[i], sep='\t')
    print('')


def print_result_message(message):
    print(f"Поздравляю! Выйграл игрок {message}")


def get_num_row_or_column(mess):
    num_min = 1
    num_max = 3
    message = f"Введите номер {mess} (от {num_min} до {num_max}):"
    mes_false = "Условия ввода не выполнены."
    return get_number(message, num_min, num_max, mes_false)


def get_coordinate(symbol):
    print(f"\nХод игрока '{symbol}'")
    row = get_num_row_or_column('строки')
    column = get_num_row_or_column('столбца')
    return (row, column)


def game_step(symbol):
    flag = True
    while flag:
        row, column = get_coordinate(symbol)
        if matrix[row][column] == "":
            matrix[row][column] = symbol
            flag = False
        else:
            print("Данная клетка занята")


def check_finish(matrix):
    flag = False
    for i in range(1, 4):
        if matrix[i][1] == matrix[i][2] == matrix[i][3] and matrix[i][1] != "":
            print_result_message(matrix[i][1])
            return False
        if matrix[1][i] == matrix[2][i] == matrix[3][i] and matrix[1][i] != "":
            print_result_message(matrix[1][i])
            return False
        for j in range(1, 4):
            if matrix[i][j] == "":
                flag = True
    if (matrix[1][1] == matrix[2][2] == matrix[3][3] or
            matrix[1][3] == matrix[2][2] == matrix[3][1]) and matrix[2][2] != "":
        print_result_message(matrix[2][2])
        return False
    if flag == False:
        print("\nНичья!\n")
    return flag


def game_start(matrix):
    print('Начало игры!')
    print_matrix(matrix)
    flag = True
    symbol = "X"
    while flag:
        game_step(symbol)
        flag = check_finish(matrix)
        if symbol == "X":
            symbol = "0"
        else:
            symbol = "X"
        print_matrix(matrix)


matrix = create_matrix()
game_start(matrix)
