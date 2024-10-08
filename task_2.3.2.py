msg = input("Введите строку: ")
index_of_letter = int(input("Номер символа: ")) - 1  # сразу отнимаем 1, чтобы превратить номер в индекс
letters = list(msg)
count = 0
if index_of_letter > 0:
    print("Символ слева:", letters[index_of_letter - 1])
    if letters[index_of_letter - 1] == letters[index_of_letter]:
        count += 1
if index_of_letter < len(letters) - 1:
    print("Символ справа:", letters[index_of_letter + 1])
    if letters[index_of_letter + 1] == letters[index_of_letter]:
        count += 1

if count == 0:
    print("Таких же символов нет.")
elif count == 1:
    print("Есть ровно один такой же символ.")
elif count == 2:
    print("Таких символов два.")
