
def display_encryption_result(message, key, alphabet):
    res = ""
    for i in range(len(message)):
        message_char = message[i]
        key_char = key[i]
        message_index = alphabet.index(message_char)
        key_index = alphabet.index(key_char)
        if message_index >= 0 and key_index >= 0:
            message_binary = format(message_index, '08b')
            key_binary = format(key_index, '08b')
            result_index = message_index ^ key_index
            while result_index >= len(alphabet):
                result_index -= len(alphabet)
            result_char = alphabet[result_index]
            res += result_char
            print(f"Символ сообщения: {message_char}\n"
                  f"Индекс символа в десятичной системе: {message_index}\n"
                  f"Индекс символа в двоичной системе:  {message_binary}\n"
                  f"Символ гаммы: {key_char}\n"
                  f"Индекс гаммы в десятичной системе: {key_index}\n"
                  f"Индекс гаммы в двоичной системе: {key_binary}\n"
                  f"Операция XOR: {format(result_index, '08b')}\n"
                  f"Полученный символ: '{result_char}'\n")
    print("Ваше сообщение:" + res)
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFJHIJKLMNOPQRSTUVWXYZ .,"
print()
print("Программа реализует 7-ю лабораторную работу 'Гаммирование'(XOR).")
print("Алфавит, который используется при кодировании:", alphabet)
str_ = input("Введите сообщение: ")
key = input("Введите ключ (гамму): ")

while len(key) > len(str_) or not key:
    key = input("Ключ не должен быть больше сообщения или пустым!")

while len(str_) > len(key):
    key += key

key = key[:len(str_)]
display_encryption_result(str_, key, alphabet)
