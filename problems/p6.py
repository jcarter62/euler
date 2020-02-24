import json


class P6:
    """
    Problem 6
    The sum of the squares of the first ten natural numbers is,

    1^2+2^2+...+10^2=385
    The square of the sum of the first ten natural numbers is,

    (1+2+...+10)^2=55^2=3025
    Hence the difference between the sum of the squares of the first ten natural numbers
    and the square of the sum is 3025−385=2640.

    Find the difference between the sum of the squares of the first one hundred natural
    numbers and the square of the sum.
    """
    def __init__(self, first_n: int = 100):
        self.description = 'Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'
        self.first_n = first_n
        sq_sum = self.calc_square_sum(self.first_n)
        sum_sq = self.calc_sum_square(self.first_n)
        value = sum_sq - sq_sum
        self.result = {'result': value}

    def __str__(self):
        result = json.dumps({
            'description': self.description,
            'result': self.result,
        })
        return result

    @staticmethod
    def calc_square_sum(n):
        result = 0
        for i in range(n+1):
            result = result + (i * i)
        return result

    @staticmethod
    def calc_sum_square(n):
        result = 0
        for i in range(n+1):
            result = result + i
        result = result * result
        return result
