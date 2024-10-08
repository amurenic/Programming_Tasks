# №1 Можно изначально не добавлять нулевые значения в список
number_of_workers = int(input("Кол-во сотрудников: "))
wages_of_workers = []
for i in range(number_of_workers):
    wage = int(input(f"Зарплата {i + 1} сотрудника: "))
    if wage > 0:
        wages_of_workers.append(wage)

print("Осталось сотрудников:", len(wages_of_workers))
print("Зарплаты:", wages_of_workers)

# №2 Можно сперва собрать все зарплаты, затем "удалить" их, собрав подходящие элементы в новый список
# number_of_workers = int(input("Кол-во сотрудников: "))
# wages_of_workers = []
# for i in range(number_of_workers):
#     wage = int(input(f"Зарплата {i + 1} сотрудника: "))
#     wages_of_workers.append(wage)
#
# new_workers = []
# for worker in wages_of_workers:
#     if worker > 0:
#         new_workers.append(worker)
#
# print("Осталось сотрудников:", len(new_workers))
# print("Зарплаты:", new_workers)

# №3 Можно и напрямую удалять нулевые элементы, но делать это надо осторожно
# number_of_workers = int(input("Кол-во сотрудников: "))
# wages_of_workers = []
# for i in range(number_of_workers):
#     wage = int(input(f"Зарплата {i + 1} сотрудника: "))
#     wages_of_workers.append(wage)
#
# index = 0
# while index < len(wages_of_workers):
#     if wages_of_workers[index] == 0:
#         wages_of_workers.pop(index)
#     else:
#         index += 1  # увеличивать индекс надо только без удаления
        # это нужно чтобы из-за сдвига не пропустить следующий за удаленным элемент списка
# print("Осталось сотрудников:", len(wages_of_workers))
# print("Зарплаты:", wages_of_workers)

#
# Дополнительно: выведите на экран максимальную и минимальную зарплату оставшихся сотрудников.
# Для этого используйте функции max и min. Да, те самые, которыми нельзя называть переменные. В скобках функций просто укажите список.
#
#
#
# Пример:
#
# Максимальная зп: 60000
#
# Минимальная зп: 10000
#
#
#

print("Максимальная зп:", max(wages_of_workers))
print("Минимальная зп:", min(wages_of_workers))
