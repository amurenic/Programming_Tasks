num_a = int(input('Левая граница: '))
num_b = int(input('Правая граница: '))

cubes = [num ** 3 for num in range(num_a, num_b + 1)]
squares = [num ** 2 for num in range(num_a, num_b + 1)]

print(f'Список кубов чисел в диапазоне от {num_a} до {num_b}:', cubes)
print(f'Список квадратов чисел в диапазоне от {num_a} до {num_b}:', squares)


