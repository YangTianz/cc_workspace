class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def sqrt(self, a):
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return a ** 0.5

    def pow(self, base, exponent):
        return base ** exponent


def main():
    print("Hello from ai-agent!")
    calc = Calculator()
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    print(f"√16 = {calc.sqrt(16)}")
    print(f"√25 = {calc.sqrt(25)}")
    print(f"2^8 = {calc.pow(2, 8)}")
    print(f"5^3 = {calc.pow(5, 3)}")


if __name__ == "__main__":
    main()
