# 1. Создайте функцию для проверки пароля
# 2. Пароль должен быть минимум 8 символов
# 3. В пароле должно быть:
#   - буквы в нижнем регистре
#   - буквы в верхнем решистре
#   - цифры
#   - специальные символы
# 4. Попросите пользователя ввести пароль в терминале и проверьте его


import re


def check_password(password):
    length_pattern = re.compile(r"\S{8,}")
    lowercase_pattern = re.compile(r"^.*[a-z]+.*$")
    uppercase_pattern = re.compile(r"^.*[A-Z+]+.*$")
    number_pattern = re.compile(r"^.*[0-9]+.*$")
    special_symbol_pattern = re.compile(r"^.*[@%#!&*^]+.*$")
    no_whitespace_pattern = re.compile(r"^\S*$")

    if not re.fullmatch(no_whitespace_pattern, password):
        return (False, "No whitespaces allowed in the password")

    if not re.fullmatch(length_pattern, password):
        return (False, "Password must have at least 8 symbols")

    if not re.fullmatch(lowercase_pattern, password):
        return (False, "Password must have at least one lowercase letter")

    if not re.fullmatch(uppercase_pattern, password):
        return (False, "Password must have at least one uppercase letter")

    if not re.fullmatch(number_pattern, password):
        return (False, "Password must have at least one number")

    if not re.fullmatch(special_symbol_pattern, password):
        return (False, "Password must have at least one special symbol @%#!&*^")

    return (True, "Password is valid!")


while True:
    password = input("Введите пароль: ")
    password_check_res = check_password(password)
    if password_check_res[0]:
        print(password_check_res[1])
        break

    print(password_check_res[1])
