salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0
for month in range(1, months + 1):
    # Расходы текущего месяца
    monthly_expense = spend * (1 + increase) ** (month - 1)

    # Расходы, которые можно покрыть зарплатой
    covered_by_salary = min(salary, monthly_expense)

    # Расходы, которые не покрыты зарплатой (нехватка средств)
    shortfall = monthly_expense - covered_by_salary

    # Обновляем подушку безопасности
    money_capital += shortfall

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital, 2))
