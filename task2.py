salary = 5000
spend = 6000
months = 10
increase = 0.03

total_spend = 0

for month in range(months):
    total_spend += spend
    spend *= (1 + increase)

needed_capital = total_spend - (salary * months)
needed_capital = max(0, needed_capital)
needed_capital = round(needed_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {needed_capital}")
