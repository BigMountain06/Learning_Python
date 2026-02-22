# Налог на недвижимое имущество

def otsenochnaya_stoimost(stoimost):
    return stoimost * 0.6

def nalog_na_imushestvo(stoimost):
    return (stoimost / 100) * 0/72

def main():
    stoimost_imushestva = float(input(f'Введите стоимость имущества: '))
    otsenochnaya_stoimost_imushestva = otsenochnaya_stoimost(stoimost_imushestva)
    nalog = nalog_na_imushestvo(otsenochnaya_stoimost_imushestva)
    print(f"\nОценочная стоимость имущества состовляет: {otsenochnaya_stoimost_imushestva:.2f}")
    print(f"Налог на оценочную стоимость состовляет: {nalog:.2f}")

if __name__ == '__main__':
    main()