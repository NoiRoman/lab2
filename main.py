import math
def main():
    print("=== Калькулятор ===")
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
    print("0. Выход")

def add(a, b): return a + b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b
def mod(a,b): return a%b

def power(a,b): return a**b
def my_sqrt(x): return math.sqrt(x)

def my_floor(x): return math.floor(x)
def my_ceil(x): return math.ceil(x)

def my_sin(x): return math.sin(x)
def my_cos(x): return math.cos(x)

memory = 0
def m_plus(x): global memory; memory += x



if __name__ == "__main__":
    main()