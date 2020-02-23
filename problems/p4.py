import json

class P4:
    """
    Largest palindrome product

    Problem 4
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    def __init__(self):
        self.a = 0
        self.b = 0
        self.description = 'Find the largest palindrome made from the product of two 3-digit numbers.'
        value = self.calc()
        self.result = {'value': value, 'numbers': [self.a, self.b]}

    def __str__(self):
        result = json.dumps({
            'description': self.description,
            'result': self.result,
            'a': self.a,
            'b': self.b
        })
        return result

    def calc(self):
        largest = 0
        a_value = 0
        b_value = 0

        for a in range(100, 999):
            for b in range(100, 999):
                product = a * b
                if product > largest:
                    sprod = str(product)
                    rprod = sprod[::-1]
                    if sprod == rprod:
                        if product > largest:
                            largest = product
                            a_value = a
                            b_value = b

        self.a = a_value
        self.b = b_value
        return largest
