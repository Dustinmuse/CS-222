class MathUtilities: #if it is static it doesn't need any objects
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

result = MathUtilities.add(5, 3)
print(result)