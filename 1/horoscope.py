a = "вЕнЕрА в доМЕ рЫб"
b = "СатУрн В ВОДОлее"
c = "Когда-ТО БуДЕт ЧетВерг"

print(a.title())
print(b.title())
print(c.title())

print("Впереди" + " большие " + "неожиданности")
print(7 == 5, 42 > 13, 144**(1/2))
print(2 * 7 - 10 > 2**4)

# Остаток от деления
z = 42
print("Число z четное?", z % 2 == 0)

y = "2000"
is_leap = (int(y) % 4) == 0
print("Год " + y + " является високосным?", is_leap)

# tuples are immutable - кортежи неизменяемые
t = (2, 12, 85, 7)
print("Тапл:", t)
print("Второй элемент тапла:", t[1])
L = [3, 4, 15, 16, 23, 42]
print("Список:", L)
print("Третий элемент списка:", L[2])

t1 = (2, 12, 85, 7)
t2 = (32, 12, 6)
t = t1 + t2
print(t)
L1 = [2, 12]
L1.append(85)
L1 = L1 + [7]
L2 = [32, 12, 6]
L = L1 + L2
print(L)

planets = ["Земля", "Венера", "Меркурий"]
print(planets)
planets.append("Марс")
planets.append("Сатурн")
print(planets)
print(planets + ["Уран", "Нептун"])
planets.pop(2)
print(planets)

locations = {} # пустой словарь
locations["Валентин"] = "Москва"
locations["Андрей"] = "Санкт-Петербург"
locations["Светлана"] = "Казань"
print(locations)
print("Иван" in locations)
print("Валентин" in locations)

a = 5
if a < 10:
    print("Я, великий Каа, вижу вы указали однозначное число")

name = "Константин"
if len(name) > 5:
    print("Какое длинное имя, " + name + "!")
else:
    print("К нам приходит " + name)


month = 7
all_months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль",
"Август", "Сентябрь", "Ноябрь", "Декабрь"]
if month == 1:
    num_days = 28
elif month > 6:
    if month % 2:
        num_days = 31
    else:
        num_days = 30
else:
    if month % 2:
        num_days = 30
    else:
        num_days = 31
print("В месяце " + all_months[month] + " " + str(num_days) + " дней")

course_by = "skillfactory"
i = 0
while i < len(course_by):
    print("* " + course_by[i] + " *")
    i = i + 1

course_by = "skillfactory"
i = 0
while i < len(course_by):
    print("=" + course_by[i].center(30) + "=")
    i = i + 1

import random
course_by = "skillfactory"
i = 0
while i < 10:
    index = random.randrange(0, len(course_by))
    print(course_by[index])
    i = i + 1

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
"неожиданного праздника", "приятных перемен"]
generated_prophecies = []
i = 0
while i < 3:
    index_t = random.randrange(0, len(times))
    index_a = random.randrange(0, len(advices))
    index_p = random.randrange(0, len(promises))
    print(times[index_t] + " " + advices[index_a] + " " + promises[index_p])
    i = i + 1

i = 0
while i < 3:
    t = random.choice(times)
    a = random.choice(advices)
    p = random.choice(promises)
    print(t + " " + a + " " + p)
    i = i + 1