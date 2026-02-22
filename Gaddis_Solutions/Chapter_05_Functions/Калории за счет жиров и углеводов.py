# Калории за счет жиров и углеводов

# Количество калорий от жиров и углеводов
def kalorii(value1, value2):
    return value1 * 9, value2 * 4

#Главная функция
def main():
    print('Введите количество употреблённых за день')
    jirov = float(input('жиров: '))
    uglevodov = float(input('углеводов: '))
    kaloriy_ot_jirov, kaloriy_ot_ulevodov = kalorii(jirov, uglevodov)
    print(f"\nВы за день употребили {kaloriy_ot_jirov:.2f} калорий от жиров и {kaloriy_ot_ulevodov:.2f} калорий от углеводов.")

if __name__ == "__main__":
    main()