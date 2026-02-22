# Cтоимость страховки

def minimum(stoimost):
    return stoimost * 0.8

def main():
    stoimost_stroyeniya = float(input('Введите стоимость строения: '))
    min_strahovaya_sum = minimum(stoimost_stroyeniya)
    print(f"\nМинимальная страховая сумма: {min_strahovaya_sum:.2f}")

if __name__ == "__main__":
    main()