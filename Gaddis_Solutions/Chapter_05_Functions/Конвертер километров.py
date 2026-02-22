# Конвертер километров

# Конвертер
def converter(s):
    return s * 0.6214

# Главная функция
def main():
    km = float(input("Введите расстояние в км: "))
    mils = converter(km)
    print(f'В милях это будет: {mils:.1f}')

if __name__ == "__main__":
    main()