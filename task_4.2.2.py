line = input('Введите строку: ')
symbol = input('Введите символ: ')

double_sym_list = [sym * 2 for sym in line]
plus_sym_list = [sym + symbol for sym in line]

print('Список удвоенных символов:', double_sym_list)
print('Склейка с дополнительным символом: ', plus_sym_list)