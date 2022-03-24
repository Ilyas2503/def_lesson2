lesson="""Написать Функцию которая принимает предложение
как аргумент, считает количество букв и возвращает
сколько символов он ввёл. НЕ ИСПОЛЬЗОВАТЬ функцию len()
"""
def argument(lesson):
    count = 0
    for i in lesson:
        count += 1
    return count
print(argument(lesson))