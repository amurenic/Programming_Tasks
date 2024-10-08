nums_list = []

N = int(input('Кол-во чисел в списке: '))

for i in range(1, N + 1):
    print("Введите ", i, "число: ")
    num = int(input())
    nums_list.append(num)

divider = int(input('Введите делитель: '))
index = 0
sum_indexes = 0
for number in nums_list:
    if number % divider == 0:
        print("Индекс числа", number, ":", index)
        sum_indexes += index
    index += 1

print("Сумма индексов:", sum_indexes)

# Вариант с новыми инструментами (enumerate и f-strings)

sum_indexes = 0
for index, number in enumerate(nums_list):  # enumerate в таких случаях очень полезен
    if number % divider == 0:
        print(f"Индекс числа {number}: {index}")
        sum_indexes += index
