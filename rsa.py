import math
import random

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
        raise ValueError("Оба числа должны быть простыми!.")

    elif p == q:
        raise ValueError("p и q не могут быть одинаковыми.")

    n = p * q
    print("Произведение p и q - Обозначим за (n): ", n)
    phi = (p - 1) * (q - 1)
    print("Функция эйлера (p - 1) * (q - 1) - Обозначим за (phi): ", phi)

    e = random.randrange(1, phi)

    while not(is_prime(e)):
        e = random.randrange(1, phi)

    g = math.gcd(e, phi)

    while g != 1 and not(is_prime(e)):
        e = random.randrange(1, phi)
        g = math.gcd(e, phi)

    d = multiplicative_inverse(e, phi)

    while d == 0:
        e = random.randrange(1, phi)
        while not (is_prime(e)):
            e = random.randrange(1, phi)
        g = math.gcd(e, phi)
        while g != 1 and not (is_prime(e)):
            e = random.randrange(1, phi)
            g = math.gcd(e, phi)

        d = multiplicative_inverse(e, phi)
    print(f"Возьмем случайное простое число e (1 < e < phi), взаимно простое со значением функции Эйлера: e = {e}")
    print(f"Вычислим d по формуле (d*e) mod(phi) = 1. (d*{e}) mod({phi}) = 1: d = {d}")

    return ((e, n), (d, n))

def sign(private_key, plaintext):
    key, n = private_key
    signature = []
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFJHIJKLMNOPQRSTUVWXYZ .,"
    for char in plaintext:
        if char in alphabet:
            message_index = alphabet.index(char)
            signature.append(pow(message_index, key, n))
            print(f"Символ сообщения: '{char}'\n"
                  f"Индекс символа в алфавите (m): {message_index}\n"
                  f"Находим значение символа в подписи по формуле - (m^d) mod(n): ({message_index} ^ {key}) mod ({n}) = {pow(message_index, key, n)}\n"
                  )
    return signature


def verify(public_key, message, signature):
    key, n = public_key
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFJHIJKLMNOPQRSTUVWXYZ .,"
    flag = True
    for i in range(len(message)):
        decrypted_char = pow(signature[i], key, n)
        while decrypted_char > len(alphabet):
            decrypted_char-=len(alphabet)
        print(f"Значение символа в подписи (s):  {signature[i]}\n"
              f"Формула операции - (s^e) mod(n): ({signature[i]} ^ {key}) mod {n} = {decrypted_char}\n"
              f"Индекс символа в алфавите: {decrypted_char}\n"
              f"Символ сообщения: '{alphabet[decrypted_char]}'\n"
              )
        if message[i] != alphabet[decrypted_char]:
            flag = False
            break
    return flag

print("Программа реализует алгоритм цифровой подписи RSA.")
print("1 - Сделать подпись. 2 - Проверить подпись")
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFJHIJKLMNOPQRSTUVWXYZ .,"
print("Используемый алфавит: ",alphabet)
choice = int(input("Выберите действие (1 или 2): "))

if choice == 1:
    p = int(input("Введите простое число p: "))
    q = int(input("Введите  простое число q: "))
    public_key, private_key = generate_keypair(p, q)

    print("\nОткрытый ключ (e, n):", public_key)
    print("\nЗакрытый ключ (d, n):", private_key)

    message = input("\nВведите сообщение для подписи:")
    print()
    signature = sign(private_key, message)

    print("Подпись:", signature)

elif choice == 2:
    message = input("Введите исходное сообщение: ")
    public_key = eval(input("Введите открытый ключ (в формате (e, n)): "))
    signature = eval(input("Введите подпись (в формате [signature]): "))
    print()
    is_valid = verify(public_key, message, signature)
    print("Верность подписи:", is_valid)

else:
    print("Неверный выбор действия.")