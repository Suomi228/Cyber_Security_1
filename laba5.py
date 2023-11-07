from math import ceil

def encrypt(key, col_n, row_n, message):
    code_str = ''
    for tab_index in range(ceil(len(message) / (col_n * row_n))):
        code_table = [['' for _ in range(col_n)] for _ in range(row_n)]
        col_counter = 0
        row_counter = 0
        for encrypted_symbol in message[tab_index * (col_n * row_n):(tab_index + 1) * (col_n * row_n)]:
            code_table[row_counter][col_counter] = encrypted_symbol
            col_counter += 1
            if col_counter == col_n:
                row_counter += 1
                col_counter = 0

        print(' ', '    '.join(str(key_index + 1) for key_index in key.keys()))
        print(*code_table, sep='\n')
        print()

        for col_index in sorted(key.keys()):
            encrypted_letters = []
            for row_list in code_table:
                encrypted_letter = row_list[key[col_index]]
                encrypted_letters.append(encrypted_letter)
            encrypted_word = ''.join(encrypted_letters)
            code_str += encrypted_word

    return code_str


def decrypt(key, col_n, row_n, message):
    decode_str = ''
    for tab_index in range(ceil(len(message) / (col_n * row_n))):
        code_table = [['' for _ in range(col_n)] for _ in range(row_n)]
        n_counter = 0

        block_encrypted_str = message[tab_index * (col_n * row_n):(tab_index + 1) * (col_n * row_n)]
        filed_rows = ceil(len(block_encrypted_str) / col_n)
        filed_cols = len(block_encrypted_str) % col_n
        all_col_list = []
        if len(block_encrypted_str) < col_n * row_n:
            for col_index in range(col_n):
                col_str = ''
                counter = 0
                while True:
                    if counter == filed_rows:
                        break
                    if counter == filed_rows - 1 and key[col_index] + 1 > filed_cols:
                        break
                    col_str += block_encrypted_str[0]
                    block_encrypted_str = block_encrypted_str[1:]
                    counter += 1
                all_col_list.append(col_str)
        else:
            for i_st in range(0, len(block_encrypted_str), row_n):
                col_str = ''
                for row_index in range(row_n):
                    col_str += block_encrypted_str[i_st + row_index]
                all_col_list.append(col_str)

        for col_list in all_col_list:
            for m_counter in range(row_n):
                if m_counter < len(col_list):
                    code_table[m_counter][key[n_counter]] = col_list[m_counter]
            n_counter += 1

        print(' ', '    '.join(str(key_index + 1) for key_index in key.keys()))
        print(*code_table, sep='\n')
        print()

        for row_list in code_table:
            for col in row_list:
                decode_str += col
    return decode_str


intent = int(input("ВВЕДИТЕ 1 ЕСЛИ ХОТИТЕ ЗАШИФРОВАТЬ, 2 ЕСЛИ РАСШИФРОВАТЬ:"))
while intent not in range(1, 2 + 1):
    intent = int(input("ВВЕДИТЕ 1 ЕСЛИ ХОТИТЕ ЗАШИФРОВАТЬ, 2 ЕСЛИ РАСШИФРОВАТЬ:"))

message = input("ВВЕДИТЕ СООБЩЕНИЕ:")

n = int(input('Введите количество столбцов: '))
while n<0:
    n = input('Введите количество столбцов: ')

m = int(input('Введите количество строк: '))
while n<0:
    n = int(input('Введите количество строк: '))

key_str = input("ВВЕДИТЕ КЛЮЧ (Формат ввода: 1-1-1-1): ")
while len(key_str.split('-'))!=n:
    key_str = input("ВВЕДИТЕ КЛЮЧ (Формат ввода: 1-1-1-1): ")

key_list = [int(key_symbol) for key_symbol in key_str.split('-')]
key = {}
real_index = 0
for index in key_list:
    key[index - 1] = real_index
    real_index += 1
if intent == 1:
    print("ЗАШИФРОВАННОЕ СООБЩЕНИЕ:"+encrypt(key, n, m, message))
else:
    print("РАСШИФРОВАННОЕ СООБЩЕНИЕ:"+decrypt(key, n, m, message))
