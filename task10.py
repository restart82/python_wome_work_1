# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

import random

coins_number = int(input("Введите количество монет >"))

coins = []
i = 0

# Заполняем массив расположений монет:
while i < coins_number:
    coins.append(random.randint(0, 1))
    i += 1

count = 0

# Считаем "решки"
for i in coins:
    if i == 1:
        count += 1

print("Вот такие выпали значения монет:")
print(coins)

if count <= (coins_number / 2):
    print(f'Нужно перевернуть {count} монет')
else:
    print(f'Нужно перевернуть {coins_number - count} монет')