"""
https://drive.google.com/file/d/1o92GnkFeGTsCrdlCiJi1z8ndg0XsIIFb/view?usp=sharing
это - ссылка на все диаграммы ко всем решённым мной задачам в одном файле от diagrams.net
Но у меня при проверке ссылки в режиме инкогнито открывается только картинка с первой диаграммой
поэтому к кажд след задаче прикрепила ссылку на её диаграму на diagrams.net (перестраховка)

Задача1. Найти сумму и произведение цифр трехзначного числа,
которое вводит пользователь.
Решение:
"""
print('Сумма и произведение цифр трёхзначного числа')

a = int(input('Введите первую цифру трёхзначного числа: '))
b = int(input('Введите вторую цифру трёхзначного числа: '))
c = int(input('Введите третью цифру трёхзначного числа: '))

print(f'Сумма цифр введённого трёхзначного числа {a}{b}{c} равна {a + b + c}.')
print(f'Произведение цифр введённого трёхзначного числа {a}{b}{c} равно {a * b * c}.')
