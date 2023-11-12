def parse_cell_coordinates(cells):
    arr_cell = []
    for cell in cells:
        coordinates = cell.split(" ")
        arr_cell.append([int(coordinates[0]) - 1, int(coordinates[1]) - 1])
    return arr_cell

def calculate_table_count(string, coll, line, cell_count):
    len_str = len(string) + cell_count
    cnt_table = len(string) // (coll * line - cell_count)
    if len_str != coll * line:
        cnt_table += 1
    return cnt_table

def read_key(coll):
    key = []
    str_key = input("Введите ключ, отделяя каждую цифру пробелом: ").split(" ")
    while len(str_key) != coll:
        print("Количество цифр в ключе должно совпадать с количеством столбцов таблицы!")
        str_key = input("Введите ключ, отделяя каждую цифру пробелом: ").split(" ")
    for digit in str_key:
        key.append(int(digit) - 1)
    return key
def encode_message(string, line, coll, arr_cell, cnt_table):
    tables = [[[0 for _ in range(coll)] for _ in range(line)] for _ in range(cnt_table)]
    k = 0
    for i in range(len(tables)):
        for j in range(line):
            for l in range(coll):
                if k >= len(string):
                    break
                elif is_cell_valid(arr_cell, j, l):
                    tables[i][j][l] = string[k]
                    k += 1
                print(tables[i][j][l], end="\t")
            if k >= len(string):
                break
            print()
        print()
    return tables

def print_encoded_message(tables, coll, key):
    print("\nЗашифрованное сообщение: ")
    for table in tables:
        for j in range(coll):
            for l in range(len(tables[0])):
                if table[l][index_of(key, j)] != 0:
                    print(table[l][index_of(key, j)], end="")



def decode_message(string, line, coll, arr_cell, cnt_table, key):
    tables = [[[0 for _ in range(coll)] for _ in range(line)] for _ in range(cnt_table)]
    remains = 0
    k = 0
    a = coll * line - len(arr_cell)

    if len(string) < a:
        remains = a - len(string)
    else:
        remains = a - len(string) % a

    for i in range(line - 1, -1, -1):
        for j in range(coll - 1, -1, -1):
            if is_cell_valid(arr_cell, i, j):
                tables[cnt_table - 1][i][j] = 1
                remains -= 1
            if remains == 0:
                break
        if remains == 0:
            break

    for i in range(cnt_table):
        for j in range(coll):
            index = index_of(key, j)
            for l in range(line):
                if tables[i][l][index] != 1 and is_cell_valid(arr_cell, l, index):
                    tables[i][l][index] = string[k]
                    k += 1
                    if k >= len(string):
                        break
            if k >= len(string):
                break

    return tables


def print_decoded_message(tables):
    found_flag = False
    for table in tables:
        for row in table:
            for cell in row:
                if cell == 1:
                    found_flag = True
                    break
                print(cell, end="\t")
            if found_flag:
                break
            print()
        if found_flag:
            break
        print()

    print("\nРасшифрованное сообщение: ")
    for table in tables:
        for row in table:
            for cell in row:
                if cell != 1 and cell != 0:
                    print(cell, end="")
def is_cell_valid(cells, i, j):
    for cell in cells:
        if cell[0] == i and cell[1] == j:
            return False
    return True

def index_of(key, index):
    for i in range(len(key)):
        if key[i] == index:
            return i
    return -1


print("Введите 1 если хотите зашифровать, 2 если расшифровать")

choice = int(input())
str_input = input("Введите сообщение: ")
line_input = int(input("Введите количество строк таблицы: "))
coll_input = int(input("Введите количество столбцов таблицы: "))
cells = input("Введите координаты ячеек через запятую(Формат ввода: 1 1, 2 4, 3 3) где первое число это номер строки, а второе - номер столбца: ").split(", ")
arr_cell = parse_cell_coordinates(cells)
key = read_key(coll_input)
cnt_table = calculate_table_count(str_input, coll_input, line_input, len(arr_cell))

if choice==1:
    tables = encode_message(str_input, line_input, coll_input, arr_cell, cnt_table)
    print_encoded_message(tables, coll_input, key)
elif choice==2:
    tables = decode_message(str_input, line_input, coll_input, arr_cell, cnt_table, key)
    print_decoded_message(tables)
else:
    print("Ошибка ввода!")
