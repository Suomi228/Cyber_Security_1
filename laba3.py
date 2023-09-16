alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬБЭЮЯ .,"
circuit1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ[]{}';:<>/?!@#%^&"
circuit2 = "йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ1234"
circuit3 = "QWERTYUIOP[]!@#$%^&*()qwertyuiopasdfghjkl;'zxcvbnm,./|0987654321ZXCVB"
circuit4 = "/.,mnbvcxz';lkjhgfdsa][oiuytrewqMNBVCXZLKJHGFDSAPOIUYTREWQюбьтимсчяэж"
circuit5 = "уеъыаоэяиьюйцкнгшщзхфвпрлджчсмтб0912873465+-=!№;%:?*()_QWEMNBVCXZLKJH"
circuit6 = "1234567890-=!@#$%^&*()_+mnbvcxzASDFGHJKLpoiuytrewqMNBVCXZlkjhgfdsaPOI"
circuit7 = "POIUYTREWQASDFGHJKLMNBVCXZzxcvbnmlkjhgfdsapoiuytrewq0987654321,./'][+"
circuit8 = "zyxwvutsrqponmlkjihgfedcba .,WVUTSRQPONMLKJIHGFEDCBAимтсьчбяюэждлорпа"
circuit9 = " .,ьыъщшчцхфутсрпонмлкйизжёедгвба123456789ЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЁ"


def creep( message, circuit1, circuit2, circuit3):
    ciph_message = ""
    cre1 = 0
    cre2 = 0
    cre3 = 0
    next_cicuit = 0
    for letter in message:
        if letter in alphabet:
            position = alphabet.find(letter)
            if letter == " ":
                next_cicuit += 1
                cre1 = 0
                cre2 = 0
                cre3 = 0
            if next_cicuit % 3 == 0:
                if cre1 % 3 == 0:
                    ciph_message += circuit1[position]
                elif cre1 % 3 == 1:
                    ciph_message += circuit2[position]
                elif cre1 % 3 == 2:
                    ciph_message += circuit3[position]
                cre1 += 1
            elif next_cicuit % 3 == 1:
                if cre2 % 3 == 0:
                    ciph_message += circuit4[position]
                elif cre2 % 3 == 1:
                    ciph_message += circuit5[position]
                elif cre2 % 3 == 2:
                    ciph_message += circuit6[position]
                cre2 += 1
            elif next_cicuit % 3 == 2:
                if cre3 % 3 == 0:
                    ciph_message += circuit7[position]
                elif cre3 % 3 == 1:
                    ciph_message += circuit8[position]
                elif cre3 % 3 == 2:
                    ciph_message += circuit9[position]
                cre3 += 1
    print("ВАШЕ ЗАШИФРОВАННОЕ СООБЩЕНИЕ:" + ciph_message)


def encreep(message, circuit1, circuit2, circuit3):
    deciph_message = ""
    enc1 = 0
    enc2 = 0
    enc3 = 0
    next_circuit = 0

    for letter in message:
        if letter in alphabet:
            position = alphabet.find(letter)

            if (letter == "%" or letter == "2" or letter == "C"
                    or letter == "я" or letter == "K" or letter == "P"
                    or letter == "]" or letter == "р" or letter == "З"):
                next_circuit += 1
                enc1 = 0
                enc2 = 0
                enc3 = 0

            if next_circuit % 3 == 2:
                if enc1 % 3 == 0:
                    deciph_message += circuit1[position]
                elif enc1 % 3 == 1:
                    deciph_message += circuit2[position]
                elif enc1 % 3 == 2:
                    deciph_message += circuit3[position]
                enc1 += 1

            elif next_circuit % 3 == 1:
                if enc2 % 3 == 0:
                    deciph_message += circuit4[position]
                elif enc2 % 3 == 1:
                    deciph_message += circuit5[position]
                elif enc2 % 3 == 2:
                    deciph_message += circuit6[position]
                enc2 += 1

            elif next_circuit % 3 == 0:
                if enc3 % 3 == 0:
                    deciph_message += circuit7[position]
                elif enc3 % 3 == 1:
                    deciph_message += circuit8[position]
                elif enc3 % 3 == 2:
                    deciph_message += circuit9[position]
                enc3 += 1

    print("ВАШЕ РАСШИФРОВАННОЕ СООБЩЕНИЕ: " + deciph_message)


message = input("ВВЕДИТЕ СООБЩЕНИЕ:")
intent = int(input("ВВЕДИТЕ 1 ЕСЛИ ХОТИТЕ ЗАШИФРОВАТЬ, 2 ЕСЛИ РАСШИФРОВАТЬ:"))
while intent not in range(1, 2 + 1):
    intent = int(input("ВВЕДИТЕ 1 ЕСЛИ ХОТИТЕ ЗАШИФРОВАТЬ, 2 ЕСЛИ РАСШИФРОВАТЬ:"))
if intent == 1:
    creep(message, circuit1, circuit2, circuit3)
else:
    encreep(message, circuit1, circuit2, circuit3)

print("\nВАШ АЛФАВИТ:" + alphabet)
print("ВАШ ДОПОЛНИТЕЛЬНЫЙ АЛФАВИТ НОМЕР 1:" + circuit1)
print("ВАШ ДОПОЛНИТЕЛЬНЫЙ АЛФАВИТ НОМЕР 2:" + circuit2)
print("ВАШ ДОПОЛНИТЕЛЬНЫЙ АЛФАВИТ НОМЕР 3:" + circuit3)

