
def get_blocked_cells_list(col_n: int, row_n: int) -> list:
    cell_num = input('Введите количество "запрещённых" ячеек: ')
    while not (1 <= int(cell_num) < col_n * row_n):
        print('Вы ввели не корректное число (число должно быть больше 0, но меньше кол-ва ячеек в таблице)')
        cell_num = input('Введите количество "запрещённых" ячеек: ')
    blocked_cells = []
    for _ in range(int(cell_num)):
        cell_col, cell_row = [*input('Введите координаты "запрещённой" ячейки (Формат: 1 1): ').split(), '', ''][:2]
        while not (1 <= int(cell_col) <= col_n and
                   1 <= int(cell_row) <= row_n):
            if not (1 <= int(cell_col) <= col_n):
                print('Вы ввели не корректное число столбцов (число должно быть больше 0, но меньше числа столбцов)')
            elif not (1 <= int(cell_row) <= row_n):
                print('Вы ввели не корректное число строк (число должно быть больше 0, но меньше числа столбцов)')
            else:
                print('Вы ввели не числа (число должно состоять только из цифр)')
            cell_col, cell_row = [*input('Введите координаты "запрещённой" ячейки (Формат: 1 1): ').split(), '', ''][:2]
        blocked_cells.append((int(cell_col) - 1, int(cell_row) - 1))
    return blocked_cells


def code(key_index_to_real_index, col_n, row_n, encrypted_str, blocked_cells):
    code_str = ''
    # Кодируем всю строку по таблицам (запускаем цикл на необходимое кол-во таблиц)
    while True:
        code_table = [['' for _ in range(col_n)] for _ in range(row_n)]
        for blocked_cell in blocked_cells:
            code_table[blocked_cell[1]][blocked_cell[0]] = 'X'
        n_counter = 0
        m_counter = 0
        # Проходимся по кодируемой строке (блок размером с таблицу или меньше) и заполняем табличку
        while True:
            # Иначе добавляем символ в нашу таблицу и удаляем его из текуущего куска шифра
            if code_table[m_counter][n_counter] != '#':
                code_table[m_counter][n_counter] = encrypted_str[0]
                encrypted_str = encrypted_str[1:]
                if not encrypted_str:
                    break

            if n_counter == col_n - 1 and m_counter == row_n - 1:
                break

            n_counter += 1
            if n_counter == col_n:
                m_counter += 1
                n_counter = 0

        # Выводим табличку и наш ключ сверху
        print(' ', '    '.join(str(key_index + 1) for key_index in key_index_to_real_index.keys()))
        print(*code_table, sep='\n')
        print()
        for blocked_cell in blocked_cells:
            code_table[blocked_cell[1]][blocked_cell[0]] = ''

        # Исходя из таблички заполняем строку шифра по столбцам
        for col_index in sorted(key_index_to_real_index.keys()):
            code_str += ''.join([row_list[key_index_to_real_index[col_index]] for row_list in code_table])
        if not encrypted_str:
            break

    return code_str


def decode(key_index_to_real_index, col_n, row_n, encrypted_str, blocked_cells):
    decode_str = ''
    # Декодируем всю строку по таблицам (запускаем цикл на необходимое кол-во таблиц
    while True:
        decode_table = [['' for _ in range(col_n)] for _ in range(row_n)]
        for blocked_cell in blocked_cells:
            decode_table[blocked_cell[1]][blocked_cell[0]] = 'X'

        if len(encrypted_str) < col_n * row_n - len(blocked_cells):
            n_counter = 0
            m_counter = 0
            test_table = [['' for _ in range(col_n)] for _ in range(row_n)]
            for blocked_cell in blocked_cells:
                test_table[blocked_cell[1]][blocked_cell[0]] = 'X'
            counter = len(encrypted_str)
            while True:
                if test_table[m_counter][n_counter] != 'X':
                    test_table[m_counter][n_counter] = '_'
                    counter -= 1
                    if counter == 0:
                        break
                n_counter += 1
                if n_counter == col_n:
                    m_counter += 1
                    n_counter = 0
            empty_place_in_cols = []
            print(*test_table, sep='\n')
            print(empty_place_in_cols, sep='\n')

            for col_index in range(col_n):
                empty_place_in_cols.append(len(['' for col_list in test_table if col_list[col_index] == '_']))

        else:
            empty_place_in_cols = [row_n for _ in range(col_n)]

        n_counter = 0
        m_counter = 0
        # Проходимся по кодируемой строке (блок размером с таблицу или меньше) и заполняем табличку
        while True:
            # Иначе добавляем символ в нашу таблицу и удаляем его из текуущего куска шифра
            if decode_table[m_counter][key_index_to_real_index[n_counter]] != 'X':
                decode_table[m_counter][key_index_to_real_index[n_counter]] = encrypted_str[0]
                encrypted_str = encrypted_str[1:]
                if not encrypted_str:
                    break

            if n_counter == col_n - 1 and m_counter == row_n - 1:
                break

            m_counter += 1
            if m_counter == row_n or m_counter + 1 > empty_place_in_cols[key_index_to_real_index[n_counter]]:
                n_counter += 1
                m_counter = 0

        # Выводим табличку и наш ключ сверху
        print(' ', '    '.join(str(key_index + 1) for key_index in key_index_to_real_index.keys()))
        print(*decode_table, sep='\n')
        print()

        for blocked_cell in blocked_cells:
            decode_table[blocked_cell[1]][blocked_cell[0]] = ''

        for row_list in decode_table:
            for col in row_list:
                decode_str += col
        if not encrypted_str:
            break

    return decode_str


print('Программа реализует решение лабораторной работы №6: "Перестановка, усложненная по таблице"')
intent = int(input("ВВЕДИТЕ 1 ЕСЛИ ХОТИТЕ ЗАШИФРОВАТЬ, 2 ЕСЛИ РАСШИФРОВАТЬ:"))
while intent not in range(1, 2 + 1):
    intent = int(input("ВВЕДИТЕ 1 ЕСЛИ ХОТИТЕ ЗАШИФРОВАТЬ, 2 ЕСЛИ РАСШИФРОВАТЬ:"))

message = input("ВВЕДИТЕ СООБЩЕНИЕ:")
print("Длина сообщения:", len(message))
col_num = int(input('Введите количество столбцов: '))
while col_num < 0:
    col_num = input('Введите количество столбцов: ')

row_num = int(input('Введите количество строк: '))
while row_num < 0:
    row_num = int(input('Введите количество строк: '))
key_str = input("ВВЕДИТЕ КЛЮЧ (Формат ввода: 1-1-1-1): ")
while len(key_str.split('-'))!=col_num:
    key_str = input("ВВЕДИТЕ КЛЮЧ (Формат ввода: 1-1-1-1): ")

key_list = [int(key_symbol) for key_symbol in key_str.split('-')]
key = {}
real_index = 0
for index in key_list:
    key[index - 1] = real_index
    real_index += 1
blocked_cells_list = get_blocked_cells_list(col_num, row_num)

if intent==1:
    print('Шифр:', code(key, col_num, row_num, message, blocked_cells_list))
else:
    print('Дешифровка:', decode(key, col_num, row_num, message, blocked_cells_list))
