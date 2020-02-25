import json


class P7:
    """
    Problem 7
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
    we can see that the 6th prime is 13.

    What is the 10 001st prime number?
    """
    def __init__(self):
        self.description = 'What is the 10 001st prime number?'
        value = self.calc(nth=10002)
        self.result = {'value': value}

    def __str__(self):
        result = json.dumps({
            'description': self.description,
            'result': self.result,
        })
        return result

    def calc(self, nth: int):
        result = 0
        result_1 = 0
        result_2 = 0
        current_th = 0
        n = 1
        while current_th < nth:
            if self.is_prime(n):
                result_2 = result_1
                result_1 = result
                result = n
                current_th += 1
            n += 1
        return [result_2, result_1, result]

    @staticmethod
    def is_prime(n):
        result = True
        if n > 1:
            for i in range(2, n//2):
                if n % i == 0:
                    result = False
                    break
        else:
            result = False
        return result
