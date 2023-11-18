
import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def multiplicative_inverse(e, phi):
    d = 0
    x1, x2, y1, y2 = 0, 1, 1, 0
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = y2 - temp1 * y1

        x2 = x1
        x1 = x
        y2 = y1
        y1 = y

    if temp_phi == 1:
        d = y2

    return d % phi


def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")

    elif p == q:
        raise ValueError("p and q cannot be equal.")

    n = p * q

    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))

def sign(private_key, plaintext):
    key, n = private_key
    signature = []
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFJHIJKLMNOPQRSTUVWXYZ .,"
    for char in plaintext:
        if char in alphabet:
            message_index = alphabet.index(char)
            signature.append(pow(message_index, key, n))
    return signature


def verify(public_key, message, signature):
    key, n = public_key
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFJHIJKLMNOPQRSTUVWXYZ .,"
    flag = True
    for i in range(len(message)):
        decrypted_char = pow(signature[i], key, n)
        while decrypted_char > len(alphabet):
            decrypted_char-=len(alphabet)
        if message[i] != alphabet[decrypted_char]:
            flag = False
            break
    return flag

# Пользовательский интерфейс
print("1. Сделать подпись")
print("2. Проверить подпись")
choice = int(input("Выберите действие (1 или 2): "))

if choice == 1:
    # Генерация ключей
    p = 17
    q = 19
    public_key, private_key = generate_keypair(p, q)

    # Вывод открытого ключа
    print("Открытый ключ:", public_key)

    # Подпись сообщения
    message = input("Введите сообщение для подписи: ")
    signature = sign(private_key, message)

    # Вывод подписи
    print("Подпись:", signature)

elif choice == 2:
    # Ввод открытого ключа, сообщения и подписи
    #public_key = eval(input("Введите открытый ключ (в формате (e, n)): "))
    public_key = eval('95, 323')
    #message = input("Введите исходное сообщение: ")
    message = "Pривет"
    signature = eval(input("Введите подпись (в формате [signature]): "))
    #signature = eval("[237, 289, 138, 281, 177, 248]")

    # Проверка подписи
    is_valid = verify(public_key, message, signature)
    print("Подпись верна:", is_valid)

else:
    print("Неверный выбор действия.")
