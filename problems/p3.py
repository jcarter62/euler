from math import floor
import json


class P3:
    """
    Largest prime factor

    Problem 3
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
    """

    def __init__(self, num: int = 600851475143):
        self.description = 'What is the largest prime factor of the number 600851475143 ?'
        self.result = self.calc(number=num)

    def __str__(self):
        result = json.dumps({
            'description': self.description,
            'result': self.result
        })
        return result

    def calc(self, number: int):
        factors = self.find_factors(number)
        largest_factor = self.find_largest(factors)
        return largest_factor

    def find_largest(self, facts):
        result = 0
        for fact in facts:
            if fact > result:
                result = fact
        return result

    def find_factors(self, n):
        factor_values = []
        i = 2
        num = n
        while (i > 1) and (i < floor(n / 2.0)):
            if num % i == 0:
                factor_values.append(i)
                num = int(num / i)
                if n == self.multiply_factors(factor_values):
                    return factor_values
            else:
                i = i + 1
        return factor_values

    def multiply_factors(self, factors):
        result = 1
        for fact in factors:
            result = result * fact
        return result
