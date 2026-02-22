# Сидячие места на стадионе

# Стоимость мест в классах в долларах
A = 20
B = 15
C = 10

# Прибыль от мест каждого класса
def get_profit(value1, value2, value3):
    value01 = value1 * A
    value02 = value2 * B
    value03 = value3 * C
    total = value01 + value02 + value03
    return value01, value02, value03, total

# Главная функция
def main():
    tickets_a = int(input('Сколько билетов на места класса A было продано? \nВведите количество: '))
    tickets_b = int(input('А B класса? \nВведите количество: '))
    tickets_c = int(input('А C класса? \nВведите количество: '))

    profit_a, profit_b, profit_c, total_profit = get_profit(tickets_a, tickets_b, tickets_c)
    
    print(f'\nПрибыль от класса А состовляет {profit_a} долларов, с класса В {profit_b} долларов и с класса С {profit_c} долларов.')
    print(f'Общая сумма прибыли состовляет {total_profit} долларов.')

if __name__ == '__main__':
    main()