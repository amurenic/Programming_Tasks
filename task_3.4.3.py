goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]

new_fruit_name = input("Новый фрукт: ")
new_fruit_price = int(input("Цена: "))

goods.append([new_fruit_name, new_fruit_price])

print("Новый ассортимент:", goods)

for good in goods:
    good[1] = round(good[1] * 1.08, 2)

print("Новый ассортимент с увел. ценой:", goods)
