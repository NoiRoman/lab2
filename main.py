import math

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b
def mod(a, b): return a % b
def power(a, b): return a ** b
def my_sqrt(x): return math.sqrt(x)
def my_floor(x): return math.floor(x)
def my_ceil(x): return math.ceil(x)
def my_sin(x): return math.sin(x)
def my_cos(x): return math.cos(x)


memory = 0
def m_plus(x):
    global memory
    memory += x

def m_minus(x):
    global memory
    memory -= x

def m_clear():
    global memory
    memory = 0


def main():
    global memory
    while True:
        print("\n=== Калькулятор by Roman ===")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Остаток от деления")
        print("6. Sin")
        print("7. Cos")
        print("8. Возведение в степень")
        print("9. Квадратный корень от числа")
        print("10. Округление в меньшую сторону")
        print("11. Округление в большую сторону")
        print("12. Работа с памятью")
        print(f"Текущая память: {memory}")
        print("0. Выход")

        choice = input("Ваш выбор: ")

        
        if choice in ['1', '2', '3', '4', '5', '8']:
            try:
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))
            except ValueError:
                print("Ошибка: нужно вводить числа!")
                continue

            if choice == '1': print(f"Результат: {add(a, b)}")
            elif choice == '2': print(f"Результат: {sub(a, b)}")
            elif choice == '3': print(f"Результат: {mul(a, b)}")
            elif choice == '4':
                if b == 0: print("Ошибка: деление на ноль!")
                else: print(f"Результат: {div(a, b)}")
            elif choice == '5':
                if b == 0: print("Ошибка: деление на ноль!")
                else: print(f"Результат: {mod(a, b)}")
            elif choice == '8': print(f"Результат: {power(a, b)}")

        
        elif choice in ['6', '7', '9', '10', '11']:
            try:
                x = float(input("Введите число: "))
            except ValueError:
                print("Ошибка: нужно вводить числа!")
                continue

            if choice == '6': print(f"Результат: {my_sin(x)}")
            elif choice == '7': print(f"Результат: {my_cos(x)}")
            elif choice == '9':
                if x < 0: print("Ошибка: корень из отрицательного числа!")
                else: print(f"Результат: {my_sqrt(x)}")
            elif choice == '10': print(f"Результат: {my_floor(x)}")
            elif choice == '11': print(f"Результат: {my_ceil(x)}")

        
        elif choice == '12':
            print("1. m+ (прибавить)")
            print("2. m- (вычесть)")
            print("3. mc (очистить)")
            mem = input("Действие: ")
            if mem == '1':
                try: m_plus(float(input("Число: "))); print(f"Память: {memory}")
                except ValueError: print("Ошибка ввода!")
            elif mem == '2':
                try: m_minus(float(input("Число: "))); print(f"Память: {memory}")
                except ValueError: print("Ошибка ввода!")
            elif mem == '3':
                m_clear(); print("Память очищена.")

        elif choice == '0':
            print("Выход...")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()