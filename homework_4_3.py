'''Задача 3. Список цифр числа'''

# Решение 1
number = int(input('Введите целое неотрицательное число: '))

result = []

while number > 0:
    i = number % 10
    result.append(i)                      # получаем последнюю цифру числа
    number //= 10                         # удаляем последнюю цифру

print(result[::-1])                       # Для разворота списка [::-1]

# Решение 2
number = input('Введите целое неотрицательное число: ')
number_list = list(map(int, str(number)))
print(number_list)

# Решение 3
number = input('Введите целое неотрицательное число: ')
number_list = [int(i) for i in str(number)]
print(number_list)






