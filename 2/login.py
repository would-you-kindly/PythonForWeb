from db import list_users
registered_users = list_users()
i = 0
while i < len(registered_users):
    username = registered_users[i][0]
    last_seen = registered_users[i][1]
    print(i + 1, username, last_seen.date)
    i = i + 1

from db import query_user_last_seen, list_users
existing_username = list_users()[0][0]
last_seen = query_user_last_seen(existing_username)
print("Пользователь", existing_username, "последний раз заходил", last_seen)
print("Пользователь shrimp", existing_username, "последний раз заходил",
query_user_last_seen("shrimp"))

email = input("Введите e-mail ")
age = input("Введите ваш год рождения: ")

from auth import make_username
user = make_username('asASdASDsd@asdasd')
print(user)

from datetime import datetime as dt
print(dt.now())
# import datetime
# print(datetime.datetime.now())
ex = dt.now()
print(ex)
print("Месяц:", ex.month)
print("День:", ex.day)
print("Час:", ex.hour)
print("Минута:", ex.minute)
print("Секунда", ex.second)

i = email.find("@")
found = (i != -1)

# correct = False
# while not correct:
#     if email.find("@") != -1:
#         correct = True
#     else:
#         print("Вы ввели неправильный емейл, попробуйте ещё раз:")
#         email = input("Введите емейл: ")


email = input("Введите e-mail ")
while email.find("@") == -1:
    print("неправильный email. Попробуйте еще раз")
    email = input("Введите e-mail ")

# Токенизацией называют процесс превращения строки в набор строк (токенов)
test_string = "какая-то строка с пробелами"
print(test_string.split())
print(test_string.split("-"))
print(test_string.split("с"))
username = email.split("@")[0].lower()
print("Вы вошли как " + username)

def my_function(x, y):
    if x * y < 0:
        z = x**2 + y**2
    else:
        z = 0
    return z < 25

import time # где-то верхушке файла
def get_email_from_user(attempts=5, sleep_duration=15):
    email = input("Введите e-mail: ")
    i = 1
    while (email.find("@") == -1):
        print("неправильный email. Попробуйте еще раз")
        i = i + 1
        email = input("Попытка " + str(i) + ". Введите e-mail: ")
        if i % attempts == 0:
            print("Переборщили с попытками. Подождите " + str(sleep_duration)
            + " секунд")
            time.sleep(sleep_duration)
    return email

get_email_from_user()

