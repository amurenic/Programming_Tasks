num_1 = int(input('Первое число: '))
num_2 = int(input('Второе число: '))

num_list = [x for x in range(num_1, num_2 +1) if x % 2 == 0]

print(f'Список чётных чисел в интервале от {num_1} до {num_2}: {num_list}')