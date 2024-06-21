print('1. Задача "Длина слова"')
a = 'Произвольная строка для вывода её длины'
print('Длина строки: "' + a + '" =', len(a), '\n')  # \n для того, чтобы визуально разделить задачи пустой строкой :)

print('2. Задача "Суммы и разности"')
first = 13
second = 28
summa = first + second
diff = first - second
print('first =', first, '\n' + 'second =', second)
print('first + second =', summa, '- сумма(summa)', '\n' + 'first - second =', diff, '- разность(diff)' + '\n')

print('3. Задача "Среднее арифметическое"')
first = 11
second = 22
third = 33
elements = (first, second, third)
mean = sum(elements) / len(elements)
print('first =', first, '\n' + 'second =', second, '\n' + 'third =', third)
print('(first + second + third) / n = (', first, ' + ', second, ' + ', third, ') / ', len(elements), ' = ', mean, ' - среднее значение(mean)', '\n', sep='')  # sep для того, чтобы убрать пробел между скобками и числами 11 и 33

print('4. Задача "Простые строчки"')
first_string = 'Вторник'
second_string = 'Понедельник'
print('first_string =', first_string, '\n' + 'second_string =', second_string)
print(second_string + ', ' + first_string, '\n')

print('5. Задача "Сложная формула"')
a = 3
b = 9
c = 5
f = a * b + a * c
print('a =', a, '\n' + 'b =', b, '\n' + 'c =', c)
print('f = (a * b) + (a * c) = (', a, ' * ', b, ') + (', a, ' * ', c, ') = ', f, sep='')
print('f^3 / 2 = ', f, '^3 / 2 = ', f**3/2, sep='')
