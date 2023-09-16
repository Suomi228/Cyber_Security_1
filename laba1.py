def cipher(message,key,intent,alphabet):
    if intent==2:
        key *= -1
    ciph_message=""
    for letter in message:
        position=alphabet.find(letter)
        new_position=position+key
        while new_position>=69:
            new_position-=69
        if (letter in alphabet):
            ciph_message+=alphabet[new_position]
        else:
            ciph_message=ciph_message+letter
    print("ВАШЕ ЗАШИФРОВАННОЕ СООБЩЕНИЕ:"+ciph_message)
message=input("ВВЕДИТЕ СООБЩЕНИЕ:")
key=int(input("ВВЕДИТЕ СДВИГ АЛФАВИТА(от 1 до 69):"))
while key not in range(1, 69 + 1):
    key = int(input("ВВЕДИТЕ СДВИГ АЛФАВИТА(от 1 до 69):"))
intent=int(input("ВВЕДИТЕ 1 ЕСЛИ ХОТИТЕ ЗАШИФРОВАТЬ, 2 ЕСЛИ РАСШИФРОВАТЬ:"))
while intent not in range(1,2+1):
    intent = int(input("ВВЕДИТЕ 1 ЕСЛИ ХОТИТЕ ЗАШИФРОВАТЬ, 2 ЕСЛИ РАСШИФРОВАТЬ:"))
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя .,АВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬБЭЮЯ"
cipher(message,key,intent,alphabet)
print("Алфавит:"+alphabet)
