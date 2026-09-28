from math import gcd

class Fraction:
    def __init__(self, num, den):
        if den == 0:
            raise ZeroDivisionError("Деление на ноль недопустимо")

        if den < 0:
            den, num = -den, -num
            
        self.num = num
        self.den = den
        self.sokr()

    def sokr(self):
        d = gcd(abs(self.num), self.den)
        self.num //= d
        self.den //= d

    def __str__(self):
        if self.num == 0: return '0'

        s = ''
        num = self.num
        if num < 0:
            s = '-'
            num = abs(num)

        if num < self.den:
            return f"{s}{num}/{self.den}"

        if num % self.den == 0:
            return f"{s}{num // self.den}"

        return f"{s}{num // self.den} {num % self.den}/{self.den}"

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        if other.num == 0:
            raise ZeroDivisionError("Деление на ноль недопустимо")
        return Fraction(self.num * other.den, self.den * other.num)

    def __add__(self, other):
        return Fraction(self.num * other.den + self.den * other.num, self.den * other.den)

    def __sub__(self, other):
        return Fraction(self.num * other.den - other.num * self.den, self.den * other.den)

    def __pow__(self, power):
        if power >= 0:
            return Fraction(self.num ** power, self.den ** power)

        return Fraction(self.den ** (-power), self.num ** (-power))

def read_fraction(text):
    p = list(map(int, text.split("/")))
    if len(p) == 1:
        return Fraction(p[0], 1)
    if len(p) == 2:
        return Fraction(p[0], p[1])
    raise ValueError("Некорректный ввод")

a = read_fraction(input("Введите первую дробь a/b или целое число: "))
oper = input("Введите знак операции (+, -, *, **, /): ")
if oper == "**":
    power = int(input("Введите степень, в которую хотите возвести число: "))
    res = a ** power
else:
    b = read_fraction(input("Введите вторую дробь a/b или целое число: "))

    if oper == "+":
        res = a + b
    elif oper == "-":
        res = a - b
    elif oper == "*":
        res = a * b
    elif oper == "/":
        res = a / b
    else:
        raise ValueError("Операция указана некорректно")

print("Ответ:", res)





