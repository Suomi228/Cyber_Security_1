alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬБЭЮЯ .,"
circuit1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ[]{}';:<>/?!@#%^&"
circuit2 = "йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ1234"
circuit3 = "QWERTYUIOP[]!@#$%^&*()qwertyuiopasdfghjkl;'zxcvbnm,./|09876543Д1ZXCVB"
circuit4 = "/.,mnbvcxz';lkjhgfdsa][oiuytrewqMNBVCXZLKJHGFDSAPOIUYTREWQюбьтимсчяэж"
circuit5 = "уеъыаоэяиьюйцкнгшщзхфвпрлджчсмтб091Д873465+-=!№;%:?*()_QWEMNBVCXZLKJH"
circuit6 = "1Д34567890-=!@#$%^&*()_+mnbvcxzASDFGHJKLpoiuytrewqMNBVCXZlkjhgfdsaPOI"
circuit7 = "POIUYTREWQASDFGHJKLMNBVCXZzxcvbnmlkjhgfdsapoiuytrewq09876543Д1,./'][+"
circuit8 = "zyxwvutsrqponmlkjihgfedcba .,WVUTSRQPONMLKJIHGFEDCBAимтсьчбяюэждлорпа"
circuit9 = " .,ьыъщшчцхфутсрпонмлкйизжёедгвба103456789ЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЁ"


def crypt(message):
    ciph_message = ""
    cre1 = 0
    cre2 = 0
    cre3 = 0
    next_cicuit = 0
    for letter in message:
        if letter in alphabet:
            position = alphabet.find(letter)
            if letter == " ":
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
                next_cicuit += 1
                cre1 = 0
                cre2 = 0
                cre3 = 0
            else:
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
def encreep(message):
    deciph_message = ""
    enc1 = 0
    enc2 = 0
    enc3 = 0
    next_circuit = 0

    for letter in message:
        if next_circuit % 3 == 0:
            if enc1 % 3 == 0:
                position = circuit1.find(letter)
                if position == alphabet.find(' '):
                    next_circuit += 1
                    enc1 = 0
                else:
                    enc1 += 1
                deciph_message += alphabet[position]
            elif enc1 % 3 == 1:
                position = circuit2.find(letter)
                if position == alphabet.find(' '):
                    next_circuit += 1
                    enc1 = 0
                else:
                    enc1 += 1
                deciph_message += alphabet[position]
            elif enc1 % 3 == 2:
                position = circuit3.find(letter)
                if position == alphabet.find(' '):
                    next_circuit += 1
                    enc1 = 0
                else:
                    enc1 += 1
                deciph_message += alphabet[position]
        elif next_circuit % 3 == 1:
            if enc2 % 3 == 0:
                position = circuit4.find(letter)
                if position == alphabet.find(' '):
                    next_circuit += 1
                    enc2 = 0
                else:
                    enc2 += 1
                deciph_message += alphabet[position]
            elif enc2 % 3 == 1:
                position = circuit5.find(letter)
                if position == alphabet.find(' '):
                    next_circuit += 1
                    enc2 = 0
                else:
                    enc2 += 1
                deciph_message += alphabet[position]
            elif enc2 % 3 == 2:
                position = circuit6.find(letter)
                if position == alphabet.find(' '):
                    next_circuit += 1
                    enc2 = 0
                else:
                    enc2 += 1
                deciph_message += alphabet[position]
        elif next_circuit % 3 == 2:
            if enc3 % 3 == 0:
                position = circuit7.find(letter)
                if position == alphabet.find(' '):
                    next_circuit += 1
                    enc3 = 0
                else:
                    enc3 += 1
                deciph_message += alphabet[position]
            elif enc3 % 3 == 1:
                position = circuit8.find(letter)
                if position == alphabet.find(' '):
                    next_circuit += 1
                    enc3 = 0
                else:
                    enc3 += 1
                deciph_message += alphabet[position]
            elif enc3 % 3 == 2:
                position = circuit9.find(letter)
                if position == alphabet.find(' '):
                    next_circuit += 1
                    enc3 = 0
                else:
                    enc3 += 1
                deciph_message += alphabet[position]

    print("ВАШЕ РАСШИФРОВАННОЕ СООБЩЕНИЕ:" + deciph_message)


message = input("ВВЕДИТЕ СООБЩЕНИЕ:")
intent = int(input("ВВЕДИТЕ 1 ЕСЛИ ХОТИТЕ ЗАШИФРОВАТЬ, 2 ЕСЛИ РАСШИФРОВАТЬ:"))
while intent not in range(1, 2 + 1):
    intent = int(input("ВВЕДИТЕ 1 ЕСЛИ ХОТИТЕ ЗАШИФРОВАТЬ, 2 ЕСЛИ РАСШИФРОВАТЬ:"))
if intent == 1:
    crypt(message)
else:
    encreep(message)

print("\nВАШ АЛФАВИТ:" + alphabet)
print("ВАШ ДОПОЛНИТЕЛЬНЫЙ АЛФАВИТ НОМЕР 1:" + circuit1)
print("ВАШ ДОПОЛНИТЕЛЬНЫЙ АЛФАВИТ НОМЕР 2:" + circuit2)
print("ВАШ ДОПОЛНИТЕЛЬНЫЙ АЛФАВИТ НОМЕР 3:" + circuit3)
print("ВАШ ДОПОЛНИТЕЛЬНЫЙ АЛФАВИТ НОМЕР 4:" + circuit4)
print("ВАШ ДОПОЛНИТЕЛЬНЫЙ АЛФАВИТ НОМЕР 5:" + circuit5)
print("ВАШ ДОПОЛНИТЕЛЬНЫЙ АЛФАВИТ НОМЕР 6:" + circuit6)
print("ВАШ ДОПОЛНИТЕЛЬНЫЙ АЛФАВИТ НОМЕР 7:" + circuit7)
print("ВАШ ДОПОЛНИТЕЛЬНЫЙ АЛФАВИТ НОМЕР 8:" + circuit8)
print("ВАШ ДОПОЛНИТЕЛЬНЫЙ АЛФАВИТ НОМЕР 9:" + circuit9)
