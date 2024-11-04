salary = 5000 
spend = 6000 
months = 10 
increase = 0.03 

total_savings = 0

for month in range(months):
    total_income = salary
    current_spend = spend
    total_income -= current_spend

    if total_income < 0:
        total_savings += abs(total_income)
    spend *= (1 + increase)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(total_savings))