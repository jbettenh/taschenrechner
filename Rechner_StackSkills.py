#Mein Taschenrechner mit Python und Kivy
import re
import kivy
kivy.require("1.9.0")

print("Mein Taschenrechner")
print("Tippen Sie 'beenden', um die App zu aufgeben.\n")
previous = 0
run = True


def perform_math():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Geben Sie die Gleichung ein:")
    else:
        equation = input(str(previous))

    if equation == 'beenden':
        print("Aufwiedersehen!")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    perform_math()