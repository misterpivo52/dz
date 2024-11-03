
class FactorialCalculator:
    cache = {}

    @staticmethod
    def factorial(n):
        if n < 0:
            raise ValueError("only positive numbers are allowed")
        elif n in (0, 1):
            return 1

        if n in FactorialCalculator.cache:
            return FactorialCalculator.cache[n]

        result = n * FactorialCalculator.factorial(n - 1)
        FactorialCalculator.cache[n] = result
        return result
if __name__ == '__main__':
    print(FactorialCalculator.factorial(int(input("enter number"))))