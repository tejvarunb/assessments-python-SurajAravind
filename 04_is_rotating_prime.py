import unittest

question_04 = """
Rotating primes

Given an integer n, return whether every rotation of n is prime.
Example 1:
Input:
n = 199
Output:
True
Explanation:
199 is prime, 919 is prime, and 991 is prime.

Example 2:
Input:
n = 19
Output:
False
Explanation:
Although 19 is prime, 91 is not.
"""


## Code taken from Thrigun Meduri
# Implement the below function and run the program

def is_rotating_prime(num):
    x=list(str(num))
    flag=False
    flag1=[]
    flage2=False
    for i in range(len(x)):
        t=x.pop()
        x.insert(0, t)
        y=""
        for ele in x:
            y+=ele
        z=int(y)
        if z>1:
            for i in range(2, z):
                if(z%i==0):
                    flag=True
                    break
        if flag:
            flag1.append(False)
        else:
            flag1.append(True)
    for i in flag1:
        if i==True:
            flag2=True
            continue
        else:
            flag2=False
            break
    if flag2:
        return True
    else:
        return False


class TestIsRotatingPrime(unittest.TestCase):

    def test_1(self):
        self.assertEqual(is_rotating_prime(2), True)

    def test_2(self):
        self.assertEqual(is_rotating_prime(199), True)

    def test_3(self):
        self.assertEqual(is_rotating_prime(19), False)

    def test_4(self):
        self.assertEqual(is_rotating_prime(791), False)

    def test_5(self):
        self.assertEqual(is_rotating_prime(919), True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
