from http.cookiejar import month

money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05
months= 0

while money_capital >= spend:
  money_capital += salary - spend
  spend += spend * increase
  months += 1
print("Количество месяцев, которое можно протянуть без долгов:", months)
