import json

class P5:
    """
    Smallest multiple

    Problem 5
    2520 is the smallest number that can be divided by each
    of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    def __init__(self, low: int = 1, high: int = 20):
        self.low = low
        self.high = high
        self.description = 'What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'
        value = self.calc()
        self.result = value

    def __str__(self):
        result = json.dumps({
            'description': self.description,
            'result': self.result
        })
        return result

    def calc(self):
        """
        Determine the smallest number that is divisible by numbers 1 to 20.
        """
        num = 22
        while not self.divisible(num):
            # we know that only even numbers are divisible by 2, so
            # we only inspect even numbers.
            num = num + 2
            if num % 10000:
                print(str(num), end='\r')

        return num

    def divisible(self, n):
        result = True
        for factor in range(self.low+1, self.high):
            if n % factor != 0:
                result = False
                break
        return result
