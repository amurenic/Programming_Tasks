count_of_workers = int(input("Кол-во сотрудников в офисе: "))
workers_id = []
for _ in range(count_of_workers):
    worker_id = int(input("ID сотрудника: "))
    workers_id.append(worker_id)

search_id = int(input("Какого сотрудника ищем? "))

# search = False
# for id in workers_id:
#     if id == search_id:
#         search = True
#
# if search:
#     print("Сотрудник работает!")
# else:
#     print("Сотрудник не работает!")


if search_id not in workers_id:  # Благодаря оператору in поиск можно упростить
    print("Сотрудник не работает!")
else:
    print("Сотрудник работает!")
