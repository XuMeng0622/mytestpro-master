from count import Calculator
import unittest

class TestCount(unittest.TestCase):
    def __init__(self):
        self.calcutor = Calculator(3, 5)

    def setUp(self):
        pass
        # print('setUp...')

    def test_add(self):
        add_result = self.calcutor.add()
        self.assertEqual(add_result, 8, msg='add result is not 8')

    def test_sub(self):
        sub_reult = self.calcutor.sub()
        self.assertEqual(sub_reult, -2)

    def test_mul(self):
        mul_reult = self.calcutor.mul()
        self.assertEqual(mul_reult, 15)

    def test_div(self):
        div_reult = self.calcutor.div()
        self.assertEqual(div_reult, 0.6)

    def tearDown(self):
        pass
        # print('tear Down...')


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestCount('test_add'))
    suit.addTest(TestCount('test_sub'))
    suit.addTest(TestCount('test_mul'))
    suit.addTest(TestCount('test_div'))

    runner = unittest.TextTestRunner()
    runner.run(suit)
