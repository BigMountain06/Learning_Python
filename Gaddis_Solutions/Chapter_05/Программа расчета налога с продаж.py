# Программа расчета налога с продаж

# 1. Функция для расчета федерального налога (например, 5%)
def calc_federal_tax(amount):
    return amount * 0.05

# 2. Функция для расчета регионального налога (например, 2.5%)
def calc_regional_tax(amount):
    return amount * 0.025

# 3. Главная функция
def main():
    # Получаем сумму покупки от пользователя
    purchase = float(input("Введите сумму покупки: "))
    
    # Считаем налоги, вызывая функции сверху
    fed_tax = calc_federal_tax(purchase)
    reg_tax = calc_regional_tax(purchase)
    
    # Считаем общую сумму (покупка + оба налога)
    total = purchase + fed_tax + reg_tax
    
    # Выводим всё на экран
    print(f"\nСумма покупки: {purchase:.2f}")
    print(f"Федеральный налог: {fed_tax:.2f}")
    print(f"Региональный налог: {reg_tax:.2f}")
    print(f"Общая сумма: {total:.2f}")

if __name__ == "__main__":
    main()