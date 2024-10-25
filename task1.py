money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05

months = 0

while True:

    budget = salary + money_capital
    if budget >= spend:
        months += 1
        money_capital -= (spend - salary)
        spend *= (1 + increase)
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", months)
