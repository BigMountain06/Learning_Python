# Расходы на автомобиль

def raschot_summ(num1, num2, num3, num4, num5, num6):
    a = num1 + num2 + num3 + num4 + num5 + num6
    return a, a * 12

def main():
    print('Месячные расходы:')
    kredit = float(input('Креди­т: '))
    strahovka = float(input('Страховка: ')) 
    benzin = float(input('Бензин: '))
    maslo = float(input('Машинное масло: '))
    shini = float(input('Шины: ')) 
    teh_osmotr = float(input('Техобслуживание: '))
    obshaya_summa, godovaya_summa = raschot_summ(kredit, strahovka, benzin, maslo, shini,teh_osmotr)
    print(f'\nОбщая сумма состовляет: {obshaya_summa:.2f}')
    print(f'Годовая сумма состовляет: {godovaya_summa:.2f}')

if __name__ == "__main__":
    main()