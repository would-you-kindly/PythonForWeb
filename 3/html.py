# fp = open("index.html", "w")
# print("<h1>Заголовок</h1>", file=fp)
# fp.close()

# coding: utf-8 (почему-то иероглифы с utf-8)
from horoscope import generate_prophecies
from datetime import datetime as dt

def generate_page(head, body):
    page = f"""<!DOCTYPE html>
    <html>
    {head}
    {body}
    </html>"""
    return page

def generate_head(title):
    head = "<title>" + title + "</title>"
    return "<head>" + head + "</head>"

def generate_body(header, paragraphs):
    body = "<h1>" + header + "</h1>"
    for p in paragraphs:
        body = body + "<p>" + p + "</p>"
    return "<body>" + body + "</body>"

def save_page(title, header, paragraphs, output="index.html"):
    fp = open(output, "w")
    today = dt.now().date()
    page = generate_page(
        head=generate_head(title),
        body=generate_body(header=header, paragraphs=paragraphs)
    )
    print(page, file=fp)
    fp.close()

today = dt.now().date()
save_page(
    title="Гороскоп на сегодня", header="Что день " + str(today) + " готовит",
    paragraphs=generate_prophecies(),
)

header = "Основное предсказание"
forecast = "На днях будет четверг. На днях был четверг."
paragraph = "<h1>%s</h1><p>%s</p>" % (header, forecast)

header = "Основное предсказание"
paragraph = "<{tag}>{content}</{tag}>".format(tag="h1", content=header)
paragraph = "<{0}>{1}<{0}>".format("h1", header)
paragraph = f"<{header}>" # f-строки

cycles = ["утро", "день", "вечер", "ночь"]
for i in range(len(cycles)):
    print(cycles[i])