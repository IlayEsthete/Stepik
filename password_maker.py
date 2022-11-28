import random

DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'
chars = []
n = int(input('Сколько паролей Вам сгенерировать? - '))
length_of_password = int(input('Какой длины нужны пароли? - '))
num = input('Включать цифры? (Да/Нет) - ')
up = input('Включать прописные буквы? (Да/Нет) - ')
low = input('Включать строчные буквы? (Да/Нет) - ')
sym = input('Включать символы !#$%&*+-=?@^_  ? (Да/Нет) - ')
il = input('Исключать неоднозначные символы il1Lo0O ? (Да/Нет) - ')

if num.lower() == 'да':
    chars += DIGITS
if up.lower() == 'да':
    chars += LOWERCASE_LETTERS
if low.lower() == 'да':
    chars += UPPERCASE_LETTERS
if sym.lower() == 'да':
    chars += PUNCTUATION
if il.lower() == 'да':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')


def generate_password(n_: int, length: int) -> None:
    """
    Сгенерирует n паролей длины length.
    
    n_ - количество требуемых паролей.
    """
    print('Ваши пароли:')
    for _ in range(n_):
        password = ''

        for _ in range(length):
            password += random.choice(chars)
        print(password)


print(chars)
