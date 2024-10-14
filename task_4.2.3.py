
def get_higher_prise(percent, price):
    return round(price * (1 + percent / 100), 2)

prices_now = [1.09, 23.56, 57.84, 4.56, 6.78]

for i_price in prices_now:
    print('Цена на товар:', i_price)

first_persent = int(input('Повышение на первый год: '))
second_persent = int(input('Повышение на второй год: '))

prices_first = [get_higher_prise(first_persent, i_price) for i_price in prices_now]
prices_second = [get_higher_prise(second_persent, i_price) for  i_price in prices_first]

print('Сумма цен за каждый год:', round(sum(prices_now), 2), round(sum(prices_first),2), round(sum(prices_second), 2))
