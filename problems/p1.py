
class P1:
    """
    Multiples of 3 and 5

    Problem 1
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    def __init__(self, num=1000):
        self.result = self.calc(num=num)
        self.description = 'Multiples of 3 and 5, between 0 and ' + str(num)

    def calc(self, num: int) -> int:
        n = 3
        result = 0
        while n < num:
            if n % 3 == 0:
                result = result + n
            elif n % 5 == 0:
                result = result + n
            n += 1
        return result
