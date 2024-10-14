original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]

current_prices = [(price
                   if price > 0 else 0)
                  for price in original_prices]

print('Текущий список цен',current_prices)