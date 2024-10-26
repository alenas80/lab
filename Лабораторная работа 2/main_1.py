money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

kol_month = 0
while salary + money_capital > spend:
    money_capital -= spend - salary
    kol_month += 1
    spend += spend * increase

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
print("Количество месяцев, которое можно протянуть без долгов:", kol_month)
