class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            return "Error: Division by zero is undefined"
        return self.num1 / self.num2


if __name__ == "__main__":
    while True:
        calc = Calculator(float(input("enter first number")), float(input("enter second number")))

        print("Addition:", calc.add())
        print("Subtraction:", calc.subtract())
        print("Multiplication:", calc.multiply())
        print("Division:", calc.divide())
        contan = input("Do you want to continue?(y/n)")
        if contan == "y":
            continue
        if contan == "n":
            break
        else:
            print("Invalid input")
            contan = input("Do you want to continue?(y/n)")
