money_capital = 20000  
salary = 5000  
spend = 6000  
increase = 0.05  

months_without_debts = 0

while money_capital >= 0:
    total_income = salary  
    current_spend = spend  
    budget = total_income + money_capital

    if budget >= current_spend:
        months_without_debts += 1  
        money_capital -= max(0, current_spend - total_income)  
    else:
        break  

    spend *= (1 + increase)

print("Количество месяцев, которое можно протянуть без долгов:", months_without_debts)