alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬБЭЮЯ .,"
circuit1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ[]{}';:<>/?!@#%^&"
circuit2 = "йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ1234"
circuit3 = "QWERTYUIOP[]!@#$%^&*()qwertyuiopasdfghjkl;'zxcvbnm,./|0987654321ZXCVB"

def creep(message, circuit1, circuit2, circuit3):
    ciph_message = ""
    cre = 0
    for letter in message:
        if letter in alphabet:
            position = alphabet.find(letter)
            if cre % 3 == 0:
                ciph_message += circuit1[position]
            elif cre % 3 == 1:
                ciph_message += circuit2[position]
            elif cre % 3 == 2:
                ciph_message += circuit3[position]
            cre += 1
    print("ВАШЕ ЗАШИФРОВАННОЕ СООБЩЕНИЕ:" + ciph_message)
def encreep(message, circuit1, circuit2, circuit3):
    deciph_message = ""
    enc = 0
    for letter in message:
        if enc%3==0:
            position = circuit1.find(letter)
            deciph_message+=alphabet[position]
        elif enc%3==1:
            position = circuit2.find(letter)
            deciph_message += alphabet[position]
        elif enc%3==2:
            position = circuit3.find(letter)
            deciph_message += alphabet[position]
        enc+=1

    print("ВАШЕ РАСШИФРОВАННОЕ СООБЩЕНИЕ:" + deciph_message)


message = input("ВВЕДИТЕ СООБЩЕНИЕ:")
intent = int(input("ВВЕДИТЕ 1 ЕСЛИ ХОТИТЕ ЗАШИФРОВАТЬ, 2 ЕСЛИ РАСШИФРОВАТЬ:"))
while intent not in range(1, 2 + 1):
    intent = int(input("ВВЕДИТЕ 1 ЕСЛИ ХОТИТЕ ЗАШИФРОВАТЬ, 2 ЕСЛИ РАСШИФРОВАТЬ:"))
if intent == 1:
    creep(message, circuit1, circuit2, circuit3)
else:
    encreep(message, circuit1, circuit2, circuit3)