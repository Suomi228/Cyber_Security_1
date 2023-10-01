def generate_vigenere_table():
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬБЭЮЯ .,"
    table = {}
    for row_char in alphabet:
        table[row_char] = {}
        for col_char in alphabet:
            row_idx = alphabet.index(row_char)
            col_idx = alphabet.index(col_char)
            shifted_char = alphabet[(row_idx + col_idx) % len(alphabet)]
            table[row_char][col_char] = shifted_char
    return table

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬБЭЮЯ .,"
numAlph = {}
for i in range(len(alphabet)):
    numAlph[alphabet[i]] = i

def encrypt(text, key):
    code = ''
    for i in range(len(text)):
        code += alphabet[(numAlph[text[i]] + numAlph[key[i % len(key)]]) % len(alphabet)]
    return code

def decrypt(text, key):
    code = ''
    for i in range(len(text)):
        code += alphabet[(numAlph[text[i]] - numAlph[key[i % len(key)]] + len(alphabet)) % len(alphabet)]
    return code

message = input("ВВЕДИТЕ СООБЩЕНИЕ:")
key = input("ВВЕДИТЕ КЛЮЧ:")
intent = int(input("ВВЕДИТЕ 1 ЕСЛИ ХОТИТЕ ЗАШИФРОВАТЬ, 2 ЕСЛИ РАСШИФРОВАТЬ:"))
while intent not in range(1, 2 + 1):
    intent = int(input("ВВЕДИТЕ 1 ЕСЛИ ХОТИТЕ ЗАШИФРОВАТЬ, 2 ЕСЛИ РАСШИФРОВАТЬ:"))
if intent == 1:
    print("ЗАШИФРОВАННОЕ СООБЩЕНИЕ:"+encrypt(message,key))
else:
    print("РАСШИФРОВАННОЕ СООБЩЕНИЕ:"+decrypt(message,key))

vigenere_table = generate_vigenere_table()

print("Таблица шифра Виженера:")
for row_char in vigenere_table:
    row = ""
    for col_char in vigenere_table[row_char]:
        row += vigenere_table[row_char][col_char] + " "
    print(row)